'''用户登录弄块'''
from dataclasses import dataclass

from app.domain.user.repository import IUserRepository


@dataclass
class LoginUserCommand:
    """用户登录命令"""
    username: str
    password: str

@dataclass
class LoginUserResult:
    """用户登录结果"""
    user_id: int
    username: str


class LoginUserHandler:
    """用户登录处理器"""
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    async def handle(self, command: LoginUserCommand) -> LoginUserResult:
        """处理用户登录命令"""
        if not command.username or not command.password:
            raise ValueError('用户名或密码不能为空')

        # 通过用户名查询用户
        user = await self.user_repository.get_by_username(command.username)

        if not user:
            raise ValueError('用户名或者密码错误')
        if not await user.verify_password(command.password):
            raise ValueError('用户名或者密码错误')
        return LoginUserResult(user_id=user.id.value, username=user.username)