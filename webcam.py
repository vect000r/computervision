import cv2 as cv
import sys

# Load the cascade classifier
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

if face_cascade.empty():
    print("Error: Could not load the cascade classifier.")
    sys.exit()

# Start the webcam
video_capture = cv.VideoCapture(0)

if not video_capture.isOpened():
    print("Error: Could not open video.")
    sys.exit()

# capture frames from the webcam
while True:
    code, frame = video_capture.read()
    
    if not code:
        print("Error: Could not read frame.")
        break

    grayscale = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    detected_faces = face_cascade.detectMultiScale(grayscale, scaleFactor=1.1, minNeighbors=5)

    # draw rectangles around the detected faces
    for (column, row, width, height) in detected_faces:
        cv.rectangle(frame, (column, row), (column + width, row + height), (0, 255, 0), 2)

    cv.imshow('Webcam - Detected Faces', frame)

    # exit if 'q' is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
video_capture.release()
cv.destroyAllWindows()