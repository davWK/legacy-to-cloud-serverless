# Use a minimal base image
FROM python:3.9.7-slim-buster AS base

# Create a non-root user
RUN useradd -m -s /bin/bash flaskuser
USER flaskuser

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Add the directory containing the flask command to the PATH
ENV PATH="/home/flaskuser/.local/bin:${PATH}"

# Use a multi-stage build to minimize the size of the image
FROM base AS final

# Copy the app code
COPY app.py .
COPY templates templates/
COPY static static/

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Run the app with Gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app