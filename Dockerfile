FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY docker-http-redirect.py .

CMD ["python", "http-redirect.py"]
