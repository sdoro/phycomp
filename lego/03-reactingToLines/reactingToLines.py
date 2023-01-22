from spike import PrimeHub, MotorPair, ColorSensor
from spike.control import wait_for_seconds

hub = PrimeHub()
drive_motors = MotorPair('C', 'D')
color_sensor = ColorSensor('B')

drive_motors.set_default_speed(50)
POWER = 50

while True:
if hub.left_button.was_pressed():
    drive_motors.start()
    color_sensor.wait_until_color('black')
    drive_motors.stop()

if hub.right_button.was_pressed():
    while True:
        drive_motors.start_tank_at_power(0, POWER)
        color_sensor.wait_until_color('black')
        drive_motors.start_tank_at_power(POWER, 0)
        color_sensor.wait_until_color('white')
