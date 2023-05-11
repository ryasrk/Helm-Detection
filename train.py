from ultralytics import YOLO
from ultralytics.yolo.engine.model import YOLO

# Load a model
model = YOLO("yolov8n.yaml") # build a new model from scratch

# Use the model
results = model.train(data="data.yaml", epochs=20, batch=8, imgsz=640, name='train', device='')