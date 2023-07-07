# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# System deps:
RUN apt-get update && apt-get install -y --no-install-recommends \
        gcc \
        curl

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Expose port
EXPOSE 8080

# Command to run the app locally
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

# Command to run on Google Cloud
CMD uvicorn main:app --host 0.0.0.0 --port $PORT
