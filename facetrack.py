import sys

import cv2
import os
import threading


def init(sm):
    print("Facetrack is starting...")
    global face_cascade
    global bc
    bc = sm.buscom
    """
    global bc
    global camera
    global rawCapture
    camera = PiCamera()
    camera.resolution = (320, 240)
    camera.framerate = 60
    camera.brightness = 70
    rawCapture = PiRGBArray(camera, size=(320, 240))
    rawCapture.seek(0)
    """
    print(sys.path[0] + '/lbpcascade_frontalface_improved.xml')
    face_cascade = cv2.CascadeClassifier(sys.path[0] + '/lbpcascade_frontalface_improved.xml')
    sm.listener.add_listener("CameraCatchEvent", track)
    print("Facetrack is ready!")


def track(event):
    frame = event.frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
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

