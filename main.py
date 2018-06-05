import facetrack
import buscom
import camera
import listener


def main():
    print("System is staring...")
    sm = SystemManager()
    sm.listener = listener.Listener()
    sm.buscom = buscom.Buscom()
    sm.camera = camera.Camera(sm)
    facetrack.init(sm)
    print("System is ready!")


class SystemManager:
    def __init__(self):
        a = 1


main()
