from spike import ForceSensor
from spike import Motor
from spike.control import Timer

from spike import PrimeHub

# Initialize the Force Sensor
force = ForceSensor('B')

# Initialize the motor
motor = Motor('A')

timer = Timer()

hub = PrimeHub()

while True:
    if force.is_pressed():
        motor.start()
        print('Newton: ', force.get_force_newton())
        print('%: ', force.get_force_percentage())
        hub.status_light.on('green')
    else:
        motor.stop()
        hub.status_light.on('red')

    if timer.now() > 10:
        break

print('Done!')
hub.status_light.on('black')

motor.stop()

