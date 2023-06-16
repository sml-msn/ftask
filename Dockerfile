FROM python:3.10
EXPOSE 8502
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
RUN dvc pull -r mydisk
CMD streamlit run app.py