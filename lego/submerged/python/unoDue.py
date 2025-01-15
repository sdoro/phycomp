from hub import light_matrix, port
import runloop
import motor_pair
import motor
import sys

motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)

async def main():

    # alzo la pala
    await motor.run_to_absolute_position(port.E,0,100)

    # vado avanti
    await light_matrix.write("f")
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 360+200, 0, velocity=200)

    # abbasso la pala
    await motor.run_to_absolute_position(port.E,260,100)

    # torno indietro
    await light_matrix.write("b")
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, -550-200, 0, velocity=200)
 

runloop.run(main())
sys.exit(0)
