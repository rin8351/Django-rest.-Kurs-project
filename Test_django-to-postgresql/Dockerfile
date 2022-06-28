FROM python:latest
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY ./requirements.txt .
ADD post ./
RUN pip install -r requirements.txt