from spike import PrimeHub, MotorPair
from spike.control import wait_for_seconds


hub = PrimeHub()
drive_motors = MotorPair('A', 'E')


drive_motors.set_default_speed(50)
drive_motors.set_motor_rotation(27.63, 'cm')


def square():
    for x in range(4):
        drive_motors.move(1.5, 'rotations')
        drive_motors.move(0.365, 'rotations', steering=100)


def triangle():
    for x in range(3):
        drive_motors.move(1.5, 'rotations')
        drive_motors.move(0.486, 'rotations', steering=100)


def circle():
    drive_motors.move(3, 'rotations', steering=60)


wait_for_seconds(1)

square()
hub.speaker.beep()

triangle()
hub.speaker.beep()

circle()
hub.speaker.beep()
