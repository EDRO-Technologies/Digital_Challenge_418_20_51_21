from uuid import UUID, uuid4

from app.api.schemas.user import UserLogin
from app.common.auth_utils import is_valid_password, jwt_decode, jwt_encode
from app.common.exceptions import (
    InvalidCredentials,
    InvalidToken,
    RedirectWrongUserIP,
)
from app.common.settings import settings
from app.dto.token import Token
from app.ports.uow import UoW


class AuthService:
    async def authenticate(
        self, user: UserLogin, auth_ip: str, uow: UoW
    ) -> Token:
        async with uow:
            db_user = await uow.users.get_user_by_user_login(user.login)
            if not db_user:
                raise InvalidCredentials

            if not is_valid_password(user.password, db_user.password):
                raise InvalidCredentials

            white_ip_list = await uow.refresh_users.get_user_white_ip_list(
                db_user.id
            )
            if not white_ip_list:
                white_ip_list = []
            white_ip_list.append(auth_ip)
            refresh_user_id = await uow.refresh_users.add_ip_to_white_ip_list(
                db_user.id, set(white_ip_list)
            )
            access_token = await self.create_access_token(db_user.id)
            refresh_token = await self.create_refresh_token(db_user.id)
            await uow.refresh_tokens.add_one_token(
                {
                    "id": uuid4(),
                    "refresh_user_id": refresh_user_id,
                    "token": refresh_token,
                }
            )
            await uow.commit()
            return Token(
                access_token=access_token,
                refresh_token=refresh_token,
                expires_in=settings.auth_settings.ACCESS_TOKEN_EXPIRE_SECONDS,
            )

    async def create_refresh_token(self, user_id: UUID) -> str:
        refresh_token = jwt_encode(
            payload={"sub": str(user_id), "iss": "dc2024"},
            expire_time_seconds=settings.auth_settings.REFRESH_TOKEN_EXPIRE_SECONDS,
        )
        return refresh_token

    async def create_access_token(self, user_id: UUID) -> str:
        access_token = jwt_encode(
            payload={"sub": str(user_id), "iss": "dc2024"},
            expire_time_seconds=settings.auth_settings.ACCESS_TOKEN_EXPIRE_SECONDS,
        )
        return access_token

    async def logout(self, refresh_token: str, uow: UoW) -> None:
        async with uow:
            await uow.refresh_tokens.delete_by_refresh_token(refresh_token)
            await uow.commit()

    async def refresh_token(
        self, refresh_token: str, request_ip: str, uow: UoW
    ) -> Token:
        async with uow:
            if not refresh_token:
                raise InvalidToken

            user_id = jwt_decode(refresh_token).get("sub")
            refresh_user = await uow.refresh_users.get_user_by_id(
                UUID(user_id)
            )
            if not refresh_user:
                raise InvalidToken

            if request_ip not in refresh_user.white_ip_list:
                raise RedirectWrongUserIP

            db_refresh_token = (
                await uow.refresh_tokens.get_by_refresh_user_id_and_token(
                    refresh_user.id, refresh_token
                )
            )

            if len(list(refresh_user.refresh_tokens_model)) >= 10:
                await uow.refresh_tokens.delete_by_refresh_user_id(
                    refresh_user.id, refresh_token
                )
            elif db_refresh_token:
                await uow.refresh_tokens.delete_one_by_id(db_refresh_token.id)
            access_token = await self.create_access_token(user_id)
            refresh_token = await self.create_refresh_token(user_id)
            await uow.refresh_tokens.add_one_token(
                {
                    "id": uuid4(),
                    "refresh_user_id": refresh_user.id,
                    "token": refresh_token,
                }
            )
            await uow.commit()
            return Token(
                access_token=access_token,
                refresh_token=refresh_token,
                expires_in=settings.auth_settings.ACCESS_TOKEN_EXPIRE_SECONDS,
            )
