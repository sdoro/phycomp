
import machine
import time
import dht

DHT = dht.DHT11(machine.Pin(13))  # Associate DHT11 with Pin(13).

while True:
    DHT.measure()                 # Start DHT11 to measure temperature and humidity data once.
    temp = DHT.temperature()
    hum = DHT.humidity()
    print('temperature:', temp, 'humidity:', hum)
    time.sleep_ms(2000)

# bot
