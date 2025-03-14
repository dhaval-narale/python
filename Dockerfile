FROM python:3.9

WORKDIR /app

COPY Coffee_Machine.py /app/

CMD ["python", "Coffee_Machine.py"]
