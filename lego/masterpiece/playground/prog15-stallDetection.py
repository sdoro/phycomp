from hub import port, sound
import motor, runloop, sys

async def main():
    # Start the motor C (also D is available)
    ret = await motor.run_for_degrees(port.C, 500, 100)
    #print('ret: ', ret[0], '-', motor.STALLED)
    if ret[0] == motor.STALLED:
        print('Stalled dection!')
        await sound.beep(400, 1000)
    else:
        print('No stalled detection!')
    sys.exit(0)

runloop.run(main())

