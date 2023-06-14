FROM python:3.10
EXPOSE 8502
WORKDIR /app
COPY . .
RUN dvc init
RUN dvc pull -r mydisk 