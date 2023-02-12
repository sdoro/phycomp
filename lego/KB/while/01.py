from spike import PrimeHub

hub = PrimeHub()                  # this is an object

# while loops are used to repeat something while a condition is true

from spike.control import wait_for_seconds

z = 0
while z < 10:
    hub.light_matrix.write(z)
    hub.speaker.beep(60, 0.3)
    wait_for_seconds(0.5)
    z += 1
