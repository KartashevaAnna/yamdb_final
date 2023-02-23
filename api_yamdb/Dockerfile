FROM python:3.7-slim

WORKDIR /app

RUN apt update && \
    apt upgrade -y && \
    apt install -y libpq-dev
RUN pip3 install --upgrade pip
COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000
