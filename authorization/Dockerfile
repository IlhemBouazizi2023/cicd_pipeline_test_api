# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install the required libraries
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python code file to the working directory
COPY authorization.py .

# Run the test commands
COPY entrypoint.sh /usr/local/bin/entrypoint1.sh
RUN chmod +x /usr/local/bin/entrypoint1.sh
CMD /usr/local/bin/entrypoint1.sh

