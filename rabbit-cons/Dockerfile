FROM python:3.11-slim-buster

COPY code/* /app/

WORKDIR /app

RUN pip3 install pika

CMD ["python", "-u", "/app/app.py"]