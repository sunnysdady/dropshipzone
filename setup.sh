#!/usr/bin/env bash
apt-get update -y
apt-get install -y wget gnupg ca-certificates fonts-liberation libasound2 \
  libatk-bridge2.0-0 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 \
  libdrm2 libexpat1 libgbm1 libglib2.0-0 libgtk-3-0 libnspr4 libnss3 \
  libpango-1.0-0 libpangocairo-1-0 libstdc++6 libx11-6 libx11-xcb1 \
  libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 \
  libxrandr2 libxshmfence1 libxss1 libxtst6 lsb-release xdg-utils \
  libu2f-udev libvulkan1 libappindicator3-1 libasound2-data
wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -i google-chrome-stable_current_amd64.deb || apt-get -fy install
rm google-chrome-stable_current_amd64.deb
