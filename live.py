import cv2
from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor

model=YOLO("last.pt")

results= model.predict(source="lalulintas.mp4", show=True)

cv2.imshow("best", results)

cv2.destroyAllWindows()