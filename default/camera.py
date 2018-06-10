import cv2
import threading


def start():
    while True:
        ret, frame = cap.read()
        listener.fire("CameraCatchEvent", CameraCatchEvent(frame))


class Camera:

    def __init__(self, sm):
        global cap
        global listener
        listener = sm.listener
        cap = cv2.VideoCapture(0)
        threading.Thread(target=start).start()


class CameraCatchEvent:
    frame = None

    def __init__(self, frame):
        self.frame = frame
