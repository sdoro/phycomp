
# test su 3 tiles (Terminatore, Curva, Terminatore): T+C+T

from hub import port, button, sound
import motor, motor_pair, color_sensor, runloop, sys

import time

# The drive motors are in port A (left) and port E (right).
motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)

# The wheel circumference is 27.63 cm.
WHEEL_CIRCUMFERENCE = 27.63

# Questa funzione restituisce `True` se si preme il pulsante sinistro.
def left_pressed():
    return button.pressed(button.LEFT) > 0

# Questa coroutine controlla continuamente se il pulsante sinistro è premuto.
async def check_button():
    global leftPressed
    sound.beep(880, 200, 100)

    leftPressed = False
    while True:
        # Attendi fino a quando il pulsante sinistro viene premuto,
        while not left_pressed():
            await runloop.sleep_ms(1)
        # Quando lo premi emetti un breve segnale acustico.
        leftPressed = True
        sound.beep(880, 200, 100)
        # Attendi fino al rilascio del pulsante sinistro.
        while left_pressed():
            await runloop.sleep_ms(1)
        leftPressed = False

leftPressed = False

# Follow the right side of black line (Black-White edge).
# To follow a White-Black edge, change the error condition to (reflection - 50)
async def line_follow_forever(v):

    # reset position for right motor that moves clockwise
    motor.reset_relative_position(port.E, 0)

    start = time.ticks_ms()
    path = [[0, 0]]

    global leftPressed

    while True:
        rp = motor.relative_position(port.E)
        #cond = (rp < 1250) or (rp > 1450)
        if color_sensor.reflection(port.F) < 30:
            break
        #if color_sensor.reflection(port.F) < 30 and cond:        # sensore DX indica incrocio?
        #    break
        #    rp = motor.relative_position(port.E)
        #    break
        #    if (rp < 1250) or (rp > 1450):
        #        motor_pair.stop(motor_pair.PAIR_1)
        #        print('trovato arresto: ', rp)
        #        break                                        # fermati!
        # Compute the error: please attention to inversion!
        #error = 50 - color_sensor.reflection(port.B)       # il sensore SX (B) segue il lato DX della linea nera
        error = color_sensor.reflection(port.B) - 50        # il sensore SX (B) segue il lato SX della linea nera

        # Compute the correction by multiplying the error
        # by a Constant of Proportionality (p)
        p = 2.25
        # Since the maximum absolute value of error is 50, the correction ranges from -112 to 112
        correction = int(error * p)
        # clamp the correction from -100 to 100 because SP3 doesn’t seem to do it internally.
        correction = min(100, max(-100, correction))
        motor_pair.move(motor_pair.PAIR_1, correction, velocity = v)
        if leftPressed:
            print('pigiato left')
            rp = motor.relative_position(port.E)
            t = time.ticks_ms() - start
            if (rp - path[-1][0]) > 25:    # troppo vicini? non registro
                path.append([rp, t])

    motor_pair.stop(motor_pair.PAIR_1)

    lt = motor.relative_position(port.E) / 360 * WHEEL_CIRCUMFERENCE
    print(round(motor.relative_position(port.E),2), 'gradi')                            # print lenght track
    print(round(lt, 2), 'cm')                            # print lenght track
    print(time.ticks_ms() - start, 'msec')            # print lenght time
    print('path percorso: ', path)

async def main():
    leftPressed = False
    await line_follow_forever(125)
    sys.exit(0)

runloop.run(check_button(),main())
