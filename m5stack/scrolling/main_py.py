import uos
from cooperative_multitasking import Tasks
from network import WLAN, AP_IF
from mqtt_client import MQTTClient
from machine import Pin
from neopixel import NeoPixel
from font5 import Font5
from neopixel_scroller import NeopixelScroller

tasks = Tasks()

ap = WLAN(AP_IF)
ap.active(False)
ap = None

client = MQTTClient(tasks,
                    hostname = 'broker.mqttdashboard.com',
                    client_id = '',
                    user_name = '...',
                    password = '')
client.activate_wlan([('...', '...')])
client.start()

gpio27 = Pin(27, Pin.OUT)
neopixels = NeoPixel(gpio27, 25)
font = Font5()
colors = [(20, 0, 0), (20, 20, 0), (0, 20, 0), (0, 0, 20)]
scroller = None

def randint(low, high):
    s = 0
    bs = uos.urandom(4)
    for b in bs:
        s = (s << 8) | b
    return low + (s % (high - low + 1))

def random_color():
    return colors[randint(0, len(colors) - 1)]

def receive_message(topic, payload_object):
    global scroller
    try:
        message = payload_object['message']
        color = random_color()
        scroller = NeopixelScroller(neopixels, message, font, foreground_color=color)
    except:
        pass

client.subscribe('...', receive_message)

def has_message():
    return scroller is not None

def await_message():
    tasks.when_then(has_message, scroll_message)

def is_connected():
    return client.is_connected()

def scroll_message():
    scroller.scroll()
    neopixels.write()
    if is_connected():
        tasks.after(300, scroll_message)
    else:
        tasks.now(clear_display)

def clear_display():
    global scroller
    scroller = None
    for pixel_index in range(25):
        neopixels[pixel_index] = (0, 0, 0)
    neopixels.write()
    tasks.now(await_message)

tasks.now(await_message)

while tasks.available():
    tasks.run()