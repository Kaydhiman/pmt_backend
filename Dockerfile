# Use the official Python image as the base image
FROM python:3.12.8-alpine3.20
# FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy only the necessary files
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the application port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app.main:app", "--reload", "--host=0.0.0.0", "--port=8000"]
