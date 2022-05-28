from microbit import *

class chuck:

    def __init__(self, offset_x,offset_y):
        self.addr = 0x52
        self.offset_x = offset_x
        self.offset_y = offset_y
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
        return data[0],data[1], data[2], data[3],data[4],butc==0,butz==0

    def centred_joystick(self):
        joyX, joyY, accX, accY, accZ, c, z = self.readall()
        return joyX-self.offset_x, joyY-self.offset_y

    def joystick_to_point(self):
        joyX, joyY = self.centred_joystick()
        if joyX<-50:
            x = 0
        elif joyX>=-50 and joyX<50:
            x = 1
        else:
            x = 2
        if joyY<-50:
            y = 2
        elif joyY>=-50 and joyY<50:
            y = 1
        else:
            y = 0
        return y*3 + x

# joystick
wii = chuck(120,131)
# images
pictures = [Image.ARROW_NW, Image.ARROW_N, Image.ARROW_NE, Image.ARROW_W,
            Image.HAPPY,Image.ARROW_E, Image.ARROW_SW, Image.ARROW_S, Image.ARROW_SE]
while True:
    display.show(pictures[wii.joystick_to_point()])
    sleep(200)
