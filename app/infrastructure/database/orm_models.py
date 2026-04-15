from tortoise import fields
from tortoise.models import Model


class UserORM(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    password = fields.CharField(max_length=255)

    class Meta:
        table = 'users'