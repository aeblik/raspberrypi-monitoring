FROM python:3.8-slim

WORKDIR /app

COPY monitor.py .

RUN apt-get update && apt-get install -y gcc python3-dev
RUN pip install requests

CMD ["python", "monitor.py"]
