'''
应用配置管理
'''
import os
from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):
    '''应用配置类 - 所有配置项可通过环境变量覆盖'''
    app_name: str = 'FastAPI DDD'
    app_version: str = '0.1.0'
    debug: bool = False  # 生产环境默认关闭
    secret_key: str = 'change-me-in-production'

    # 数据库配置 - PostgreSQL (Railway 会自动设置 DATABASE_URL)
    db_url: str = 'postgres://localhost:5432/fastapi_db'
    # 兼容 Railway 的 DATABASE_URL 环境变量
    database_url: str | None = None

    @property
    def get_db_url(self) -> str:
        """优先使用 DATABASE_URL (Railway 自动设置)"""
        return self.database_url or self.db_url

    # 使用 ConfigDict 替代 class Config
    # 使用绝对路径确保无论从哪个目录运行都能正确找到 .env 文件
    model_config = ConfigDict(
        env_file=Path(__file__).parent.parent / '.env',  # 从config/settings.py定位到根目录的.env
        env_file_encoding='utf-8',
        case_sensitive=False  # 环境变量通常不区分大小写
    )

settings = Settings()

if __name__ == '__main__':
    import sys
    print(f"app_name: {repr(settings.app_name)}")
    print(f"app_version: {settings.app_version}")
    print(f"debug: {settings.debug}")
    print(f"secret_key: {settings.secret_key}")
    print(f"db_url: {settings.db_url}")

    # 验证是否从 .env 文件加载
    print(f"\n配置验证:")
    print(f"app_name 来自 .env: {settings.app_name == '侯林帅测试DDD'}")
    print(f"app_name 是默认值: {settings.app_name == 'FastAPI  DDD'}")
