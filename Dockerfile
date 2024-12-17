# 使用官方 Python 3.9 镜像作为基础镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 复制 requirements.txt 文件到容器中
COPY requirements.txt .

# 安装所需的 Python 包
RUN pip install --no-cache-dir -r requirements.txt

# 复制当前目录下的所有文件到容器的 /app 目录
COPY . .

# 暴露 FastAPI 默认端口
EXPOSE 8009

# 运行 FastAPI 应用
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8009", "--reload"]