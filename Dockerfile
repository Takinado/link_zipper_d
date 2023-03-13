FROM python:3.10.10-slim
WORKDIR /usr/src/app
COPY requirements.txt .
RUN python -m pip install --upgrade pip \
    && apt-get update \
    && apt-get install -y python3-dev default-libmysqlclient-dev build-essential
RUN pip install -r requirements.txt
ENTRYPOINT ["/bin/sh", "/usr/src/app/entrypoint.sh"]
COPY . .
