from fastapi import APIRouter
from schemas import UserCreate

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register")
def register(user: UserCreate):
    return {
        "message": "User Registered Successfully",
        "username": user.username,
        "role": user.role
    }

@router.get("/")
def get_users():
    return {
        "message": "User List"
    }