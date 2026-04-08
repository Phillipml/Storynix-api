from fastapi import APIRouter

from src.schemas.auth import LoginRequest
from src.security import sign_jwt
from src.views.auth import LoginResponse


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=LoginResponse)
async def login(data: LoginRequest):
    return sign_jwt(user_id=data.user_id)
