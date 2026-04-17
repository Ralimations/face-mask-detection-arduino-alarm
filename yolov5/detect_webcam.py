import cv2
import torch
import serial
import time

# Initialize serial communication with Arduino
arduino = serial.Serial('COM5', 9600)  # Change 'COM3' to your Arduino port  # Change 'COM3' to your Arduino port
time.sleep(2)  # Wait for Arduino to reset

# Load the trained YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='runs/train/exp8/weights/best.pt', force_reload=True)

# Open the webcam
cap = cv2.VideoCapture(0)  # 0 is the default camera

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Perform detection
    results = model(frame)
    detections = results.pandas().xyxy[0]  # Get detections in pandas DataFrame

    # Check for mask detection
    mask_detected = any(detections['name'] == 'mask')  # Assuming 'mask' is the class name for wearing a mask

    # Send signal to Arduino
    if mask_detected:
        arduino.write(b'0')  # Send '0' for mask detected
    else:
        arduino.write(b'1')  # Send '1' for no mask detected

    # Render results on the frame
    frame = results.render()[0]

    # Display the resulting frame
    cv2.imshow('Webcam Detection', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()