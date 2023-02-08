from spike import PrimeHub
from spike.control import wait_for_seconds

hub = PrimeHub()


# start beep, wait 2 sec, stop beep

hub.speaker.start_beep(85)

wait_for_seconds(2)

hub.speaker.stop()
