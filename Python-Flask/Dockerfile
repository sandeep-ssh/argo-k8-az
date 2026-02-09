# Force native ARM64 to avoid x64 emulation on Apple Silicon
FROM --platform=linux/arm64 python:3.9-slim

# Prevent Python from buffering logs (useful in Docker)
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Install dependencies first to leverage Docker layer caching
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/app.py .

EXPOSE 5000

CMD ["python", "app.py"]
