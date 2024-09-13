# Use the official Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask via requirements.txt
RUN pip install -r requirements.txt

# Expose port 5000 for Flask
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
