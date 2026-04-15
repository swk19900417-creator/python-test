from dataclasses import dataclass

from app.domain.user.entity import User
from app.domain.user.repository import IUserRepository


@dataclass
class RegisterUserCommand:
    """注册用户命令"""
    username: str
    password: str

@dataclass
class RegisterUserUseResult:
    """注册用户结果"""
    user_id: int
    username: str


class RegisterUserHandler:
    """注册用户处理器"""

    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    async def handle(self, command: RegisterUserCommand) -> RegisterUserUseResult:
        """处理注册用户命令"""
        if not command.username or not command.password:
            raise ValueError('用户名或密码不能为空')

        #用户名是否存在
        if await self.user_repository.exists_by_username(command.username):
            raise ValueError('用户名已存在')

        #创建用户模型
        user = User(id=None,username=command.username, password=command.password)

        save_user=await self.user_repository.save(user)

        return RegisterUserUseResult(user_id=save_user.id.value, username=save_user.username)