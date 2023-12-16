# Pull base image
FROM python:3.10.12-slim-bullseye

# Set environment variables
ENV PYTHON_ENV PROD
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD exec gunicorn ffautomaton.wsgi:application --bind 0.0.0.0:8000 --workers 3
