FROM python:3.6.9

# 환경 변수 설정
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Avoiding user interaction with tzdata
ENV DEBIAN_FRONTEND=noninteractive

#dependencies를 위한 apt-get update
RUN apt-get update && apt-get -y install \
    libpq-dev --no-install-recommends apt-utils

COPY . .

WORKDIR /code/backend/

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt