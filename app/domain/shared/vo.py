'''
共享值对象
'''
from dataclasses import dataclass

@dataclass(frozen=True)   #dataclass会日动实现_init()和eq()方法 frozen=True使实例不可变
class UserId:
    """用户ID"""
    value: int

    def __post_init__(self):
        if not isinstance(self.value, int):
            raise TypeError('用户ID必须是整数')
