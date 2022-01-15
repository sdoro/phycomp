from machine import Pin
from ir_rx import NEC_16

ir_key = {
    0x40: 'POWER',
    0x5c: 'UP',
    0x5d: 'DOWN',
    0x41: 'END',
    0x58: 'RED',
    0x59: 'GREEN',
    0x45: 'BLUE',
    0x44: 'WHITE',
    
    0x0b: 'AUTO'
    }

def callback(data, addr, ctrl):
    if data > 0:  # NEC protocol sends repeat codes.
        #print('Data {:02x} Addr {:04x}'.format(data, addr))
        print(ir_key[data])

ir = NEC_16(Pin(23, Pin.IN), callback)