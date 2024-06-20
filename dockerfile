FROM python:3.9-slim

WORKDIR /app

COPY /app.py .
COPY /requeriments.txt .

RUN pip install -r requeriments.txt

EXPOSE 5000

CMD ["python","app.py"]