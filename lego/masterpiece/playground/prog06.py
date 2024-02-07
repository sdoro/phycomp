'''
Ad esempio, il programma seguente divide il codice che controlla il colore rilevato e il pulsante premuto in due coroutine. La funzione `run()` sull'ultima riga di codice avvia entrambe le coroutine contemporaneamente.
'''

from hub import button, port, sound
import color
import color_sensor
import runloop

# Questa funzione restituisce `True` se il sensore di colore rileva il rosso.
def red_detected():
    return color_sensor.color(port.F) == color.RED

# Questa funzione restituisce `True` se si preme il pulsante sinistro.
def left_pressed():
    return button.pressed(button.LEFT) > 0

# Questa coroutine controlla continuamente se il sensore di colore rileva il rosso.
async def check_color():
    while True:
        # Attendi fino a quando viene rilevato il rosso.
        while not red_detected():
            await runloop.sleep_ms(1)
        # Quando viene rilevato, avvia un segnale acustico molto lungo.
        sound.beep(440, 1000000, 100)
        # Attendi fino a quando il rosso non viene più rilevato.
        while red_detected():
            await runloop.sleep_ms(1)
        # Quando il rosso non viene più rilevato, arresta il suono.
        sound.stop()

# Questa coroutine controlla continuamente se il pulsante sinistro è premuto.
async def check_button():
    while True:
        # Attendi fino a quando il pulsante sinistro viene premuto,
        while not left_pressed():
            await runloop.sleep_ms(1)
        # Quando lo premi emetti un breve segnale acustico.
        sound.beep(880, 200, 100)
        # Attendi fino al rilascio del pulsante sinistro.
        while left_pressed():
            await runloop.sleep_ms(1)

# Esegui entrambe le coroutine.
runloop.run(check_color(), check_button())

'''
Agita un mattoncino LEGO rosso davanti al sensore di colore e premi il pulsante sinistro sull'hub mentre il programma è in esecuzione. Come in precedenza, udirai un segnale acustico per tutto il tempo in cui viene rilevato il colore rosso e un breve segnale acustico ogni volta che viene premuto il pulsante sinistro. Questa volta, è possibile premere il pulsante sinistro e udire un segnale acustico mentre viene rilevato il colore rosso perché entrambe le funzioni vengono eseguite contemporaneamente.

Quando crei le coroutine, ricorda che:

-   Le coroutine devono includere almeno un comando `await`.
-   Con un ciclo `while` _stretto_, utilizza `await runloop.sleep_ms(1)` all'interno del ciclo per consentire l'avvio e l'esecuzione di altre coroutine.
'''


