from hub import port
import motor_pair, color_sensor, runloop

# Constants for Drive Base 1
motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)

# Follow the right side of black line (Black-White edge). NOTE: Our test was run on a black-white mat.
# If your mat has many colors, you will have to lower the threshold to avoid other colors.
# To follow a White-Black edge, change the IF condition from < 50 to > 50
# To use color mode, import color, and use condition:
# if (color_sensor.color(port.A) == color.BLACK)
async def line_follow_forever(v):
    while (True):
        if (color_sensor.reflection(port.B) < 50): # sensor is on Black. Lower threshold as needed for your case.
            # Turn right, i.e. away from Black
            motor_pair.move(motor_pair.PAIR_1, 50, velocity = v)
        else: # sensor is on white
            # Turn left, i.e. towards Black
            motor_pair.move(motor_pair.PAIR_1, -50, velocity = v)

async def main():
    await line_follow_forever(200)

runloop.run(main())
