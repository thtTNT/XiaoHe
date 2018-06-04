import facetrack
import buscom


def main():
    print("System is staring...")
    buscom.init()
    facetrack.init(buscom)
    print("System is ready!")


main()