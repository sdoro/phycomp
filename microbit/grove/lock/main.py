from microbit import *
from tm1637 import TM1637
from LuchettoRotante import *
import music

combinazione = [10, 20, 30]
lucchetto = LucchettoRotante(combinazione)
print(lucchetto)

tm = TM1637(clk=pin2, dio=pin16)


num = 0
tm.number(num)
lock = 0
im = Image.ARROW_E
display.show(im)
dx = True

while True:
    if button_a.was_pressed():
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
        print('b pressed')
        # prova ad aprire
        if lucchetto.apri():
            print("lucchetto aperto")
            music.play(music.PUNCHLINE)
            
        else:
            print("lucchetto NON aperto")
            music.play(music.FUNERAL)

        break
        
    if pin_logo.is_touched():
        # reset
        print("reset")
        lucchetto.reset()
        lock = 0
        im = Image.ARROW_E
        display.show(im)
        dx = True
        
    sleep(1000)
    val = pin0.read_analog()
    tmp = val*39//1021
    if tmp != lock:
        lock = tmp
        music.pitch(800, 6)
    #display.scroll(str(lock))
    tm.number(lock)
    #music.pitch(800, 6)
    print('val: ', val, ' lock: ', lock)
