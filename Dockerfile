FROM python:3.11

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .

CMD guvicorn main:app --bind=0.0.0.0:8000
