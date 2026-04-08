from fastapi import APIRouter
from schemas.auth import LoginRequest
from views.auth import LoginResponse
from security import sign_jwt


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=LoginResponse)
async def login(data: LoginRequest):
    return sign_jwt(user_id=data.user_id)
