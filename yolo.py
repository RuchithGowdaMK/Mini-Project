from ultralytics import YOLO
model = YOLO("yolo11s.pt")   # auto-downloads pretrained weights
results = model("empty.jpg")
results[0].show()