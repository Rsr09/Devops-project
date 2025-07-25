# Use the official Python image from Docker Hub
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy local code to the container
COPY . .

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose port 80 to the outside world
EXPOSE 80

# Run the application
CMD ["python", "app.py"]
