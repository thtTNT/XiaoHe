import cv2
import listener


class Camera:

    def __init__(self):
        print("camera is staring...")
        global cap
        cap = cv2.VideoCapture(0)
        print("camera is ready!")

    def start():
        while True:
            ret, frame = cap.read()
        listener
        cap.release()


class CameraCatchEvent:

    def __init__(self, frame):
        self.frame = frame
