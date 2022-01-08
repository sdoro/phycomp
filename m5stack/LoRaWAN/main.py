from cooperative_multitasking import Tasks
from machine import UART
from lora_states import NOT_JOINED, JOINING, JOINED, SENDING, SENT, RETRY
from asr6501 import ASR6501

tasks = Tasks()
uart2 = UART(2, tx=26, rx=32)
uart2.init(baudrate=115200, bits=8, parity=None, stop=1, txbuf=256, rxbuf=256)
modem = ASR6501(uart2, '70B3D57ED004AEC4', '0000000000000000', '1A02BBC6664AA1878BAC050A447ABEC6')  # DevEUI, AppEUI, AppKey as hex codes
count = 0

def modem_state_changed():
    return modem.has_state_changed()

def start_join():
    yellow()
    modem.send_join()
    tasks.when_then(modem_state_changed, end_join)
    
def end_join():
    state = modem.get_state()
    if state == JOINING:
        tasks.when_then(modem_state_changed, end_join)
    elif state == JOINED:
        green()
        tasks.after(10000, start_send)
    elif state == NOT_JOINED:
        tasks.after(60000, start_join)
    else:
        raise NotImplementedError()
    
def start_send():
    global count
    count += 1
    blue()
    modem.send_message(bytes(str(count), 'ASCII'), count % 29 == 1)  # message, confirmed
    tasks.when_then(modem_state_changed, end_send)

def end_send():
    state = modem.get_state()
    if state == SENDING:
        tasks.only_one_of(tasks.when_then(modem_state_changed, end_send), tasks.after(60000, assume_sent))  # workaround for AT+DTRX response lines
    elif state == SENT:
        magenta()
        tasks.after(300000, start_send)
    elif state == RETRY:
        red()
        tasks.after(300000, start_send)
    elif state == NOT_JOINED:
        red()
        tasks.after(300000, start_join)
    else:
        raise NotImplementedError()

def assume_sent():
    magenta()
    tasks.after(240000, start_send)


from machine import Pin
from neopixel import NeoPixel

gpio27 = Pin(27, Pin.OUT)
neopixels = NeoPixel(gpio27, 1)

def yellow():
    print("inizio yellow")
    neopixels[0] = (01, 01, 01)
    neopixels.write()
    print("fine yellow")

def green():
    neopixels[0] = (0, 25, 0)
    neopixels.write()

def blue():
    neopixels[0] = (0, 0, 25)
    neopixels.write()

def magenta():
    neopixels[0] = (20, 0, 20)
    neopixels.write()

def red():
    neopixels[0] = (25, 0, 0)
    neopixels.write()


tasks.now(start_join)

while tasks.available():
    tasks.run()
    
