FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# ensure that any dependent models are downloaded at build-time
RUN python app.py download-files

# Run the application.
ENTRYPOINT ["python", "app.py"]
CMD ["start"]
