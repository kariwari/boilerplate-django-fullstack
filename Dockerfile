# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /src

# Install dependencies
COPY requirements.txt /src/
RUN pip install -r requirements.txt

# Copy project
COPY . /src/

# Copy .env file
COPY .env /src/.env

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "django_project.wsgi:application"]