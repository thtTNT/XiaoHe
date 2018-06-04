import facetrack
import buscom
import camera


def main():
    print("System is staring...")
    sm = SystemManager()
    sm.buscom = buscom.Buscom()
    sm.camera = camera.Camera()
    for att in dir(getattr(sm.buscom, "writeData")):
        print(dir(getattr(getattr(sm.buscom, "writeData"),att)))
    print("fuck you")
    sm.listener = listener.Listener()
    facetrack.init(sm)
    print("System is ready!")


class SystemManager:
    def __init__(self):
        a = 1


main()
