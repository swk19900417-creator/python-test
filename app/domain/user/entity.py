from dataclasses import dataclass
from typing import Optional

from app.domain.shared.vo import UserId
@dataclass
class User:
    """用户"""
    id: Optional[UserId]
    username: str
    password: str

    def __post_init__(self):
        if not self.username:
            raise ValueError('用户名不能为空')
        if not self.password:
            raise ValueError('密码不能为空')

    async def verify_password(self, password: str) -> bool:
        """验证密码"""
        return self.password == password

    async def update_password(self, password: str) -> None:
        """更新密码"""
        if not password:
            raise ValueError('密码不能为空')
        self.password = password