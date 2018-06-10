import platform


def init_listener():
    print("Listener is starting...")
    import listener
    sm.listener = listener.Listener()
    print("Listener is ready!")


def init_buscom():
    if sn.find("Linux") != -1:
        print("I2C is starting...")
        import buscom
        sm.buscom = buscom.Buscom()
        print("I2C is ready!")
        return
    print("I2C has been skipped")


def init_camera():
    if sn.find("Linux") != -1:
        print("Camera is starting...")
        from raspberry import camera
        sm.camera = camera.Camera(sm)
        print("Camera is ready!")
        return
    print("Camera is starting...")
    from default import camera
    sm.camera = camera.Camera(sm)
    print("Camera is ready!")


def init_server():
    print("Server is starting...")
    import server
    sm.server = server.Server(sm)
    print("Server is ready!")


def init_facetrack():
    print("Facetrack is staring...")
    import facetrack
    sm.facetrack = facetrack.Facetrack(sm)
    print("Facetrack is ready!")


def main():
    print("System is staring...")
    global sn
    global sm
    sm = SystemManager()
    sn = platform.platform()
    print("detect system name:" + sn)
    init_listener()
    init_buscom()
    init_camera()
    init_server()
    init_facetrack()
    print("System is ready!")


class SystemManager:
    def __init__(self):
        a = 1


main()
