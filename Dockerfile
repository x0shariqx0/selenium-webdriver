FROM python:3.10-slim

WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget unzip curl ca-certificates \
    fonts-liberation libnss3 libatk-bridge2.0-0 libxss1 \
    libasound2 libgbm1 libgtk-3-0 libx11-xcb1 \
    && rm -rf /var/lib/apt/lists/*

# Install Chrome for Testing (fixed version)
RUN wget https://storage.googleapis.com/chrome-for-testing-public/142.0.7444.162/linux64/chrome-linux64.zip \
    && unzip chrome-linux64.zip \
    && mv chrome-linux64 /opt/chrome \
    && ln -s /opt/chrome/chrome /usr/bin/google-chrome \
    && rm chrome-linux64.zip

# Install matching ChromeDriver (same version)
RUN wget https://storage.googleapis.com/chrome-for-testing-public/142.0.7444.162/linux64/chromedriver-linux64.zip \
    && unzip chromedriver-linux64.zip \
    && mv chromedriver-linux64/chromedriver /usr/bin/chromedriver \
    && chmod +x /usr/bin/chromedriver \
    && rm -rf chromedriver-linux64 chromedriver-linux64.zip

# Install Selenium
RUN pip install --no-cache-dir selenium

# Copy files
COPY firsttest.py .
COPY index.html .

# Run test
CMD ["python", "firsttest.py"]
