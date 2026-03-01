FROM python:3.10-slim

# Install required system packages
RUN apt update && apt install -y git && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /VJ-Forward-Bot

# Copy requirements first (better caching)
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .

# Run both services properly
CMD ["sh", "-c", "gunicorn app:app & python3 main.py"]