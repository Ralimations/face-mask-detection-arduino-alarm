# BCA108 Final Project

BCA108 Final Project is a college project that combines computer vision and embedded-system behavior for real-time face mask detection using YOLOv5, webcam input, and Arduino-based hardware feedback.

## Overview

The project uses a custom YOLOv5 detection flow to classify whether a mask is detected in the webcam feed. Detection results are sent over serial communication to an Arduino, which then drives indicator outputs such as LEDs and a buzzer.

This project reflects a combination of software and hardware integration work aligned with an Embedded Systems academic track.

## Stack

- Python
- YOLOv5
- PyTorch
- OpenCV
- Arduino
- Serial communication

## Project Structure

- `yolov5/`: computer vision pipeline and detection code
- `yolov5/detect_webcam.py`: webcam-based detection script with Arduino signaling
- `sketch_dec18a/sketch_dec18a.ino`: Arduino logic for LEDs and buzzer output

## Requirements

- Python 3.10+
- Arduino-compatible board
- Webcam

Install dependencies:

```bash
pip install -r requirements.txt
```

## Notes

- The current detection script expects trained weights at `runs/train/exp8/weights/best.pt`.
- Training output and local virtual environments are intentionally excluded from this cleaned portfolio version.
- If you want to run the detection flow, you will need to provide the trained weights and update the serial port if needed.

## Academic Context

This project is being preserved as part of my student portfolio under Mindanao State University, Bachelor of Science in Computer Applications, major in Embedded Systems.
