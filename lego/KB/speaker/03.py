from spike import PrimeHub
from spike.control import wait_for_seconds

hub = PrimeHub()


# start, wait LEFT button (and release), beep, wait RIGHT button (and release), stop beep


hub.left_button.wait_until_pressed()
hub.speaker.start_beep(85)

hub.left_button.wait_until_released()
hub.speaker.stop()
