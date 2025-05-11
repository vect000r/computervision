import cv2 as cv

# read the image
original = cv.imread('people.jpg')

# convert to grayscale
grayscale = cv.cvtColor(original, cv.COLOR_BGR2GRAY)

# load the haarcascade from OpenCV
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

detected_faces = face_cascade.detectMultiScale(grayscale, scaleFactor=1.1, minNeighbors=5)

# draw rectangles around the detected faces
for (column, row, width, height) in detected_faces:
    cv.rectangle(original, (column, row), (column + width, row + height), (0, 255, 0), 2)

# show the image with detected faces
cv.imshow('Detected Faces', original)
cv.waitKey(0)
cv.destroyAllWindows()

# save the image with detected faces
cv.imwrite('detected_faces.jpg', original)