FROM python:3.11-slim

EXPOSE 8000

WORKDIR /app

RUN apt-get update && \
    apt-get install -y gcc libffi-dev netcat-traditional && \
    rm -rf /var/lib/apt/lists/*

COPY ./app ./app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["uvicorn", "app.infra.api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
