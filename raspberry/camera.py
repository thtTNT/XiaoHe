from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import os
import threading


def start():
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        listener.fire("CameraCatchEvent", CameraCatchEvent(frame.array))
        rawCapture.seek(0)


class Camera:

    def __init__(self, sm):
        global listener
        listener = sm.listener
        global camera
        global rawCapture
        camera = PiCamera()
        camera.resolution = (320, 240)
        camera.framerate = 60
        camera.brightness = 70
        rawCapture = PiRGBArray(camera, size=(320, 240))
        rawCapture.seek(0)
        threading.Thread(target=start).start()


class CameraCatchEvent:
    frame = None

    def __init__(self, frame):
        self.frame = frame
