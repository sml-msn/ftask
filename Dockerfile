FROM python:3.10
EXPOSE 8502
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
RUN mkdir datasets
CMD streamlit run app.py