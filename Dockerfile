# Use the official Debian-based Python image
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "volunteering_app", "manage.py", "runserver"]
