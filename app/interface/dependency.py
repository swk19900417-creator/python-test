'''
依赖注入模块
'''
from fastapi import Depends

from app.application.user.commands.login_user import LoginUserHandler
from app.application.user.commands.register_user import RegisterUserHandler
from app.application.user.queries.get_orders import GetOrdersHandler
from app.domain.user.repository import IUserRepository
from app.infrastructure.repository.user_impl import UserRepositoryImpl


def get_user_repository() -> IUserRepository:
    return UserRepositoryImpl()

def get_register_user_handler(user_repository: IUserRepository = Depends(get_user_repository)) -> RegisterUserHandler:
    return RegisterUserHandler(user_repository)

def get_login_user_handler(user_repository: IUserRepository = Depends(get_user_repository)) -> LoginUserHandler:
    return LoginUserHandler(user_repository)

def get_orders_handler() -> GetOrdersHandler:
    return GetOrdersHandler()