FROM python:3.9


WORKDIR /app

COPY requirements.txt ./
COPY app/ /app/app
COPY run.py /app/run.py

RUN pip install -r requirements.txt

CMD python run.py