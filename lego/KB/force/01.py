from spike import PrimeHub
from spike import ForceSensor

hub = PrimeHub()                  # this is an object

# Force sensor

force_sensor=ForceSensor('C')

while True:
    force_sensor.wait_until_pressed()
    #hub.speaker.beep()
