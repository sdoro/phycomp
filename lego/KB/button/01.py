from spike import PrimeHub

hub = PrimeHub()                  # this is an object

# Create forever loops with python

while True:
    if hub.left_button.is_pressed(): # this is how to detect button presses
        hub.speaker.beep()
