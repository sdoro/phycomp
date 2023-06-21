
import network
import time

import ujson
import urequests

import sys

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect("USER", "PASSWORD")
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
    return wlan
    
wifi = do_connect()
print('IP address: ', wifi.ifconfig()[0])


#text = '{"region":6,"province":"LE","town":"Lecce","fuelType":"2-1","priceOrder":"asc"}'
text = '{"points":[{"lat":40.3515155,"lng":18.1750161}],"fuelType":"2-1","priceOrder":"asc","radius":5}'

URL = 'https://carburanti.mise.gov.it/ospzApi/search/zone'
res = urequests.post(URL, headers = {'content-type': 'application/json'}, data = text)

jsonresults = ujson.loads(res.content)
print('Numero di record: ', len(jsonresults['results']))
print(jsonresults['results'][0])

wifi.disconnect()
print("Done")

# bot
