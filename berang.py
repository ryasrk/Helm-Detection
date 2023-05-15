import tkinter as tk
from tkinter import filedialog, Tk, Label
import cv2
import PIL
from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
from PIL import Image, ImageTk

model=YOLO("last.pt")

class VideoPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Helm Detections")

        # Create buttons
        self.browse_button = tk.Button(master, text="Browse", command=self.browse_file)
        self.camera_button = tk.Button(master, text="Camera", command=self.camera)
        self.play_button = tk.Button(master, text="Play", command=self.play_video)
        self.stop_button = tk.Button(master, text="Stop", command=self.stop_video)

        # Create video canvas
        self.canvas = tk.Canvas(master, width=640, height=480)

        # Add buttons and canvas to the grid
        self.browse_button.grid(row=0, column=0)
        self.play_button.grid(row=0, column=1)
        self.stop_button.grid(row=0, column=2)
        self.camera_button.grid(row=0, column=3)
        self.canvas.grid(row=1, column=0, columnspan=4)

        self.video_path = ""

    def browse_file(self):
        self.video_path = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("MP4 files", "*.mp4"), ("AVI files", "*.avi"), ("All files", "*.*")))


    def play_video(self):
        self.playing = True
        if self.video_path == "":
            return
        results= model.predict(source=self.video_path, show=True)
        image = results
        cv2.VideoCapture(self.video_path)

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Convert frame to tkinter compatible image
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = cv2.resize(image, (640, 480))
            image = Image.fromarray(image)
            photo = ImageTk.PhotoImage(image)

            # Update canvas
            self.canvas.create_image(0, 0, image=photo, anchor=tk.NW)
            self.canvas.image = photo

            # Wait for 25ms and exit if "q" is pressed
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Release the capture and destroy all windows
        cap.release()
        cv2.destroyAllWindows()
    def camera(self):

        results= model.predict(0)

        cv2.VideoCapture("last", results)
        cv2.destroyAllWindows()

    def stop_video(self):
        self.playing = False
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlayer(root)
    root.mainloop()