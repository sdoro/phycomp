from microbit import *

baseline = compass.get_field_strength() # Take a baseline reading of magnetic strength

while True:
  if abs(compass.get_field_strength() - baseline) > 10000:
      # Magnetic field strength increased by 10000
      display.show(Image.NO)    # Show a cross symbol
  else:
      display.clear()
