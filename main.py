import cv2
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

#how to create docker container for this project
#1. create a file named Dockerfile in the project directory
#2. add the following lines to the Dockerfile
#FROM python:3.8-slim
#WORKDIR /app
#COPY . /app
#RUN pip install opencv-python numpy
#CMD ["python", "main.py"]
#3. build the docker image using the command: docker build -t color-detection .
#4. run the docker container using the command: docker run -it --rm --name
# to exclude virtual environment files from the docker image, create a .dockerignore file
# and add the following lines to it:
#.venv
#__pycache__/
#for readme file
#to create a requirements.txt file, run the command: pip freeze > requirements.txt