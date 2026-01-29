# Use the official Debian-based Python image
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./volunteering_app .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
