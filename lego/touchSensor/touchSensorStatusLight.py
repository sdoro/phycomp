from spike import ForceSensor
from spike.control import Timer

from spike import PrimeHub

from spike.control import wait_for_seconds

# Initialize the Force Sensor
force = ForceSensor('B')


timer = Timer()

hub = PrimeHub()

spento = True

while True:
    if force.is_pressed():
        print('Newton: ', force.get_force_newton())
        print('%: ', force.get_force_percentage())
        if spento:
            hub.status_light.on('green')
        else:
            hub.status_light.on('black')
        spento = not spento

    else:
        if spento:
            hub.status_light.on('red')
        else:
            hub.status_light.on('black')
        spento = not spento

    if timer.now() > 10:
        break

    wait_for_seconds(.250)

print('Done!')
hub.status_light.on('black')

