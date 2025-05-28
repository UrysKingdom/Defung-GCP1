# Use the official Python image.
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy app code
COPY . .

# Expose port 8080
EXPOSE 8080

# Command to run the app
CMD ["python", "main.py"]