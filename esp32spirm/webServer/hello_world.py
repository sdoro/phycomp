#!/usr/bin/env micropython

#################################################
import network

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect("USER", "PASSWORD")
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
    return wlan.ifconfig()[0]
    
ip = do_connect()
print('IP address: ', ip)
##################################################

import tinyweb

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
    await response.send('<html><body><h1>Hello, world! (<a href="/table">table</a>)</h1></html>\n')


# HTTP redirection
@app.route('/redirect')
async def redirect(request, response):
    log.info("richiesto: /redirect")
    # Start HTTP response with content-type text/html
    await response.redirect('/')


# Another one, more complicated page
@app.route('/table')
async def table(request, response):
    log.info("richiesto: /table")
    # Start HTTP response with content-type text/html
    await response.start_html()
    await response.send('<html><body><h1>Simple table</h1>'
                        '<table border=1 width=400>'
                        '<tr><td>Name</td><td>Some Value</td></tr>')
    for i in range(10):
        await response.send('<tr><td>Name{}</td><td>Value{}</td></tr>'.format(i, i))
    await response.send('</table>'
                        '</html>')


def run():
    app.run(host='0.0.0.0', port=8081)


if __name__ == '__main__':
    run()
    # To test your server:
    # - Terminal:
    #   $ curl http://localhost:8081
    #   or
    #   $ curl http://localhost:8081/table
    #
    # - Browser:
    #   http://localhost:8081
    #   http://localhost:8081/table
    #
    # - To test HTTP redirection:
    #   curl http://localhost:8081/redirect -v
