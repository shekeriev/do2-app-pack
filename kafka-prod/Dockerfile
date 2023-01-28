FROM python:3.11-slim-buster

COPY code/* /app/

WORKDIR /app

RUN pip3 install kafka-python

CMD ["python", "-u", "/app/app.py"]