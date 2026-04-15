from fastapi import APIRouter, status, HTTPException
from fastapi.params import Depends
from pydantic import BaseModel

from app.application.common.exception import DomainException
from app.application.user.commands.register_user import RegisterUserCommand, RegisterUserHandler
from app.application.user.commands.login_user import LoginUserCommand, LoginUserHandler
from app.interface.dependency import get_register_user_handler, get_login_user_handler

auth_router = APIRouter(prefix="/auth", tags=["认证"])


class RegisterRequest(BaseModel):
    username: str
    password: str


class RegisterResponse(BaseModel):
    user_id: int
    username: str
    message: str

class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    user_id: int
    username: str
    message: str


@auth_router.post("/register", response_model=RegisterResponse, status_code=status.HTTP_201_CREATED)
async def register(request: RegisterRequest, handler: RegisterUserHandler = Depends(get_register_user_handler)):
    """注册用户"""
    try:
        command = RegisterUserCommand(username=request.username, password=request.password)
        result = await handler.handle(command)
        return RegisterResponse(user_id=result.user_id, username=result.username, message="注册成功")
    except DomainException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@auth_router.post("/login", response_model=LoginResponse, status_code=status.HTTP_200_OK)
async def login(request: LoginRequest, handler: LoginUserHandler = Depends(get_login_user_handler)):
    """登录用户"""
    try:
        command = LoginUserCommand(username=request.username, password=request.password)
        result = await handler.handle(command)
        return LoginResponse(user_id=result.user_id, username=result.username, message="登录成功")
    except DomainException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
