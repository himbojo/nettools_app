# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application files to the container
COPY . /app

# Install necessary system tools (net-tools, dig)
RUN apt-get update && apt-get install -y \
    iputils-ping \
    dnsutils \
    traceroute \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your app runs on
EXPOSE 5000

# Set the entrypoint to run the Flask app
CMD ["python", "run.py"]