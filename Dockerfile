# Use a minimal base image with Python
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY . .

# Set environment variables (optional but nice)
ENV FLASK_APP=app
ENV FLASK_ENV=development

# Expose the port Flask will run on
EXPOSE 5000

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]

