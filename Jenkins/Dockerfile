FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ARG APP_VERSION=unknown
ARG GIT_COMMIT=unknown
ARG BUILD_NUMBER=unknown
ARG BRANCH_NAME=unknown

ENV APP_VERSION=$APP_VERSION
ENV GIT_COMMIT=$GIT_COMMIT
ENV BUILD_NUMBER=$BUILD_NUMBER
ENV BRANCH_NAME=$BRANCH_NAME

EXPOSE 8080

CMD ["python", "app.py"]