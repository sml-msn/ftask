FROM python:3.10
EXPOSE 8502
WORKDIR /app
RUN pip install dvc
COPY . .
RUN dvc pull -r mydisk 