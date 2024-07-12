FROM python:3.9-slim-buster

WORKDIR  /app

COPY add_two_numbers.py .

CMD ["python", "add_two_numbers.py"]
