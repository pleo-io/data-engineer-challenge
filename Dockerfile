FROM python:3

WORKDIR /app

COPY ./src/requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY ./src /app

ENTRYPOINT ["python", "main.py"]
