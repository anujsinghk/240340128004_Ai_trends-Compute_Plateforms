FROM python:3.9-slim-buster-alpine3.15

WORKDIR  /app

COPY add_two_numbers.py .

CMD ["python", "add_two_numbers.py"]
