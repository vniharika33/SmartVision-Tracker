print("Before import")

from ultralytics import YOLO

print("Import successful")

model = YOLO("yolov8n.pt")

print("Model loaded successfully")