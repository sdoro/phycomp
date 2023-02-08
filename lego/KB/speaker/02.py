from spike import PrimeHub
from spike.control import wait_for_seconds

hub = PrimeHub()


# start, wait LEFT button (don't release), beep, wait LEFT button release, stop beep

hub.left_button.wait_until_pressed()
hub.speaker.start_beep(85)

hub.right_button.wait_until_pressed()
hub.speaker.stop()
