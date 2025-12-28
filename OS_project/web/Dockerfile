FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install flask pandas reportlab qrcode[pil]

CMD ["python3", "app.py"]