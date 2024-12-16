# Use a lightweight Python image
FROM python:3.10-slim

# Install system dependencies required by Playwright and Fly
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    tar \
    git \
    build-essential \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libasound2 \
    libpangocairo-1.0-0 \
    libpangoft2-1.0-0 \
    libxkbcommon0 \
    libxfixes3 \
    libgbm1 \
    libdrm2 \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /workspace

# Add a non-root user for development
RUN useradd -ms /bin/bash vscode

# Switch back to vscode user
USER vscode

# Copy requirements.txt and install Python dependencies
COPY requirements.txt /workspace/requirements.txt
RUN pip install --no-cache-dir -r /workspace/requirements.txt

# Install Playwright browsers explicitly via Python
RUN python -m playwright install

# Expose default ports for web server
EXPOSE 5500 8080
