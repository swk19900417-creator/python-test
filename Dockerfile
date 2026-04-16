# ========================================
# 多阶段构建 - 优化镜像大小
# ========================================

# 阶段1: 构建依赖
FROM python:3.13-slim AS builder

# 安装 UV 包管理器
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# 设置工作目录
WORKDIR /app

# 复制依赖文件
COPY pyproject.toml uv.lock* ./

# 使用 UV 安装依赖到虚拟环境
RUN uv sync --frozen --no-dev --no-install-project

# ========================================
# 阶段2: 运行时镜像
# ========================================
FROM python:3.13-slim AS runtime

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

# 设置工作目录
WORKDIR /app

# 从构建阶段复制虚拟环境
COPY --from=builder /app/.venv /app/.venv

# 复制应用代码
COPY . .

# 暴露端口 (Railway 会自动注入 PORT 环境变量)
EXPOSE 8000

# 启动命令 - 使用 Railway 注入的 PORT 环境变量
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]
