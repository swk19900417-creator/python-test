# DDD FastAPI 项目 - AI 编程助手上下文

## 项目概述

这是一个基于 FastAPI 框架实现的领域驱动设计（DDD）示例项目。项目采用现代 Python 开发最佳实践，集成了配置管理、异步数据库支持等企业级特性。

## 技术栈

- **框架**: FastAPI (0.121.3+)
- **配置管理**: Pydantic Settings + python-dotenv
- **数据库**: MySQL (异步支持通过 asyncmy)
- **包管理**: UV (现代 Python 包管理器)
- **Python版本**: 3.13+

## 项目结构

```
DDD/
├── main.py                 # 应用入口点
├── pyproject.toml          # 项目配置和依赖管理
├── .env                    # 环境变量配置
├── config/
│   └── settings.py         # 应用配置类 (Pydantic Settings)
├── data/                   # 数据目录 (预留)
├── .spec-workflow/         # 规范工作流目录
└── .venv/                  # 虚拟环境
```

## 核心模块说明

### 配置管理 (`config/settings.py`)
- 使用 Pydantic 的 BaseSettings 进行类型安全的配置管理
- 支持从 `.env` 文件加载环境变量
- 包含应用基础配置和数据库连接配置
- 采用现代的 ConfigDict 配置方式

### 应用入口 (`main.py`)
- 当前为示例代码，包含基本的 Hello World 功能
- 预留为 FastAPI 应用的启动入口

## 开发规范

### 代码风格
- 使用 Python 3.13+ 现代语法特性
- 遵循 PEP 8 代码规范
- 使用类型注解增强代码可读性
- 中文注释便于团队理解

### 配置管理最佳实践
- 敏感信息通过环境变量管理
- 使用 Pydantic 进行配置验证
- 分离开发、测试、生产环境配置

### DDD 架构指导原则
- 领域层：业务逻辑和领域规则
- 应用层：业务流程编排
- 基础设施层：数据访问和外部服务集成
- 界面层：API 暴露和用户交互

## 常用命令

### 开发环境
```bash
# 激活虚拟环境
source .venv/bin/activate  # Linux/Mac
# 或
.venv\Scripts\activate     # Windows

# 安装依赖
uv sync

# 运行应用
python main.py
```

### 配置验证
```bash
# 测试配置加载
python config/settings.py
```

## 数据库配置

项目使用 MySQL 数据库，配置信息：
- 主机: 8.155.43.9:3306
- 数据库: sqlalchemy
- 编码: utf8mb4
- 驱动: asyncmy (异步)

## AI 编程助手使用指南

### 上下文理解
1. 这是一个 DDD 架构的学习/演示项目
2. 重点在于展示领域驱动设计的最佳实践
3. 使用现代 FastAPI 异步开发模式

### 开发重点
- 完善领域模型设计
- 实现仓储模式
- 添加应用服务层
- 集成数据库迁移工具
- 添加 API 路由和中间件

### 注意事项
- 保持 DDD 分层架构的清晰性
- 确保异步编程的正确使用
- 配置的环境隔离和安全性
- 代码的可测试性和可维护性

## 扩展建议

1. **领域层扩展**: 添加聚合根、实体、值对象
2. **应用服务**: 实现业务用例和流程编排
3. **数据访问**: 集成 SQLAlchemy 或 Tortoise ORM
4. **API 设计**: 完善路由设计和响应模型
5. **测试**: 添加单元测试和集成测试
6. **部署**: 添加 Docker 容器化配置
7. **文档**: 完善 API 文档和使用说明

## 版本信息

- Python: 3.13+
- 项目版本: 0.1.0
- 配置版本: 采用现代 Pydantic v2 配置方式