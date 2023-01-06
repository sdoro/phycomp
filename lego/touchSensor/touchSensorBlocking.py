from spike import ForceSensor
from spike import Motor
from spike.control import Timer

# Initialize the Force Sensor
force = ForceSensor('B')

# Initialize the motor
motor = Motor('A')

from spike import PrimeHub

timer = Timer()

hub = PrimeHub()

while True:
    force.wait_until_pressed()
    motor.start()
    print('Newton: ', force.get_force_newton())
    print('%: ', force.get_force_percentage())
    hub.status_light.on('green')


    force.wait_until_released()
    motor.stop()
    hub.status_light.on('red')


    if timer.now() > 10:
        break

print('Done!')
hub.status_light.on('black')

