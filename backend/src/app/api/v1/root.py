from fastapi import APIRouter

from app.api.v1.auth import router as auth_router
from app.api.v1.well_day import router as well_day_router
from app.common.settings import settings

root_router = APIRouter(prefix=settings.app_settings.api_v1_prefix)
root_router.include_router(auth_router)
root_router.include_router(well_day_router)
