from hub import light_matrix, port
import runloop
import motor_pair
import motor
import sys

motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)


async def main():
    
    # abbasso la pala
    await motor.run_to_absolute_position(port.E,260,100)

    # vado avanti
    await light_matrix.write("f")
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 1646, 0, velocity=300)

    # abbasso la pala
    await motor.run_to_absolute_position(port.E,0,100)
   
    # torno indietro
    await light_matrix.write("b")
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, -1646-180, 0, velocity=300)
 

runloop.run(main())
sys.exit(0)
