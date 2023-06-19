
import network
import time
from umqtt.robust import MQTTClient

from random import randint

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect("TISCALI_4299", "7mrgluqqmu")
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
    return wlan.ifconfig()[0]
    
ip = do_connect()
print('IP address: ', ip)

CHANNEL_ID = "2193739"
WRITE_API_KEY = "M3S9HKDXE7X0E9TP"
THINGSPEAK_MQTT_CLIENT_ID = b"OycBFBE4IQwoEQkqICIfNQo"
THINGSPEAK_MQTT_USERNAME = b"OycBFBE4IQwoEQkqICIfNQo"
THINGSPEAK_MQTT_PASSWORD = b"37jLzZKYWQ5KSOplvYMCJXDL"
THINGSPEAK_CHANNEL_ID = b'2193739'

client = MQTTClient(server=b"mqtt3.thingspeak.com",
                    client_id=THINGSPEAK_MQTT_CLIENT_ID, 
                    user=THINGSPEAK_MQTT_USERNAME, 
                    password=THINGSPEAK_MQTT_PASSWORD, 
                    ssl=False)

print('connecting to thingspeak ...')
try:
    client.connect()
except Exception as e:
    print('could not connect to MQTT server {}{}'.format(type(e).__name__, e))
    sys.exit()

credentials = bytes("channels/{:s}/publish".format(THINGSPEAK_CHANNEL_ID), 'utf-8')  
# continually publish two fields to a Thingspeak channel using MQTT
PUBLISH_PERIOD_IN_SEC = 20
while True:
    try:
        f1 = randint(40, 80)
        f2 = randint(81, 120)
        payload = "field1=" + str(f1) + "&field2=" + str(f2)
        print('sending to thingspeak ...')
        client.publish(credentials, payload)
        time.sleep(PUBLISH_PERIOD_IN_SEC)
    except  KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        print('disconnecting from thingspeak ...')
        client.disconnect()
        break

print("Done")

# bot
