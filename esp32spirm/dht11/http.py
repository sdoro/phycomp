#!/usr/bin/env micropython

#################################################
import network

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        #wlan.connect("USER", "PASSWORD")
        wlan.connect("TISCALI_4299", "7mrgluqqmu")
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
    return wlan.ifconfig()[0]
    
ip = do_connect()
print('IP address: ', ip)
##################################################

import machine
import time
import dht

import tinyweb

DHT = dht.DHT11(machine.Pin(13))  # Associate DHT11 with Pin(13).

# Create web server application
app = tinyweb.webserver()

import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("server web")

# Index page
@app.route('/')
async def index(request, response):
    log.info("richiesto: /")
    # Start HTTP response with content-type text/html
    await response.start_html()
    # Send actual HTML page
    await response.send('<html><body><h1>Ciao Micropython! (<a href="/misurazioni">misurazioni</a>)</h1></html>\n')


# Application page
@app.route('/misurazioni')
async def misurazioni(request, response):
    log.info("richiesto: /misurazioni")
    # Start HTTP response with content-type text/html
    await response.start_html()
    await response.send('<html><meta charset="utf-8" /><body><h1>Misurazione con DHT11 su ESP32 e server http</h1>')
    DHT.measure()
    await response.send('<p>Temperatura: {} e umidità: {}</p>'.format(DHT.temperature(), DHT.humidity()))
    await response.send('</html>')
    log.info("Temperatura: " + str(DHT.temperature()) + " Umidità: " + str(DHT.humidity()))


def run():
    app.run(host='0.0.0.0', port=8081)


if __name__ == '__main__':
    run()
    # To test your server:
    # - Terminal:
    #   $ curl http://ESPip:8081
    #   or
    #   $ curl http://ESPip:8081/misurazioni
    #
    # - Browser:
    #   http://ESPip:8081
    #   http://ESPip:8081/misurazioni
    #
