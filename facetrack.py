from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import os
import threading


def init(buscom):
    print("Facetrack is starting...")
    global bc
    global camera
    global rawCapture
    global face_cascade
    bc = buscom
    camera = PiCamera()
    camera.resolution = (320, 240)
    camera.framerate = 60
    camera.brightness = 70
    rawCapture = PiRGBArray(camera, size=(320, 240))
    rawCapture.seek(0)
    face_cascade = cv2.CascadeClassifier('/home/pi/develop/opencv-3.4.1/data/lbpcascades/lbpcascade_frontalface.xml')
    threading.Thread(target=track).start()
    print("Facetrack is ready!")


def track():
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray)
        max_w = 0
        max_h = 0
        max_x = 0
        max_y = 0
        size = 0
        for (x, y, w, h) in faces:
            if w * h > max_w * max_h:
                max_w = w
                max_h = h
                max_x = x
                max_y = y
            size = size + 1
            if size > 0:
                bc.writeData(0x04,
                             "001|" + str(size) + "|" + str(max_x) + "|" + str(max_y) + "|" + str(max_w) + "|" + str(
                                 max_h))
        rawCapture.seek(0)
