FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# 1. Install Node.js + Audio Libs + FFMPEG
RUN apt-get update && apt-get install -y \
    curl \
    ffmpeg \
    pulseaudio \
    libasound2 \
    libpulse-dev \
    build-essential \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# 2. Copy Code & Install Python Dependencies
COPY . .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 3. PulseAudio Root Permissions Setup
RUN mkdir -p /var/run/pulse /var/lib/pulse && \
    chmod -R 777 /var/run/pulse /var/lib/pulse

# 4. Final CMD (Added --system for Root and Node fix)
# Hum PulseAudio ko system mode mein chalayenge taaki root error na aaye
CMD pulseaudio --start --system --realtime=no --disallow-exit && \
    python main.py
