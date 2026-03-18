FROM python:3.10-slim

# Prevent python from buffering and creating pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# System dependencies: Sirf Audio aur FFMPEG par focus
RUN apt-get update && apt-get install -y \
    ffmpeg \
    pulseaudio \
    libasound2 \
    alsa-utils \
    libpulse-dev \
    libffi-dev \
    libssl-dev \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy your bot file (Jo single file maine di thi)
COPY . .

# Install Python requirements
# Make sure requirements.txt has: pyrogram, pytgcalls[tgcalls], TgCrypto
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Create pulse directory for root access fix
RUN mkdir -p /var/run/pulse /home/pulse && \
    chmod -R 777 /var/run/pulse /home/pulse

# --- THE MAGIC CMD ---
# 1. PulseAudio ko system mode mein start karega (Root fix)
# 2. Virtual Sink banayega (Fake Mic) taaki 'pulse' input kaam kare
# 3. Bot file run karega
CMD pulseaudio --start --system --realtime=no && \
    pactl load-module module-null-sink sink_name=Virtual_Sink && \
    python main.py
