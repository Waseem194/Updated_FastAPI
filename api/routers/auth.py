from fastapi import FastAPI,APIRouter

from models import Users
from schemas import UserRequest
from passlib.context import CryptContext

router = APIRouter()

bcrypt_context = CryptContext(schemes=['bcrypt'],deprecated='auto')

@router.post("/auth")
async def create_user(user_request:UserRequest):
    create_user_request = Users(
        first_name = user_request.first_name,
        last_name = user_request.last_name,
        email = user_request.email,
        hashed_password = user_request.password,
        role = user_request.role,
        is_active = True
    )
    return create_user_request