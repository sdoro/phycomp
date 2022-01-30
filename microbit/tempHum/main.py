def on_forever():
    dht11_dht22.query_data(DHTtype.DHT11, DigitalPin.P0, True, False, True)
    basic.show_string("T:")
    basic.show_number(dht11_dht22.read_data(dataType.TEMPERATURE))
    basic.show_string("U:")
    basic.show_number(dht11_dht22.read_data(dataType.HUMIDITY))
basic.forever(on_forever)
