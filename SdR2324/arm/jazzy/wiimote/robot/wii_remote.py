import cwiid
 
print("Press down and hold buttons 1 and 2 on the Nintendo Wii remote.")
print(" ")
print("Hold down until you see a success message.")
print("If unsuccessful, try again.")
 
# Create a Wiimote object and assign it to the
# variable named wii. Bluetooth handshake
# is performed between the Wii remote
# and the Raspberry Pi
wii = cwiid.Wiimote()
 
print("Wiimote is Ready!")
 
# Turn on Wiimote reporting to enable the Python
# code to receive input from the Wiimote.
wii.rpt_mode = cwiid.RPT_BTN

cnt = 0
 
while cnt < 5:
   print(cnt)
   # Save the value of the button that was pressed
   # into a variable named buttons
   buttons = wii.state["buttons"]
 
   # Bit-wise AND operation. Returns 1 in each
   # bit position for which buttons and
   # cwiid.BTN_XXXX are ones.
   if (buttons & cwiid.BTN_LEFT):
      print("robot.left()")
   if (buttons & cwiid.BTN_RIGHT):
      print("robot.right()")
   if (buttons & cwiid.BTN_UP):
      print("robot.forward()")
   if (buttons & cwiid.BTN_DOWN):
      print("robot.backward()")
   if (buttons & cwiid.BTN_B):
      print("robot.stop()")

   cnt += 1
   import time
   time.sleep(1)
