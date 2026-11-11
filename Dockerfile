FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
# No instalamos chromium normal, usamos los binarios de playwright
RUN playwright install chromium

CMD ["python", "main.py"]