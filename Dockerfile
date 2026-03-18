FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Sirf FFMPEG aur basic audio libs
RUN apt-get update && apt-get install -y \
    ffmpeg \
    pulseaudio \
    libasound2 \
    libpulse-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Cloud platforms par PulseAudio ko bina root-check ke chalane ka setup
CMD pulseaudio -D --exit-idle-time=-1 --disallow-exit --raw --no-cpu-limit && \
    python main.py
