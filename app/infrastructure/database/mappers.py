'''
实体与ORM映射
'''
from app.domain.shared.vo import UserId
from app.domain.user.entity import User
from app.infrastructure.database.orm_models import UserORM


class UserMapper:
    '''用户映射器'''

    @staticmethod
    def to_entity(orm_model:UserORM) -> User:
        '''将ORM对象转换为实体对象'''
        return User(
            id=UserId(orm_model.id) if orm_model.id else None,
            username=orm_model.username,
            password=orm_model.password
        )

    @staticmethod
    def to_orm(entity: User) -> UserORM:
        '''将实体对象转换为ORM对象'''
        orm_model=UserORM()
        if entity.id:
            orm_model.id=entity.id.value
        orm_model.username=entity.username
        orm_model.password=entity.password
        return orm_model
