from microbit import *

class chuck:

    def __init__(self):
        self.addr = 0x52
        i2c.write(self.addr, bytes([0x40,0x00]), repeat=False)
        sleep(1)

    def read(self):
        i2c.write(self.addr, b'\x00', repeat=False)
        sleep(1)
        buf = i2c.read(self.addr, 6, repeat=False)
        data = [(0x17 + (0x17 ^ buf[i])) for i in range(6)]
        return data

    def readall(self):
        data = self.read()
        butc = (data[5] & 0x02)
        butz = (data[5] & 0x01)
        # joyX, joyY, accX, accY, accZ, c, z
        return data[0],data[1], data[2], data[3], data[4], butc==0, butz==0


wii = chuck()
while True:
    joyX, joyY, accX, accY, accZ, c, z = wii.readall()
    print(joyX, joyY, accX, accY, accZ, c, z,sep='\t')
    sleep(50)
