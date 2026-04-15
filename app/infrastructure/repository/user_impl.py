from typing import Optional

from app.domain.shared.vo import UserId
from app.domain.user.entity import User
from app.domain.user.repository import IUserRepository
from app.infrastructure.database.mappers import UserMapper
from app.infrastructure.database.orm_models import UserORM

class UserRepositoryImpl(IUserRepository):
    '''用户仓储的实现类'''

    async def save(self, user: User) -> User:
        orm_model = UserMapper.to_orm(user)
        await orm_model.save()
        return UserMapper.to_entity(orm_model)


    async def get_by_id(self, user_id: UserId) -> Optional[User]:
        orm_model = await UserORM.get_or_none(id=user_id.value)
        if orm_model:
            return UserMapper.to_entity(orm_model)
        return None


    async def get_by_username(self, username: str) -> Optional[User]:
        orm_model = await UserORM.get_or_none(username=username)
        if orm_model:
            return UserMapper.to_entity(orm_model)
        return None


    async def exists_by_username(self, username: str) -> bool:
        return await UserORM.filter(username=username).exists()


    async def delete(self, user_id: UserId) -> bool:
        orm_model = await UserORM.get_or_none(id=user_id.value)
        if orm_model:
            await orm_model.delete()
            return True
        return False


    async def select_all(self) -> list[User]:
        orm_models = await UserORM.all()
        return [UserMapper.to_entity(orm_model) for orm_model in orm_models]
