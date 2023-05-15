import cv2
from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import tkinter as tk
import tkinter.filedialog
import os
from tkinter.filedialog import askopenfilename

root = tkinter.Tk()
root.withdraw()

currdir = os.getcwd()
tempdir = tkinter.filedialog.askopenfilename(parent=root, initialdir=currdir, title='Please select a directory')

model=YOLO("last.pt")

results= model.predict(source=tempdir, show=True)

cv2.imshow("last", results)

cv2.destroyAllWindows()