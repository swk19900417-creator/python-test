'''
用户仓储的接口(抽象类)
'''

from abc import ABC, abstractmethod
from typing import Optional

from app.domain.shared.vo import UserId
from app.domain.user.entity import User


class IUserRepository(ABC):

    @abstractmethod
    async def save(self, user: User) -> User:
        """保存用户"""
        pass

    @abstractmethod
    async def get_by_id(self, user_id: UserId) -> Optional[User]:
        """通过ID获取用户"""
        pass

    @abstractmethod
    async def get_by_username(self, username: str) -> Optional[User]:
        """通过用户名获取用户"""
        pass

    @abstractmethod
    async def exists_by_username(self, username: str) -> bool:
        """判断用户名是否存在"""
        pass

    @abstractmethod
    async def delete(self, user_id: UserId) -> bool:
        """删除用户"""
        pass

    @abstractmethod
    async def select_all(self) -> list[User]:
        """查询所有用户"""
        pass