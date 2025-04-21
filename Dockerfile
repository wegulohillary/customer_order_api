# Dockerfile for Customer Order API

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . .

# Run migrations and start server
CMD ["gunicorn", "customer_order_api.wsgi:application", "--bind", "0.0.0.0:8000"]