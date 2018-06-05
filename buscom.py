import wiringpi2 as wpi


class Buscom:
    def __init__(self):
        print("I2C is starting...")
        print("I2C is ready!")
        global add_dict
        add_dict = {}

    def writeData(self, address, str):
        str = str + "*"
        bs = str.encode()
        if add_dict[address] is not None:
            bus = add_dict[address]
        else:
            bus = wpi.wiringPiI2CSetup(address)
            add_dict[address] = bus
        for byte in bs:
            wpi.wiringPiI2CWrite(bus, int(byte))
