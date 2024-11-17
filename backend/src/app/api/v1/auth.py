from typing import Annotated

from fastapi import APIRouter, Body, Depends, Request, Response

from app.api.schemas.user import UserLogin
from app.common.settings import settings
from app.dto.token import Token
from app.ports.uow import UoW
from app.services.auth import AuthService

router = APIRouter(prefix="/auth")


@router.post("/login", status_code=200, response_model=Token)
async def user_login(
    request: Request,
    response: Response,
    uow: Annotated[UoW, Depends()],
    service: Annotated[AuthService, Depends()],
    user: Annotated[UserLogin, Body()],
):
    token = await service.authenticate(user, request.client.host, uow)
    # await service.add_new_ip_to_white_ip_list(request.client.host)
    response.set_cookie(
        "access_token",
        token.access_token,
        max_age=settings.auth_settings.ACCESS_TOKEN_EXPIRE_SECONDS,
        httponly=True,
    )
    response.set_cookie(
        "refresh_token",
        token.refresh_token,
        max_age=settings.auth_settings.REFRESH_TOKEN_EXPIRE_SECONDS,
        httponly=True,
    )
    return token


@router.post("/refresh", response_model=Token)
async def refresh(
    request: Request,
    response: Response,
    service: Annotated[AuthService, Depends()],
    uow: Annotated[UoW, Depends()],
):
    new_token = await service.refresh_token(
        request.cookies.get("refresh_token"), request.client.host, uow
    )
    response.set_cookie(
        "access_token",
        new_token.access_token,
        max_age=settings.auth_settings.ACCESS_TOKEN_EXPIRE_SECONDS,
        httponly=True,
    )
    response.set_cookie(
        "refresh_token",
        new_token.refresh_token,
        max_age=settings.auth_settings.REFRESH_TOKEN_EXPIRE_SECONDS,
        httponly=True,
    )
    return new_token


@router.post("/logout", response_model=dict)
async def logout(
    request: Request,
    response: Response,
    uow: Annotated[UoW, Depends()],
    service: Annotated[AuthService, Depends()],
):
    await service.logout(request.cookies.get("refresh_token"), uow)
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")
    return {"message": "Logged out successfully."}
