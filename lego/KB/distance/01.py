from spike import PrimeHub
from spike import DistanceSensor

hub = PrimeHub()                  # this is an object

# Distance Sensor
distance_sensor = DistanceSensor("B")

while True:
    print(distance_sensor.get_distance_cm())
    distance_sensor.wait_for_distance_closer_than(10, 'cm')
    hub.speaker.beep()
