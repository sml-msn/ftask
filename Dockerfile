FROM python:3.10
EXPOSE 8502
WORKDIR /app
RUN pip install dvc
RUN pip install dvc-gdrive
COPY . .
RUN dvc pull -r mydisk --noauth_local_webserver