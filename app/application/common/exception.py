'''
通用业务异常
'''


class DomainException(Exception):
    '''
    业务异常
    '''

    def __init__(self, message: str, code: int):
        self.message = message
        self.code = code
        super().__init__(message)


class AuthException(DomainException):
    '''
    认证异常
    '''

    def __init__(self, message="认证异常！"):
        super().__init__(message, 401)


class DuplicateException(DomainException):
    '''
    重复异常
    '''

    def __init__(self, message="重复异常！"):
        super().__init__(message, 409)


class NotFoundException(DomainException):
    '''
    未找到异常
    '''

    def __init__(self, message="未找到异常！"):
        super().__init__(message, 404)

class validationException(DomainException):
    '''
    验证异常
    '''

    def __init__(self, message="验证异常！"):
        super().__init__(message, 422)