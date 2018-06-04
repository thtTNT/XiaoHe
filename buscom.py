import wiringpi2 as wpi


def init():
    print("I2C is starting...")
    print("I2C is ready!")


def writeData(address, str):
    str = str + "*"
    bs = str.encode()
    bus = wpi.wiringPiI2CSetup(address)
    for byte in bs:
        wpi.wiringPiI2CWrite(bus, int(byte))
