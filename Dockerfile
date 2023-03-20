FROM python:3.10.10-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1 #запрещает Python записывать файлы pyc на диск
ENV PYTHONUNBUFFERED 1 #запрещает Python буферизовать stdout и stderr
COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    apt update && \
    apt install python3-dev default-libmysqlclient-dev build-essential -y && \
    rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.txt
ENTRYPOINT ["/app/wait-for-it.sh", "db:3306", "-s" , "-t", "60", "--", "/bin/bash", "/app/entrypoint.sh"]
COPY . .
