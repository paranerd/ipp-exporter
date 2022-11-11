FROM python:3.8-alpine
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["/usr/bin/uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
