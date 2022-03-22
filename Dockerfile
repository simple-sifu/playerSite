# Pull base image
FROM python:3.9.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /code

# Copy project
COPY . /code/

# Install dependencies
RUN pip install -r requirements.txt
