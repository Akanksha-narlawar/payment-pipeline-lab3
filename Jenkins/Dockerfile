FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV APP_VERSION=unknown
ENV GIT_COMMIT=unknown
ENV BUILD_NUMBER=unknown

EXPOSE 8080

CMD ["python", "app.py"]