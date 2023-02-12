from spike import PrimeHub
from spike.control import wait_for_seconds

hub = PrimeHub()                  # this is an object

# for loops are used to repeat something a fixed number of times

for i in range(10):
    hub.light_matrix.write(i)
    hub.speaker.beep(60, 0.3)
    wait_for_seconds(0.5)
