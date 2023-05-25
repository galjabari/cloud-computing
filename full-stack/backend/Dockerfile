# Use a lightweight python as the base image
FROM python:3.9-alpine
WORKDIR /app
COPY requirements.txt .
COPY src/ .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "server.py"]