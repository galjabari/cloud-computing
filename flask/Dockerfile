# Set the base image
FROM python:3.7-alpine
# Set the working directory in the container
WORKDIR /app
# Copy the dependencies file to the working directory
COPY requirements.txt .
# Install dependencies
RUN pip install -r requirements.txt
# Copy the content of the local src directory to the working directory
COPY src/ .
# Execute the Python program
CMD [ "python", "./server.py" ]
# Bind program to port 5000
EXPOSE 5000
