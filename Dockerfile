# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy application files into the container
COPY requirements.txt .  
COPY app.py .            

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 80 for the Flask app
EXPOSE 80

# Define the command to run the application
CMD ["python", "app.py"]

# Add a comment in Dockerfile
# Updated Flask application for ECS deployment
