FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install opencv-python numpy
CMD ["python", "main.py"]