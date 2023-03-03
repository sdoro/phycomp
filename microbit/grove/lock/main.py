from microbit import *
from tm1637 import TM1637
from LuchettoRotante import *
import music

# init display driver
tm = TM1637(clk=pin2, dio=pin16)

# init lock
combinazione = [10, 20, 30]
lucchetto = LucchettoRotante(combinazione)
print(lucchetto)


num = 0
tm.number(num)
lock = 0
im = Image.ARROW_E
display.show(im)
dx = True

while True:

    if button_a.was_pressed():
        # accetta il valore sul display come mossa sul lucchetto
        print('a pressed')
        if dx:
            print('dx')
            # chiama ruota a dx per lock 
            lucchetto.giraDestra(lock)
            im = Image.ARROW_W
            display.show(im)
            dx = False
        else:
            print('dx')
            # chiama ruota a sx per lock
            lucchetto.giraSinistra(lock)
            im = Image.ARROW_E
            display.show(im)
            dx = True

    elif button_b.was_pressed():
        # dai il comando apri al lucchetto
        print('b pressed')
        # prova ad aprire
        if lucchetto.apri():
            print("lucchetto aperto")
            display.show(Image.HAPPY)
            music.play(music.PUNCHLINE)
            
        else:
            print("lucchetto NON aperto")
            display.show(Image.SAD)
            music.play(music.FUNERAL)

        break
        
    if pin_logo.is_touched():
        # dai il comando reset al lucchetto
        print("reset")
        lucchetto.reset()
        lock = 0
        im = Image.ARROW_E
        display.show(im)
        dx = True

    sleep(1000)
    # transform a value from Potentiometer [0, 1021] into a number between 0 and 39
    val = pin0.read_analog()
    tmp = val*39//1021
    if tmp != lock:
        # if rotated make a "click"
        lock = tmp
        music.pitch(800, 6)

    tm.number(lock)
    print('val[0,1021]: ', val, ' lock[0,39]: ', lock)

# bot
