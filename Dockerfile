﻿FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

ENV PYTHONPATH=/app/src

EXPOSE 8010

CMD ["uvicorn", "web_api.main:app", "--host", "0.0.0.0", "--port", "8010", "--app-dir", "src"]