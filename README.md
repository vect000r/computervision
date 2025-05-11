# Face Detection System

A simple Python application that detects faces using OpenCV, both in static images and through webcam feed.

## Project Files

- `single.py`: Detects faces in a static image ('people.jpg')
- `webcam.py`: Detects faces in real-time using your webcam
- `people.jpg`: Sample input image
- `detected_faces.jpg`: Output image with detected faces

## Requirements

- Python 3.x
- OpenCV (`cv2`)

## Installation

1. Install OpenCV:
   ```
   pip install opencv-python
   ```

2. Clone or download this repository

## Usage

### Static Image Face Detection

Run the `single.py` script to detect faces in a static image:

```
python single.py
```

This will:
- Load the image 'people.jpg'
- Detect faces using Haar Cascade classifier
- Display the result with green rectangles around detected faces
- Save the result as 'detected_faces.jpg'

### Webcam Face Detection

Run the `webcam.py` script to detect faces in real-time using your webcam:

```
python webcam.py
```

- Green rectangles will highlight detected faces
- Press 'q' to quit the application

## How It Works

The application uses OpenCV's Haar Cascade classifier to detect faces. The process involves:

1. Converting images to grayscale for processing
2. Applying the pre-trained face detection model
3. Drawing rectangles around detected face regions

## Customizing

To use a different image, replace 'people.jpg' with your image file, or modify the filename in `single.py`.

## Troubleshooting

- If the webcam doesn't start, ensure your camera is connected and not in use by another application
- If face detection isn't working well, try adjusting the parameters in the `detectMultiScale()` function:
  - `scaleFactor`: Controls the image size reduction at each scale
  - `minNeighbors`: Higher values result in fewer detections but with higher quality
