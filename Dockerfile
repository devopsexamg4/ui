FROM python:3.12.2-slim

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./UI /app
COPY ./.env.prod /app/.env

RUN --mount=type=secret,id=secret_1 \
    sed -i "s|SECRET_KEY=|SECRET_KEY=$(cat /run/secrets/secret_1)|" /app/.env
RUN --mount=type=secret,id=secret_2 \
    sed -i "s|DEBUG=|DEBUG=$(cat /run/secrets/secret_2)|" /app/.env
RUN --mount=type=secret,id=secret_3 \
    sed -i "s|ALLOWED_HOSTS=|ALLOWED_HOSTS=$(cat /run/secrets/secret_3)|" /app/.env
RUN --mount=type=secret,id=secret_4 \
    sed -i "s|SU_PASSWORD=|SU_PASSWORD=$(cat /run/secrets/secret_4)|" /app/.env
RUN --mount=type=secret,id=secret_5 \
    sed -i "s|SU_USER=|SU_USER=$(cat /run/secrets/secret_5)|" /app/.env
RUN --mount=type=secret,id=secret_6 \
    sed -i "s|SU_EMAIL=|SU_EMAIL=$(cat /run/secrets/secret_6)|" /app/.env


RUN mkdir -p /var/log/gunicorn/
RUN mkdir -p /var/run/gunicorn/

WORKDIR /app

RUN chmod +x ./entrypoint.sh
ENTRYPOINT [ "sh","./entrypoint.sh" ]
