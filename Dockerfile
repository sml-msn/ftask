FROM python:3.10
EXPOSE 8502
WORKDIR /app
COPY . .
CMD dvc pull -r mydisk 