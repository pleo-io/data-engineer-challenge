FROM python:3

WORKDIR /app

COPY ./src/requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY ./src /app

COPY wait-for-it.sh /app/wait-for-it.sh
