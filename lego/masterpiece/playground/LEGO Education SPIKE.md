# Python

## Guida introduttiva

### Introduzione a Python

Python è un noto linguaggio di programmazione basato su testo, particolarmente adatto per i principianti perché è conciso e facile da leggere. È utile anche per i programmatori perché è applicabile allo sviluppo Web e software, nonché ad applicazioni scientifiche come l'analisi dei dati e l'apprendimento automatico (machine learning).

Questa **Guida introduttiva** fornisce le nozioni di base sull'utilizzo di Python con LEGO® Education SPIKE™ Prime. Contenuti dei capitoli:

**Introduzione a Python**

1.  Impara a usare l'_editor di codice_ nell'app LEGO® Education SPIKE™ App per scrivere codice in Python.

**Hello, World!**

2.  Scrivi un messaggio sulla matrice luce dell'hub SPIKE Prime.

**Commenti in Python**

3.  Scopri come i commenti possono aiutarti a descrivere le bozze e i programmi finiti.

**Controllo dei motori**

4.  Definisci e avvia _funzioni asincrone_ per controllare i motori.

**Variabili**

5.  Controlla due motori con variabili _locali_ e _globali_.

**Il potere del numero casuale**

6.  Scopri come creare programmi divertenti e imprevedibili che controllano la luce sull'hub.

**Controllo del sensore**

7.  Controlla un motore utilizzando il sensore di forza. Quindi impara a utilizzare la console per eseguire il _debug_ del programma.

**Condizioni del sensore**

8.  Utilizza _espressioni logiche_ per reagire a condizioni diverse. Quindi impara a eseguire insieme parti diverse del codice per reagire a più condizioni.

**Passaggi successivi**

9.  Ottieni suggerimenti sulle risorse aggiuntive per saperne di più sull'uso di Python con SPIKE Prime.

#### Sintassi di Python

Quando si impara un linguaggio di programmazione basata su testo, il primo passo è comprenderne la _sintassi_. Questa sintassi del linguaggio stabilisce le regole per la scrittura di _istruzioni_ (righe di codice) e come indicare _blocchi di codice_ costituiti da più istruzioni.

In Python, ogni istruzione inizia con un livello di _rientro_ e termina con un'_interruzione di riga_. Il rientro è il numero di spazi prima di un'istruzione. Le righe con lo stesso numero di spazi hanno lo stesso _livello di rientro_ e appartengono allo stesso blocco di codice. L'app SPIKE utilizza 4 spazi per ogni livello di rientro.

È possibile scrivere il codice nell'_editor di codice_, le cui funzionalità consentono di scriverlo correttamente. Ad esempio, quando si avvia un nuovo blocco di codice, ad esempio una _funzione_ o un'istruzione `if`, l'editor fa rientrare la riga successiva con quattro spazi aggiuntivi. Inoltre, numera ogni riga per facilitare l'esplorazione del codice.

_L'evidenziazione della sintassi_ nell'editor di codice mostra _commenti_, _parole chiave_, testo e numeri in colori diversi in modo che il codice risulti più facile da leggere. Nel codice seguente, il commento sulla prima riga è verde, le parole chiave `print`, `if` e `True` sono blu, il testo `'LEGO'` è magenta e il numero `123` è arancione.

```
# Questo è un commento
print('LEGO')
if True:
    print(123)
```

Il codice sopra riportato è un _programma di esempio_, che troverai in tutti i capitoli della **Guida introduttiva**. Ogni esempio presenta un'icona Copia nell'angolo in alto a destra:

![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt73a5a79fe3818470/63e0ca257ccfaf4bc687f657/copy.svg)

Premi questa icona per copiare l'intero programma di esempio. Quindi fai clic con il pulsante destro del mouse o premi a lungo l'editor di codice e scegli Incolla dal menu per incollare il codice. Puoi anche premere `CTRL`+`V` in Windows o `Command`+`V` in Mac.

#### Moduli SPIKE Prime

Per controllare l'hub SPIKE Prime, i sensori e i motori, sono necessari i _moduli_ SPIKE Prime. I moduli vengono utilizzati per organizzare il codice correlato. Ce n'è uno per ogni componente SPIKE Prime, ad esempio, il modulo `motor` contiene il codice per controllare i motori. Per utilizzare la funzionalità di un modulo, prima è necessario _importarlo_ con l'istruzione `import`:

```
import motor
```

Importa i moduli necessari una volta all'inizio del programma Python. Vedi la sezione relativa ai **Moduli SPIKE Prime** di questa Guida per l'utente per ulteriori informazioni sui moduli e la rispettiva funzionalità.

#### MicroPython

L'hub SPIKE Prime è un piccolo computer denominato microcontrollore, dotato di memoria e potenza di elaborazione limitate. Poiché il linguaggio di programmazione Python completo utilizzerebbe troppa memoria, l'hub esegue _MicroPython_, una versione altamente ottimizzata del linguaggio Python, che può essere eseguita su microcontrollori. Anche i moduli per controllare l'hub SPIKE Prime, i sensori e i motori sono altamente ottimizzati grazie all'uso di _tipi di dati perfezionati_.

Hai visto che l'editor di codice mostra testo e numeri in colori diversi, perché si tratta di tipi di dati diversi. Python effettua un'ulteriore distinzione tra numeri interi e decimali. I numeri interi sono anche noti come _interi_ o di tipo `int`, che è ottimizzato in MicroPython. I decimali utilizzano il tipo `float` non ottimizzato, pertanto i moduli SPIKE Prime evitano questo tipo di dati. Ciò significa che devi attenerti ai numeri interi o utilizzare _unità_ diverse per descrivere i decimali. Per indicare mezzo secondo, puoi utilizzare 500 millisecondi anziché 0,5 secondi.

#### Sfida

Puoi copiare parte del codice di esempio in questo capitolo e incollarlo nell'editor di codice?

### Hello, World!

Quando si impara un nuovo linguaggio di programmazione, è tradizione creare un programma "Hello, World!". Scriverai "Hello, World!" sulla matrice luce dell'hub SPIKE Prime. Innanzitutto, assicurati che l'hub SPIKE Prime sia acceso e connesso all'app SPIKE. Quindi segui questi quattro passaggi:

1.  Assicurati che l'editor di codice sia vuoto eliminando il codice esistente.
2.  Premi l'icona Copia nell'angolo in alto a destra dell'esempio seguente per copiare il codice.
3.  Fai clic con il pulsante destro del mouse o premi a lungo l'editor di codice, quindi scegli Incolla dal menu per incollare il codice.
4.  Premi il pulsante Play per eseguire il programma.

```
from hub import light_matrix

light_matrix.write('Hello, World!')
```

Vedrai scorrere il testo "Hello, World!" nella matrice luce.

Diamo un'occhiata al codice riga per riga.

La prima riga importa il modulo `light_matrix` dal modulo `hub`, che controlla la Matrice luce dell'hub. Dopo aver importato un modulo, è possibile utilizzarne le varie funzioni.

L'ultima riga _chiama_ la _funzione_ `write()`dal modulo `light_matrix` per scrivere "Hello, World!" sulla matrice luce.

#### Definizione di una funzione

Nell'esempio precedente è stata utilizzata la funzione `write()`. Una funzione è un blocco di codice che esegue un'attività quando viene chiamata. È possibile definire una funzione con la parola chiave `def`, seguita dal nome della funzione, dalle parentesi e dai due punti. Il _corpo_ della funzione è rientrato e contiene tutto il codice che viene eseguito quando chiami la funzione. È possibile chiamare una funzione scrivendo il nome della funzione e le parentesi. Assicurati di annullare il _rientro_ della chiamata di funzione, altrimenti farà parte del corpo della funzione.

L'esempio seguente definisce la funzione `hello()`, che scrive "Hello, World!" sulla matrice luce e chiama la funzione una volta. Prova a eseguire il codice di esempio. Ricorda di eliminare il codice esistente dall'editor di codice, prima di copiare, incollare ed eseguire il codice.

```
from hub import light_matrix

def hello():
    light_matrix.write('Hello, World!')

hello()
```

#### Aggiunta di un parametro

Nell'esempio precedente, la funzione `hello()` non presenta _parametri_, quindi scrive "Hello World" sulla matrice luce ogni volta che la chiami. Per un effetto più dinamico, aggiungi un nome di parametro all'interno delle parentesi della definizione della funzione. Il blocco di codice nel corpo della funzione può quindi utilizzare questo parametro per eseguire operazioni diverse in base al relativo valore. Un esempio di quanto detto sopra è la funzione `write()`, che ha un parametro obbligatorio: il testo da scrivere sulla matrice luce.

Nell'esempio seguente aggiungiamo un parametro `name` alla funzione `hello()`, che quindi scrive `'Hello, ' + name + '!'` sulla matrice luce. Nota l'_operatore_ `+`, che consente di aggiungere parti di testo insieme. Il testo è noto anche come _stringa_ o tipo `str`. È racchiuso tra virgolette semplici singole (`'`) o doppie (`"`), utilizzando lo stesso tipo intorno a una determinata stringa di testo. La funzione aggiornata `hello()` ha un parametro obbligatorio di tipo `str`, quindi puoi _passare_ la stringa `'World'` come _argomento_ quando la chiami per scrivere "Hello, World!" sulla matrice luce.

Prova a eseguire il codice di esempio. Non dimenticare di eliminare il codice esistente dall'editor di codice prima di copiare, incollare ed eseguire il nuovo codice.

```
from hub import light_matrix

def hello(name):
    light_matrix.write('Hello, ' + name + '!')

hello('World')
```

Vedrai scorrere ancora una volta il testo "Hello, World!" nella matrice luce.

#### Sfida

Puoi modificare il codice in modo che l'hub saluti \* te \*anziché il mondo?

### Commenti in Python

È più facile usare il codice quando si sa cosa si deve fare. Puoi descriverlo nel linguaggio di tutti i giorni aggiungendo commenti. I commenti non fanno parte del codice eseguito nell'hub, quindi non ne influenzano la funzionalità.

Il carattere `#` segna l'inizio di un commento. In genere si inserisce un commento prima del codice che lo descrive, ma è anche possibile inserire brevi commenti dopo un'istruzione di codice.

```
# Questo è un commento
from hub import light_matrix
# Questo è un altro commento
```

A volte parte del programma non si comporta come vorresti. In questi casi, è utile _commentare_ parti del codice aggiungendo il carattere `#` all'inizio della riga. Queste righe diventano quindi commenti e non vengono più eseguite come parte del programma. Aggiungere commenti su parti di un programma può aiutare a _eseguire il debug_ o trovare e correggere il problema. Per commentare rapidamente più righe di codice, selezionale e premi `CTRL`+`/` su Windows o `Command`+`/` su Mac. Per riportare più commenti in codice, selezionali e premi la stessa combinazione di tasti.

```
# La riga successiva è commentata:
# light_matrix.write('Hello, World!')
```

Puoi anche utilizzare i commenti per descrivere il codice prima di scrivere il codice di lavoro. Quest'ultimo è chiamato _pseudo-codice_ e può aiutarti a descrivere nel linguaggio di tutti i giorni cosa dovrebbe fare il programma. Nell'esempio seguente vengono utilizzati i commenti come pseudocodice per l'animazione del battito di ciglia sulla matrice luce.

```
# Mostra una faccina felice con occhi sulla matrice luce.
# Attendi per un po' di tempo.
# Mostra uno smile senza occhi sulla matrice luce.
# Attendi per un breve periodo di tempo.
# Mostra di nuovo la prima immagine sulla matrice luce.
```

#### Programma Battito di ciglia

Questo programma mostrerà sulla matrice luce dell'Hub una faccina con le ciglia che battono. Copia il codice riportato di seguito e incollalo nell'editor di codice. Quindi, eseguire il programma. Come sempre, elimina qualsiasi codice esistente dall'editor di codice prima di incollare il nuovo codice.

Quando esegui questo programma, vedrai lampeggiare la faccina sorridente dopo un secondo. Il programma chiama la funzione `show_image()` dal modulo `hub.light_matrix` per mostrare un'immagine sulla matrice luce. Il programma utilizza la funzione `sleep_ms()` del modulo `time` per aggiungere ritardi di alcuni millisecondi tra immagini diverse. Nel codice, ogni commento descrive le operazioni che deve eseguire la riga di codice successiva.

```
import time

from hub import light_matrix

# Mostra una faccina felice sulla matrice luce.
light_matrix.show_image(light_matrix.IMAGE_HAPPY)

# Attendi per un secondo.
time.sleep_ms(1000)

# Mostra uno smile sulla matrice luce.
light_matrix.show_image(light_matrix.IMAGE_SMILE)

# Attendi per 0,2 secondi
time.sleep_ms(200)

# Mostra una faccina felice sulla matrice luce.
light_matrix.show_image(light_matrix.IMAGE_HAPPY)
```

#### "WET" o "DRY"?

Anche se commentare ogni riga di codice è allettante, il risultato che otterrai è _WET (Write Everything Twice)_, ovvero scriverai tutto due volte. Questi commenti _WET_ non aiutano i lettori se il codice è autoesplicativo. Segui invece il principio _DRY_ (Don't repeat yourself) e _non ripeterti_.

Nell'esempio seguente, le righe di codice che fanno battere le ciglia sono all'interno della nuova funzione `blink()`. Il programma chiama quindi la funzione tre volte, in modo che le ciglia battano tre volte. Nota: questa volta i commenti descrivono solo le parti principali del codice per aiutare i lettori a capire cosa dovrebbe fare.

```
import time

from hub import light_matrix

# Questa funzione fa battere le ciglia.
def blink():
    light_matrix.show_image(light_matrix.IMAGE_HAPPY)
    time.sleep_ms(1000)
    light_matrix.show_image(light_matrix.IMAGE_SMILE)
    time.sleep_ms(200)
    light_matrix.show_image(light_matrix.IMAGE_HAPPY)

# Fai battere le ciglia tre volte.
blink()
blink()
blink()
```

#### Sfida

Puoi modificare il codice per far sì che gli occhi rimangano aperti più a lungo ogni volta che battono le ciglia?

### Controllo dei motori

Ora puoi connetterti e utilizzare i motori. Connetti un motore alla porta A e prova il programma riportato di seguito.

![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt63eb551ed45ad623/63e0d3764488ff110cae9e58/controlling_motors.png)

```
import motor
from hub import port

# Aziona un motore sulla porta A per 360 gradi a 720 gradi al secondo.
motor.run_for_degrees(port.A, 360, 720)
```

Dovresti vedere il motore girare a 360 gradi (una rotazione completa) a 720 gradi (due rotazioni) al secondo.

Esaminiamo il codice riga per riga.

La prima riga importa il modulo `motor` che controlla i motori.

La seconda riga importa `port` dal modulo `hub`, che contiene il valore per ogni porta. Puoi scrivere `port.A` per la porta A, `port.B` per la porta B e così via per specificare le porte desiderate.

L'ultima riga chiama la funzione `run_for_degrees()` con tre _argomenti_:

1.  Il primo parametro specifica il motore da azionare, utilizzando il valore della porta.
2.  Il secondo parametro specifica il numero di gradi da eseguire.
3.  Il terzo parametro specifica a quale velocità azionare il motore, in gradi al secondo.

#### Motori multipli

Ora connetti un secondo motore alla porta B e prova il programma riportato di seguito.

```
import motor
from hub import port

# Aziona due motori sulle porte A e B per 360 gradi a 720 gradi al secondo.
# I motori funzionano contemporaneamente.
motor.run_for_degrees(port.A, 360, 720)
motor.run_for_degrees(port.B, 360, 720)
```

Nota: entrambi i motori girano a 360 gradi (una rotazione) a 720 gradi al secondo, iniziando e terminando contemporaneamente. Poiché le istruzioni dei due motori si trovano su righe separate, ci si potrebbe aspettare che vengano eseguite una alla volta. Tuttavia, vengono eseguite contemporaneamente perché `run_for_degrees()` è una funzione _awaitable_, ovvero che può essere eseguita in modo asincrono. Ciò significa che \*puoi \* aspettare che venga completata, ma non è necessario. Per impostazione predefinita, il programma continua immediatamente alla riga di codice successiva mentre il codice awaitable viene eseguito fino al completamento in background. Ciò consente di eseguire più comandi contemporaneamente.

#### Ciclo di esecuzione e parole chiave Async e Await

Per utilizzare in modo efficace il codice awaitable con la flessibilità di eseguire comandi contemporaneamente o in sequenza, è necessario eseguire il codice in una _funzione asincrona_ utilizzando un _ciclo di esecuzione_. Il modulo `runloop` controlla il ciclo di esecuzione sull'hub e consente di eseguire funzioni asincrone con la rispettiva funzione `run()`. Una funzione asincrona, nota anche come _coroutine_, è un elemento awaitable che utilizza la parola chiave `async` prima della definizione della funzione. Di norma, si denomina la coroutine contenente il programma principale `main()`. Il codice seguente mostra la struttura generale di un programma che utilizza un ciclo di esecuzione.

```
import runloop

async def main():
    # Scrivi qui il tuo programma.

runloop.run(main())
```

Nel corpo di una coroutine, è possibile utilizzare la parola chiave `await` prima di chiamare un comando awaitable. In questo modo la coroutine viene messa in pausa fino al completamento del comando. Senza la parola chiave, il programma continua immediatamente alla riga di codice successiva nella coroutine. È comunque possibile utilizzare il codice normale (non awaitable) all'interno della coroutine. Tuttavia, in questo modo verrà sempre messo in pausa o _bloccato_ l'intero programma fino al completamento del comando.

Il programma seguente definisce la coroutine `main()`, che utilizza la parola chiave `await` prima delle due chiamate di funzione `run_for_degrees()`. Viene utilizzata la funzione `run()` del modulo `runloop` per eseguire la coroutine `main()` sulla riga di codice finale.

```
import motor
import runloop
from hub import port

async def main():
    # Aziona due motori sulle porte A e B per 360 gradi a 720 gradi al secondo.
    # I motori vengono azionati uno dopo l'altro.
    await motor.run_for_degrees(port.A, 360, 720)
    await motor.run_for_degrees(port.B, 360, 720)

runloop.run(main())
```

Prova il codice di esempio. Dovresti vedere entrambi i motori girare a 360 gradi (una rotazione) a 720 gradi al secondo, uno alla volta.

#### Sfida

È possibile modificare il codice per azionare nuovamente entrambi i motori contemporaneamente?

### Variabili

A volte, ci si ritrova a scrivere lo stesso numero più volte. Ad esempio, i comandi del motore nel capitolo precedente venivano eseguiti ogni volta per lo stesso numero di gradi alla stessa velocità. In casi come questo, l'utilizzo delle variabili semplifica la modifica di più comandi.

Puoi creare una variabile scrivendone il nome, seguito da un singolo segno `=` e il valore iniziale per la variabile. Se desideri modificare il valore di una variabile esistente, utilizza lo stesso identico formato per _assegnarle_ un nuovo valore.

Connetti i motori alle porte A e B e prova il programma riportato di seguito.

```
import motor
import runloop
from hub import port

async def main():
    # Creare una variabile `velocity` con un valore di 720.
    velocity = 720

    # Aziona due motori sulle porte A e B per 360 gradi.
    # Utilizza il valore della variabile `velocity` per la velocità del motore.
    await motor.run_for_degrees(port.A, 360, velocity)
    await motor.run_for_degrees(port.B, 360, velocity)

runloop.run(main())
```

Come nel capitolo precedente, vedrai entrambi i motori girare a 360 gradi (una rotazione) a 720 gradi al secondo, uno alla volta. Nell'esempio riportato di seguito viene creata una variabile `velocity` e viene utilizzata nelle chiamate di funzione `run_for_degrees()`. Poiché abbiamo usato una variabile, è facile modificare la velocità del motore per tutti i comandi del motore. Prova a modificare il valore della variabile `velocity` ed esegui nuovamente il programma.

#### Ambito della variabile

È importante capire l'importanza di _dove_ viene creata una variabile. Quando si crea una variabile all'interno di una funzione, questa è disponibile solo per tale funzione. Questa è chiamata variabile _locale_ . Se desideri utilizzare una variabile tra diverse funzioni del programma, devi creare la variabile all'esterno delle funzioni, ad esempio sotto le istruzioni `import`. Questa è chiamata variabile _globale_.

```
import motor
import runloop
from hub import port

# Crea una variabile globale `velocity` con un valore di 720.
velocity = 720

async def main():
    # Crea una variabile locale `degrees` con un valore di 360.
    degrees = 360

    # Aziona due motori sulle porte A e B.
    # Utilizza il valore della variabile `degrees` per il numero di gradi.
    # Utilizza il valore della variabile `velocity` per la velocità del motore.
    await motor.run_for_degrees(port.A, degrees, velocity)
    await motor.run_for_degrees(port.B, degrees, velocity)

runloop.run(main())
```

Ancora una volta, vedrai entrambi i motori girare a 360 gradi (una rotazione) a 720 gradi al secondo, uno alla volta. Questa volta la variabile `velocity` ha un _ambito_ globale e una nuova variabile `degrees` ha un ambito locale. Puoi utilizzare la variabile globale `velocity` sia all'interno che all'esterno della funzione `main()`, ma la variabile locale `degrees` può essere utilizzata solo all'interno della funzione `main()` in cui è definita.

Definire tutte le variabili nella parte superiore del programma in modo che abbiano un ambito globale può essere allettante, perché in tal modo è possibile utilizzarle comodamente nell'intero programma. Tuttavia, ciò significa anche che il valore di tali variabili può essere modificato da _qualsiasi punto_ del programma, con effetti collaterali indesiderati. È invece opportuno che le variabili abbiano un _ambito ristretto_, in modo che solo le parti del programma che devono utilizzarle e modificarle possano accedervi.

#### Variabili nei cicli

In Python, il modo più semplice per ripetere un codice per un certo numero di volte è usare un ciclo `for` con la funzione `range()` incorporata. Ad esempio, per ripetere qualcosa quattro volte, si scrive `for i in range(4):` seguito dal codice che si desidera eseguire quattro volte. Puoi pensare a `range(4)` come la _tupla_ `(0, 1, 2, 3)`. Tuple ed _elenchi_ come `[1, 2, 3]` sono oggetti _iterabili_. Il ciclo `for` prende un iterabile e ne \* scorre in ciclo\* i rispettivi valori fino a raggiungere la fine.

Quando un ciclo `for` _itera_ su una tupla o un elenco, modifica il valore di una variabile locale su ogni iterazione. Finora, hai creato variabili in modo esplicito e assegnato loro un valore usando il segno `=`. In un ciclo `for`, il nome della variabile locale viene definito dopo la parola chiave `for`, in questo caso `i`. Ogni volta che il ciclo viene eseguito, il valore di questa variabile locale `i` cambia. Sarà `0` la prima volta che il ciclo viene eseguito e `3` l'ultima volta che viene eseguito, che corrispondono ai valori in `(0, 1, 2, 3)`.

Nell'esempio seguente viene utilizzato un ciclo `for` per modificare la variabile globale `velocity` quattro volte per azionare il motore sulla porta A ogni volta con una velocità diversa. Per abilitare la modifica della variabile globale `velocity` nel _contesto locale_ della funzione `main()`, è necessario utilizzare la parola chiave `global` prima di `velocity` all'inizio del corpo della funzione.

```
import motor
import runloop
from hub import port

# Creare una variabile globale `velocity` con un valore di 450.
velocity = 450

async def main():
    # Utilizza la parola chiave `global` per abilitare la modifica `velocity` qui.
    global velocity

    # Crea una variabile locale `degrees` con un valore di 360.
    degrees = 360

    # Il ciclo `for` crea una variabile locale `i` e si ripete 4 volte.
    # I valori della variabile `i` sono 0, 1, 2 e 3.
    for i in range(4):
        # Modifica la variabile globale `velocity` aggiungendo `i`*90 ogni volta.
        # I valori della variabile `velocity` sono 450, 540, 720 e 990.
        velocity = velocity + i*90
        await motor.run_for_degrees(port.A, degrees, velocity)

    # Il valore della variabile `velocity` esterna al ciclo `for` è 990.
    await motor.run_for_degrees(port.B, degrees, velocity)

runloop.run(main())
```

Esegui il codice di esempio. Vedrai il motore sulla porta A girare a 360 gradi per quattro volte, a quattro velocità diverse che aumentano ogni volta. Alla fine, il motore sulla porta B gira una volta a 360 gradi a 990 gradi al secondo.

#### Sfida

Puoi modificare il codice in modo che il motore sulla porta A giri ogni volta a un numero diverso di gradi?

### Il potere del numero casuale

A volte, il miglior programma è imprevedibile. Quando non sai cosa farà un programma, questo sembra più vivo. Per ottenere questo risultato, aggiungi un po' di casualità.

Il programma seguente imposterà la luce del pulsante di accensione dell'hub SPIKE Prime su dieci colori diversi, con un ritardo casuale tra ogni cambio di colore.

```
import random
import time
from hub import light

for color in range(11):
    # Imposta la luce sul colore corrente.
    light.color(light.POWER, color)

    # Tieni la luce accesa per 0,5-1,5 secondi.
    sleep_time = random.randint(500, 1500)
    time.sleep_ms(sleep_time)
```

Ogni colore è rappresentato da un numero diverso. Il ciclo `for` esegue l'iterazione su `range(11)` e assegna il valore alla variabile `color`. La luce sarà impostata su `0` (nero) che la spegne alla prima esecuzione del ciclo e su `10` (bianco) nell'ultima iterazione. Nota: questo programma importa il modulo `random`, che contiene diverse funzioni per aggiungere casualità.

In questo esempio viene utilizzata la funzione `randint()`, con un valore `start` di 500 e un valore `stop` di 1500. Con questi argomenti, la funzione \* restituisce\*, un numero compreso tra 500 e 1500 per aggiungere qualche variazione al tempo di sospensione. Tuttavia, i colori si illumineranno sempre nello stesso ordine anche se si esegue il programma più volte. Fortunatamente, il modulo `random` presenta altre funzioni per aggiungere ancora più casualità al programma.

#### Ciclo continuo

È anche possibile usare un ciclo `while` per ripetere un'operazione continuamente anziché numero di volte specifico. In Python, il modo più semplice per creare tale ciclo è scrivere `while True:` seguito dal codice che desideri eseguire continuamente. Nell'esempio successivo viene utilizzato un ciclo `while True` per eseguire continuamente un piccolo spettacolo di luci o fino all'arresto del programma.

```
import random
import time
from hub import light

while True:
    # Genera un numero casuale compreso tra 1 e 9.
    random_color = random.randint(1, 9)

    # Imposta la luce sul colore casuale.
    light.color(light.POWER, random_color)

    # Tieni la luce accesa per 0,5-1,5 secondi.
    sleep_time = random.randint(500, 1500)
    time.sleep_ms(sleep_time)
```

Nota: il pulsante di accensione si illumina in colori casuali, con un ritardo casuale tra ogni cambio di colore. Nell'esempio viene utilizzata di nuovo la funzione `randint()` per generare un numero compreso tra 1 e 9 (entrambi inclusi), che corrisponde ai diversi numeri di colore, tranne il nero (`0`) e il bianco (`10`).

#### Elenchi e costanti

Se vuoi che lo spettacolo di luci includa solo determinati colori, puoi inserirli in un _elenco_ da cui scegliere un colore casuale. Crei un nuovo elenco come una variabile, scrivendo prima il nome dell'elenco, quindi il segno `=` e infine i valori tra parentesi quadre, separati da virgole. Per un elenco semplice con almeno due _elementi_, scrivi `my_list = [1, 2]`. Puoi aggiungere tutti i valori desiderati.

Come hai visto negli esempi precedenti, ogni colore è rappresentato da un numero diverso. Puoi utilizzare questo numero per impostare la luce su colore corrispondente, ad esempio, il numero `9` imposterà la luce sul rosso. Tuttavia, l'utilizzo di numeri per i colori può rendere più difficile per gli altri lettori capire cosa farà il codice. È possibile aggiungere commenti per descrivere ogni valore, ma creare variabili per ogni colore è un modo migliore. Il modulo `color` ha una variabile `RED` in modo da poter scrivere `color.RED` al posto del numero `9` nel codice. (Una variabile nell'elenco con tutte le lettere maiuscole è una _costante_, il che significa che non la si deve modificare).

Nell'esempio seguente viene importato il modulo `color` e vengono utilizzate alcune costanti di colore per creare l'elenco `colors`. Questa volta, la funzione `randint()` determina il numero di volte in cui viene eseguito il ciclo `for` e la luce diventa bianca alla fine di questo piccolo spettacolo di luci casuali.

```
import random
import time
import color
from hub import light

# Crea un elenco con alcuni colori chiari diversi.
colors = [color.RED, color.GREEN, color.BLUE, color.YELLOW]

# Modifica la luce da cinque a dieci volte.
times = random.randint(5, 10)

for i in range(times):
    # Scegli un colore casuale dall'elenco dei colori.
    random_color = random.choice(colors)

    # Imposta la luce sul colore casuale.
    light.color(light.POWER, random_color)

    # Tieni la luce accesa per 0,5-1,5 secondi.
    sleep_time = random.randint(500, 1500)
    time.sleep_ms(sleep_time)

# Imposta la luce su bianco.
light.color(light.POWER, color.WHITE)
```

La spia del pulsante di accensione cambierà in uno dei colori causali dell'elenco, per un numero casuale di volte, con un ritardo casuale tra ogni cambio di colore. Nell'esempio viene utilizzata la funzione `choice()` per selezionare un colore casuale dall'elenco `colors`.

#### Sfida

Puoi cambiare il codice in modo da includere colori diversi nell'elenco `colors`?

### Controllo del sensore

Nei capitoli precedenti, hai provato a usare variabili e numeri casuali per controllare i motori e la luce. Ora utilizzerai un valore del sensore per controllare un motore.

Connetti un motore alla porta A e un sensore di forza alla porta B e prova il programma riportato di seguito.

![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltb1f58f66da0fcb3e/63e0d376260a9a2054c6d1ad/sensor_control.png)

```
import force_sensor
import motor
from hub import port

# Memorizza la forza del sensore di forza in una variabile.
force = force_sensor.force(port.B)

# Stampa la variabile nella console.
print(force)

# Aziona il motore e utilizza la variabile per impostare la velocità.
motor.run(port.A, force)
```

Premi il sensore di forza mentre il programma è in esecuzione. Questa operazione non è servita a molto, giusto? Fortunatamente, l'esempio utilizza la funzione integrata `print()` per scrivere la variabile `force` nella console, in modo da poter vedere facilmente cosa è andato storto.

#### La console

A volte il tuo programma non fa quello che ti aspetti che faccia. Quando ciò accade, puoi utilizzare la funzione `print()` per eseguire il _debug_ del programma. La funzione `print()` scrive qualsiasi cosa passi come argomento nella finestra Console sotto l'editor di codice, in questo caso la forza del sensore di forza. Esegui nuovamente il programma e osserva il valore visualizzato nella console.

Vedrai un singolo numero nella console e, a meno che tu non stia premendo il sensore di forza quando hai avviato il programma, quel numero è `0`. Azionare un motore a 0 gradi al secondo non serve a molto, quindi il problema è che il programma controlla il valore del sensore solo una volta all'inizio del programma. Per aggiornare la velocità del motore in base alla forza per tutta da durata dell'esecuzione del programma, è necessario utilizzare di nuovo il ciclo `while True`.

Inoltre, nella console vengono visualizzati i messaggi di errore quando si verifica un problema durante l'esecuzione del programma. Un errore comune si verifica quando si esegue un programma per controllare un motore o leggere un sensore non connesso. Disconnetti il sensore di forza ed esegui lo stesso programma un'ultima volta. Nella console viene visualizzato un messaggio di errore che informa che c'è stato un problema, la relativa descrizione e su quale riga di codice si è verificato.

#### Correzione dei bug

La console ti ha aiutato a trovare due bug. Connetti di nuovo il sensore di forza alla porta B per correggere il secondo bug, quindi esegui il programma sottostante che corregge il primo bug _racchiudendo_ il codice in un ciclo `while True`.

```
import force_sensor
import motor
from hub import port

while True:
    # Memorizza la forza del sensore di forza in una variabile.
    force = force_sensor.force(port.B)

    # Stampa la variabile nella console.
    print(force)

    # Aziona il motore e utilizza la variabile per impostare la velocità.
    motor.run(port.A, force)
```

Premi il sensore di forza mentre il programma è in esecuzione. Vedrai il motore accelerare o rallentare a seconda di quanto forte premi il sensore di forza. Nella console vengono visualizzati anche molti valori variabili. La forza del sensore di forza viene misurata in decinewton (dN) e poiché la forza massima misurabile è di 10 newton, il valore massimo in dN è pari a 100. Un motore che gira a 100 gradi al secondo non è ancora molto veloce!

#### Valori restituiti dalla funzione

Invece di memorizzare il valore del sensore di forza in una variabile, è anche possibile definire una funzione che _restituisce_ questo valore. Separare le diverse parti del programma in questo modo semplifica l'organizzazione del codice e la correzione di eventuali bug.

Il programma successivo definisce una funzione `motor_velocity()` che restituisce la velocità del motore desiderata in base alla forza del sensore di forza anziché utilizzare una variabile.

```
import force_sensor
import motor
from hub import port

# Questa funzione restituisce la velocità del motore desiderata.
def motor_velocity():
    # La velocità è cinque volte la forza del sensore di forza.
    return force_sensor.force(port.B) * 5

while True:
    # Aziona il motore come prima.
    # Utilizza il valore restituito dalla funzione `motor_velocity()` per la velocità.
    motor.run(port.A, motor_velocity())
```

Premi il sensore di forza mentre il programma è in esecuzione. Vedrai il motore accelerare o rallentare a seconda di quanto forte premi il sensore di forza. La funzione `motor_velocity()` moltiplica il valore della forza per 5, quindi la velocità sarà compresa tra 0 e 500 gradi al secondo.

#### Sfida

Puoi modificare il codice per azionare il motore a 1000 gradi al secondo quando il sensore di forza è completamente premuto?

### Condizioni del sensore

Hai utilizzato il valore del sensore per controllare direttamente un motore, ma è anche possibile modificare il _flusso_ del programma utilizzando le _condizioni_ del sensore e un'istruzione `if`. L'istruzione `if` è una parte essenziale della programmazione, nonché il modo più semplice per controllare il flusso del programma.

Per creare un'istruzione `if`, devi scrivere `if` seguita da un'espressione logica e dai due punti. Le espressioni logiche sono fondamentalmente domande chiuse (sì/no), come "Il colore è rosso?" o "Il pulsante è premuto?" Se la risposta alla domanda è "sì", l'espressione viene valutata come `True`, altrimenti è `False`. Questi sono i due valori _booleani_ usati in Python e sono di tipo `bool`. Tutte le righe di codice con lo stesso livello di rientro dopo l'istruzione `if` fanno parte del blocco di codice che viene eseguito se l'espressione è `True`.

Ad esempio, connetti un sensore di colore alla porta A ed esegui il programma riportato di seguito.

![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/blt91959e56cb5c545c/63e0d376c28ed80d991c9e78/sensor_conditions.png)

```
from hub import port, sound
import color
import color_sensor
import runloop

async def main():
    while True:
        # Controlla se viene rilevato il colore rosso.
        if color_sensor.color(port.A) == color.RED:
            # Se viene rilevato il rosso, avvia un segnale acustico molto lungo.
            sound.beep(440, 1000000, 100)
            # Metti in pausa il programma mentre viene rilevato il rosso.
            while color_sensor.color(port.A) == color.RED:
                await runloop.sleep_ms(1)
            # Arresta il suono quando il rosso non viene più rilevato.
            sound.stop()

runloop.run(main())
```

Agita un mattoncino LEGO® rosso davanti al sensore di colore mentre il programma è in esecuzione. Quando viene rilevato il colore rosso udirai un segnale acustico, che si arresta quando tale colore non viene più rilevato. Nell'esempio viene utilizzata un'istruzione `if` per verificare se il colore rilevato dal sensore di colore è rosso. Tale verifica viene effettuata utilizzando l'_operatore di uguaglianza_ `==` con il valore di colore del sensore di colore a sinistra e la costante `color.RED` a destra. (Nota che ci sono due segni `=` rispetto al singolo segno `=` utilizzato per assegnare valori alle variabili). Se il valore di colore del sensore di colore è uguale alla costante `color.RED`, la condizione è `True` e viene eseguito il blocco di codice dopo l'istruzione `if`.

È importante racchiudere il codice in un ciclo `while True`. In caso contrario, il sensore di colore controlla il colore solo per una frazione di secondo all'avvio del programma. Finora, hai usato il ciclo `while` con la costante `True` per ripetere il codice in continuazione. È inoltre possibile utilizzare il ciclo `while` con un'espressione logica per ripetere il codice solo finché tale espressione restituisce `True`. L'esempio precedente utilizza la stessa condizione dell'istruzione `if` nel ciclo interno `while` per continuare a riprodurre il segnale acustico mentre viene rilevato il colore rosso. Quando la condizione non è più `True`, l'hub _esce_ dal ciclo `while` ed esegue la riga di codice successiva per arrestare il suono.

All'interno del loop interno `while`, nota la funzione `sleep_ms()` del modulo `runloop`. Questa funzione mette in pausa la coroutine `main()` per un certo numero di millisecondi in modo _non bloccante_. Poiché utilizza la parola chiave `await`, è possibile eseguire altre attività mentre la coroutine è in pausa. Nell'esempio, la pausa è di un millisecondo. Questo tempo può sembrare poco, ma è sufficiente per consentire all'hub di eseguire molte coroutine contemporaneamente. La funzione `sleep_ms()` del modulo `time`, utilizzata nei capitoli precedenti, mette in pausa il programma in modo _bloccante_. Ciò significa che mette in pausa l'intero programma e non solo il blocco di codice in cui viene chiamato.

#### Che altro?

Puoi aggiungere più di una condizione estendendo l'istruzione `if` con un'istruzione `elif` che controlla un'altra condizione. Puoi aggiungere tutti questi elementi necessari e seguire la stessa sintassi dell'istruzione `if`. L'istruzione `elif` essere sullo stesso livello di rientro della prima istruzione `if` e la parola chiave `elif` deve essere è seguita da un'espressione logica e dai due punti. Applica un rientro alle righe di codice successive da eseguire quando questa condizione è `True`.

A volte, nessuna delle condizioni nelle istruzioni `if` e `elif` è `True`. In questo caso, è possibile eseguire un codice aggiungendo un'istruzione `else` senza alcuna condizione. Questo viene eseguito quando tutte le condizioni precedenti sono `False`.

Ad esempio, il programma seguente aggiunge un'istruzione `elif` e `else` per emettere un segnale acustico anche se viene premuto il pulsante sinistro.

```
from hub import button, port, sound
import color
import color_sensor
import runloop

# Questa funzione restituisce `True` se il sensore di colore rileva il rosso.
def red_detected():
    return color_sensor.color(port.A) == color.RED

# Questa funzione restituisce `True` se si preme il pulsante sinistro.
def left_pressed():
    return button.pressed(button.LEFT) > 0

async def main():
    while True:
        if red_detected():
            # Se viene rilevato il rosso, avvia un segnale acustico molto lungo.
            sound.beep(440, 1000000, 100)
            # Attendi fino a quando il rosso non viene più rilevato.
            while red_detected():
                await runloop.sleep_ms(1)
        elif left_pressed():
            # Premendo il pulsante sinistro viene emesso un breve segnale acustico.
            sound.beep(880, 200, 100)
            # Attendi fino al rilascio del pulsante sinistro.
            while left_pressed():
                await runloop.sleep_ms(1)
        else:
            # In caso contrario, arresta il suono.
            sound.stop()

runloop.run(main())
```

Agita un mattoncino LEGO rosso davanti al sensore di colore e premi il pulsante sinistro sull'hub mentre il programma è in esecuzione. Udirai un segnale acustico per tutto il tempo in cui viene rilevato il colore rosso e un breve segnale acustico ogni volta che viene premuto il pulsante sinistro.

Nell'esempio vengono definite due funzioni per eseguire i test logici e restituire il risultato. La funzione `red_detected()` controlla se il colore rilevato dal sensore di colore è il rosso e restituisce il risultato `True` o `False`. La funzione `left_pressed()` utilizza la funzione `pressed()` del modulo `hub.button` e utilizza l'operatore `>` per verificare se il valore è _maggiore di_ `0` e restituisce il risultato.

Il codice nell'istruzione `if` riportato qui è in gran parte lo stesso del primo esempio, ma ora utilizza la funzione `red_detected()` in due posizioni invece di ripetere la condizione per le istruzioni `if` e `while`. L'istruzione `elif` utilizza la funzione `left_pressed()` per verificare se il pulsante sinistro sull'hub viene premuto per più di `0` millisecondi.

Nota: l'istruzione `elif` viene eseguita solo quando la condizione della prima istruzione `if` è `False`. Pertanto, la pressione del pulsante mentre il sensore di colore rileva qualcosa di rosso non produce alcun effetto. Considera attentamente l'ordine delle condizioni `if` e `elif`, quindi controlla prima quelle più importanti. L'istruzione `else` arresta il suono se nessuna delle due condizioni è `True`.

#### Condizioni multiple

Quando si utilizzano le istruzioni `if`/`elif`/`else` per verificare la presenza di più condizioni, viene eseguito solo uno dei blocchi. Queste condizioni si _escludono a vicenda_. Hai visto che durante il rilevamento del colore rosso, la pressione del pulsante sinistro non ha prodotto alcun effetto. Per verificare effettivamente più condizioni, è necessario controllarle contemporaneamente. Come l'aggiunta di diversi stack di blocchi parole, in Python è possibile eseguire più coroutine con la funzione `run()` del modulo `runloop`. Finora, l'hai chiamata con la coroutine `main()` come unico argomento, ma è possibile passare più coroutine come argomenti separati da virgole.

Ad esempio, il programma seguente divide il codice che controlla il colore rilevato e il pulsante premuto in due coroutine. La funzione `run()` sull'ultima riga di codice avvia entrambe le coroutine contemporaneamente.

```
from hub import button, port, sound
import color
import color_sensor
import runloop

# Questa funzione restituisce `True` se il sensore di colore rileva il rosso.
def red_detected():
    return color_sensor.color(port.A) == color.RED

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
```

Agita un mattoncino LEGO rosso davanti al sensore di colore e premi il pulsante sinistro sull'hub mentre il programma è in esecuzione. Come in precedenza, udirai un segnale acustico per tutto il tempo in cui viene rilevato il colore rosso e un breve segnale acustico ogni volta che viene premuto il pulsante sinistro. Questa volta, è possibile premere il pulsante sinistro e udire un segnale acustico mentre viene rilevato il colore rosso perché entrambe le funzioni vengono eseguite contemporaneamente.

Quando crei le coroutine, ricorda che:

-   Le coroutine devono includere almeno un comando `await`.
-   Con un ciclo `while` _stretto_, utilizza `await runloop.sleep_ms(1)` all'interno del ciclo per consentire l'avvio e l'esecuzione di altre coroutine.

#### Sfida

Puoi modificare il codice per rilevare un colore diverso dal rosso?

### Passaggi successivi

Nei capitoli precedenti:

-   Hai appreso le basi per utilizzare Python con SPIKE Prime e come utilizzare la matrice luce, la luce, l'altoparlante e i pulsanti, nonché i motori, il sensore di colore e il sensore di forza dell'hub.
-   Hai acquisito familiarità con le funzioni regolari e asincrone, le variabili locali e globali e i tipi di dati come `int`, `bool`, `str`, `tuple` e `list`.
-   Hai utilizzato i cicli `for` e `while`, nonché le istruzioni `if`/`elif`/`else` per controllare il flusso del programma.
-   Hai imparato a utilizzare i commenti nel codice e, quando le cose vanno male, a eseguire il debug del programma.

Complimenti, hai raggiunto un bel risultato!

Se vuoi saperne di più sull'uso di Python con SPIKE Prime, sono disponibili ulteriori risorse cui puoi accedere.

#### Guida per l'utente di Python

Questa sezione della **Guida introduttiva** ha coperto solo in parte tutto ciò che è possibile fare con Python e SPIKE Prime. Esplora queste altre tre sezioni della Guida per l'utente di Python.

1.  **Esempi** Trova programmi di esempio che mostrano come usare Python per eseguire varie attività. Copiali, provali e modificali in base alle tue esigenze.
2.  **Moduli SPIKE Prime** Trova la documentazione di tutte le funzioni e le variabili nei moduli SPIKE Prime con brevi esempi di come usarle.

#### Lezioni di Python

Nel sito Web LEGOeducation.com/lessons, seleziona il prodotto **SPIKE™ Prime with Python**. Troverai diverse unità di apprendimento con 6-8 lezioni ciascuna (disponibili solo in inglese). Queste 50+ lezioni coprono una vasta gamma di argomenti, dal debug al controllo dei sensori, da semplici giochi a dati e funzioni matematiche. Scopri le numerose possibilità e impara a padroneggiare il linguaggio di programmazione Python con SPIKE Prime.

#### Sfida

Crea un nuovo progetto Python e inizia a programmare!

## Moduli API

### App

Il modulo `app` viene utilizzato per comunicare tra hub e app

#### Moduli secondari

#### Grafico a barre

Il modulo `bargraph` viene utilizzato per creare grafici a barre nell’app SPIKE

Per utilizzare il modulo `bargraph`, è sufficiente importarlo nel modo seguente:

```
from app import bargraph
```

Dettagli `bargraph`

##### Funzioni

##### change

change(color: int, value: float) -> None

###### Parametri

___

###### color: int

Un colore del modulo `color`

###### value: float

Il valore

##### clear\_all

clear\_all() -> None

###### Parametri

___

##### get\_value

get\_value(color: int) -> Awaitable

###### Parametri

___

###### color: int

Un colore del modulo `color`

##### hide

hide() -> None

###### Parametri

___

##### set\_value

set\_value(color: int, value: float) -> None

###### Parametri

___

###### color: int

Un colore del modulo `color`

###### value: float

Il valore

##### show

show(fullscreen: bool) -> None

###### Parametri

___

###### fullscreen: bool

Mostra su schermo intero

#### Visualizza

Il modulo `display` viene utilizzato per visualizzare le immagini nell’app SPIKE

Per utilizzare il modulo `display`, è sufficiente importarlo nel modo seguente:

```
from app import display
```

Dettagli `display`

##### Funzioni

##### hide

hide() -> None

###### Parametri

___

##### image

image(image: int) -> None

###### Parametri

___

###### Immagine: int

ID dell’immagine da mostrare. La gamma di immagini disponibili è compresa tra 1 e 21. Sono presenti costanti sul modulo `display` per queste

##### show

show(fullscreen: bool) -> None

###### Parametri

___

###### fullscreen: bool

Mostra su schermo intero

##### text

text(text: str) -> None

###### Parametri

___

###### text: str

Testo da visualizzare

##### Costanti

___

##### app.display Costanti

**IMAGE\_ROBOT\_1** = 1

**IMAGE\_ROBOT\_2** = 2

**IMAGE\_ROBOT\_3** = 3

**IMAGE\_ROBOT\_4** = 4

**IMAGE\_ROBOT\_5** = 5

**IMAGE\_HUB\_1** = 6

**IMAGE\_HUB\_2** = 7

**IMAGE\_HUB\_3** = 8

**IMAGE\_HUB\_4** = 9

**IMAGE\_AMUSEMENT\_PARK** = 10

**IMAGE\_BEACH** = 11

**IMAGE\_HAUNTED\_HOUSE** = 12

**IMAGE\_CARNIVAL** = 13

**IMAGE\_BOOKSHELF** = 14

**IMAGE\_PLAYGROUND** = 15

**IMAGE\_MOON** = 16

**IMAGE\_CAVE** = 17

**IMAGE\_OCEAN** = 18

**IMAGE\_POLAR\_BEAR** = 19

**IMAGE\_PARK** = 20

**IMAGE\_RANDOM** = 21

#### Linegraph

Il modulo `linegraph` viene utilizzato per creare grafici a linee nell’app SPIKE

Per utilizzare il modulo `linegraph`, è sufficiente importarlo nel modo seguente:

```
from app import linegraph
```

Dettagli `linegraph`

##### Funzioni

##### clear

clear(color: int) -> None

###### Parametri

___

###### color: int

Un colore del modulo `color`

##### clear\_all

clear\_all() -> None

###### Parametri

___

##### get\_average

get\_average(color: int) -> Awaitable

###### Parametri

___

###### color: int

Un colore del modulo `color`

##### get\_last

get\_last(color: int) -> Awaitable

###### Parametri

___

###### color: int

Un colore del modulo `color`

##### get\_max

get\_max(color: int) -> Awaitable

###### Parametri

___

###### color: int

Un colore del modulo `color`

##### get\_min

get\_min(color: int) -> Awaitable

###### Parametri

___

###### color: int

Un colore del modulo `color`

##### hide

hide() -> None

###### Parametri

___

##### plot

plot(color: int, x: float, y: float) -> None

###### Parametri

___

###### color: int

Un colore del modulo `color`

###### x: float

Valore X

###### y: float

Valore Y

##### show

show(fullscreen: bool) -> None

###### Parametri

___

###### fullscreen: bool

Mostra su schermo intero

#### Musica

Il modulo `music` viene utilizzato per fare musica nell’app SPIKE

Per utilizzare il modulo `music`, è sufficiente importarlo nel modo seguente:

```
from app import music
```

Dettagli `music`

##### Funzioni

##### play\_drum

play\_drum(drum: int) -> None

###### Parametri

___

###### drum: int

Il nome del tamburo. Vedere tutti i valori disponibili nel modulo app.sound.

##### play\_note

play\_note(instrument: int, note: int, duration: int) -> None

###### Parametri

___

###### instrument: int

Il nome dello strumento. Vedere tutti i valori disponibili nel modulo app.music.

###### note: int

La nota midi da suonare (0-130)

###### duration: int

Durata in millisecondi.

##### Costanti

___

##### app.music Costanti

**DRUM\_BASS** = 2

**DRUM\_BONGO** = 13

**DRUM\_CABASA** = 15

**DRUM\_CLAVES** = 9

**DRUM\_CLOSED\_HI\_HAT** = 6

**DRUM\_CONGA** = 14

**DRUM\_COWBELL** = 11

**DRUM\_CRASH\_CYMBAL** = 4

**DRUM\_CUICA** = 18

**DRUM\_GUIRO** = 16

**DRUM\_HAND\_CLAP** = 8

**DRUM\_OPEN\_HI\_HAT** = 5

**DRUM\_SIDE\_STICK** = 3

**DRUM\_SNARE** = 1

**DRUM\_TAMBOURINE** = 7

**DRUM\_TRIANGLE** = 12

**DRUM\_VIBRASLAP** = 17

**DRUM\_WOOD\_BLOCK** = 10

**INSTRUMENT\_BASS** = 6

**INSTRUMENT\_BASSOON** = 14

**INSTRUMENT\_CELLO** = 8

**INSTRUMENT\_CHOIR** = 15

**INSTRUMENT\_CLARINET** = 10

**INSTRUMENT\_ELECTRIC\_GUITAR** = 5

**INSTRUMENT\_ELECTRIC\_PIANO** = 2

**INSTRUMENT\_FLUTE** = 12

**INSTRUMENT\_GUITAR** = 4

**INSTRUMENT\_MARIMBA** = 19

**INSTRUMENT\_MUSIC\_BOX** = 17

**INSTRUMENT\_ORGAN** = 3

**INSTRUMENT\_PIANO** = 1

**INSTRUMENT\_PIZZICATO** = 7

**INSTRUMENT\_SAXOPHONE** = 11

**INSTRUMENT\_STEEL\_DRUM** = 18

**INSTRUMENT\_SYNTH\_LEAD** = 20

**INSTRUMENT\_SYNTH\_PAD** = 21

**INSTRUMENT\_TROMBONE** = 9

**INSTRUMENT\_VIBRAPHONE** = 16

**INSTRUMENT\_WOODEN\_FLUTE** = 13

#### Suono

Il modulo `sound` è utilizzato per riprodurre suoni nell’app SPIKE

Per utilizzare il modulo `sound`, è sufficiente importarlo nel modo seguente:

```
from app import sound
```

Dettagli `sound`

##### Funzioni

##### play

play(sound\_name: str, volume: int = 100, pitch: int = 0, pan: int = 0) -> Awaitable

Riproduce un suono nell’App SPIKE

###### Parametri

___

###### sound\_name: str

Il nome del suono visualizzato nell'estensione audio Blocchi parole

###### volume: int

Volume (0-100)

###### pitch: int

Il tono del suono

###### pan: int

L'effetto panoramica determina quale altoparlante emette il suono, dove "-100" corrisponde a solo l'altoparlante sinistro, "0" normale e "100" solo l'altoparlante giusto.

##### set\_attributes

set\_attributes(volume: int, pitch: int, pan: int) -> None

###### Parametri

___

###### volume: int

Volume (0-100)

###### pitch: int

Il tono del suono

###### pan: int

L'effetto panoramica determina quale altoparlante emette il suono, dove "-100" corrisponde a solo l'altoparlante sinistro, "0" normale e "100" solo l'altoparlante giusto.

##### stop

stop() -> None

###### Parametri

___

### Colore

Il modulo `color` contiene tutte le costanti di colore da utilizzare con i moduli `color_matrix`, `color_sensor` e `light`.

Per utilizzare il modulo Colore, aggiungi la seguente istruzione di importazione al progetto:

```
import color
```

#### Costanti

___

#### color Costanti

**BLACK** = 0

**MAGENTA** = 1

**PURPLE** = 2

**BLUE** = 3

**AZURE** = 4

**TURQUOISE** = 5

**GREEN** = 6

**YELLOW** = 7

**ORANGE** = 8

**RED** = 9

**WHITE** = 10

**UNKNOWN** = -1

### Matrice di colori

Per utilizzare il modulo Matrice di colori, aggiungi la seguente istruzione di importazione al progetto:

```
import color_matrix
```

Tutte le funzioni del modulo devono essere chiamate all'interno del modulo `color_matrix` come prefisso nel modo seguente:

```
color_matrix.set_pixel(port.A, 1, 1, (color.BLUE, 10))
```

#### Funzioni

#### clear

clear(port: int) -> None

Disattiva tutti i pixel su una matrice di colori

```
from hub import port
import color_matrix

color_matrix.clear(port.A)
```

##### Parametri

___

##### port: int

Una porta del modulo secondario `port` nel modulo `hub`

#### get\_pixel

get\_pixel(port: int, x: int, y: int) -> tuple\[int, int\]

Recupera un pixel specifico rappresentato come una tupla contenente il colore e l'intensità

```
from hub import port
import color_matrix

# Stampa il colore e l’intensità del pixel 0,0 sulla matrice di colori collegata alla porta A 
print(color_matrix.get_pixel(port.A, 0, 0))
```

##### Parametri

___

##### port: int

Una porta del modulo secondario `port` nel modulo `hub`

##### x: int

Il valore X (0 - 2)

##### y: int

Il valore Y, intervallo (0 - 2)

#### set\_pixel

set\_pixel(port: int, x: int, y: int, pixel: tuple\[color: int, intensity: int\]) -> None

Modifica un singolo pixel su una matrice di colori

```
from hub import port
import color
import color_matrix

# Modifica il colore del pixel 0,0 sulla matrice di colori collegata alla porta A 
color_matrix.set_pixel(port.A, 0, 0, (color.RED, 10))

# Stampa il colore del pixel 0,0 sulla matrice di colori collegata alla porta A 
print(color_matrix.get_pixel(port.A, 0, 0)[0])
```

##### Parametri

___

##### port: int

Una porta del modulo secondario `port` nel modulo `hub`

##### x: int

Il valore X (0 - 2)

##### y: int

Il valore Y, intervallo (0 - 2)

##### pixel: tuple\[color: int, intensity: int\]

Tupla contenente colore e intensità, ovvero con quale intensità illuminare il pixel

#### show

show(port: int, pixels: list\[tuple\[int, int\]\]) -> None

Modifica tutti i pixel contemporaneamente su una matrice di colori

```
from hub import port
import color
import color_matrix

# Aggiorna tutti i pixel sulla matrice di colori usando la funzione show 

# Crea un elenco con 18 elementi (coppie di colori e intensità) 
pixels = [(color.BLUE, 10)] * 9 

# Aggiorna tutti i pixel per mostrare lo stesso colore e intensità 
color_matrix.show(port.A, pixels)
```

##### Parametri

___

##### port: int

Una porta del modulo secondario `port` nel modulo `hub`

##### pixels: list\[tuple\[int, int\]\]

Un elenco contenente valori di colore e intensità per tutti i 9 pixel.

### Sensore di colore

Il modulo `color_sensor` consente di scrivere codice che reagisce a colori specifici o all'intensità della luce riflessa.

Per utilizzare il modulo Sensore di colore, aggiungi la seguente istruzione di importazione al progetto:

```
import color_sensor
```

Tutte le funzioni del modulo devono essere chiamate all'interno del modulo `color_sensor` come prefisso nel modo seguente:

```
color_sensor.reflection(port.A)
```

Il Sensore di colore è in grado di riconoscere i seguenti colori:

Rosso  
Verde  
Blu  
Magenta  
Giallo  
Arancione  
Azzurro  
Nero  
Bianco

#### Funzioni

#### color

color(port: int) -> int

Restituisce il valore di colore del colore rilevato. Utilizza il modulo `color` per mappare il valore di colore a un colore specifico.

```
import color_sensor
from hub import port
import color

if color_sensor.color(port.A) is color.RED:
    print("Red detected")
```

##### Parametri

___

##### port: int

Una porta del modulo secondario `port` nel modulo `hub`

#### reflection

reflection(port: int) -> int

Recupera l'intensità della luce riflessa (0-100%).

##### Parametri

___

##### port: int

Una porta del modulo secondario `port` nel modulo `hub`

#### rgbi

rgbi(port: int) -> tuple\[int, int, int, int\]

Recupera l'intensità complessiva del colore e l'intensità del rosso, del verde e del blu.

Restituisce tuple\[red: int, green: int, blue: int, intensity: int\]

##### Parametri

___

##### port: int

Una porta del modulo secondario `port` nel modulo `hub`

### Dispositivo

Il modulo `device` consente di scrivere codice per ottenere informazioni sui dispositivi collegati all'hub.

Per utilizzare il modulo Dispositivo, aggiungi la seguente istruzione di importazione al progetto:

```
import device
```

Tutte le funzioni del modulo devono essere chiamate all'interno del modulo `device` come prefisso nel modo seguente:

```
device.device_id(port.A)
```

#### Funzioni

#### data

data(port: int) -> tuple\[int\]

Recupera i dati raw LPF-2 da un dispositivo.

##### Parametri

___

##### port: int

Una porta del modulo secondario `port` nel modulo `hub`

#### device\_id

device\_id(port: int) -> int

Recupera l'ID dispositivo di un dispositivo. Ogni dispositivo dispone di un ID in base al rispettivo tipo.

##### Parametri

___

##### port: int

Una porta del modulo secondario `port` nel modulo `hub`

#### get\_duty\_cycle

get\_duty\_cycle(port: int) -> int

Recupera il ciclo di lavoro di un dispositivo. I valori restituiti sono compresi tra 0 e 10.000

##### Parametri

___

##### port: int

Una porta del modulo secondario `port` nel modulo `hub`

#### ready

ready(port: int) -> bool

Quando un dispositivo è collegato all'hub, potrebbe essere necessario un breve intervallo di tempo prima che sia pronto ad accettare le richieste.  
Utilizzare `ready` per verificare la conformità dei dispositivi collegati.

##### Parametri

___

##### port: int

Una porta del modulo secondario `port` nel modulo `hub`

#### set\_duty\_cycle

set\_duty\_cycle(port: int, duty\_cycle: int) -> None

Imposta il ciclo di lavoro su un dispositivo. Intervallo da 0 a 10.000

##### Parametri

___

##### port: int

Una porta del modulo secondario `port` nel modulo `hub`

##### duty\_cycle: int

Valore PWM (0-10.000)

### Sensore di distanza

Il modulo `distance_sensor` consente di scrivere un codice che reagisce a distanze specifiche o che illumina il Sensore di distanza in modi diversi.

Per utilizzare il modulo Sensore di distanza, aggiungi la seguente istruzione di importazione al progetto:

```
import distance_sensor
```

Tutte le funzioni del modulo devono essere chiamate all'interno del modulo `distance_sensor` come prefisso nel modo seguente:

```
distance_sensor.distance(port.A)
```

#### Funzioni

#### clear

clear(port: int) -> None

Spegne tutte le luci nel sensore di distanza collegato a `port`.

##### Parametri

___

##### port: int

Una porta del modulo secondario `port` nel modulo `hub`

#### distance

distance(port: int) -> int

Recupera la distanza in millimetri acquisita dal sensore di distanza collegato a `port`. Se il sensore di distanza non è in grado di leggere una distanza valida, restituirà -1.

##### Parametri

___

##### port: int

Una porta del modulo secondario `port` nel modulo `hub`

#### get\_pixel

get\_pixel(port: int, x: int, y: int) -> int

Recupera l'intensità di una luce specifica sul sensore di distanza collegato a `port`.

##### Parametri

___

##### port: int

Una porta del modulo secondario `port` nel modulo `hub`

##### x: int

Il valore X (0 - 3)

##### y: int

Il valore Y, intervallo (0 - 3)

#### set\_pixel

set\_pixel(port: int, x: int, y: int, intensity: int) -> None

Modifica l'intensità di una luce specifica sul sensore di distanza collegato a `port`.

##### Parametri

___

##### port: int

Una porta del modulo secondario `port` nel modulo `hub`

##### x: int

Il valore X (0 - 3)

##### y: int

Il valore Y, intervallo (0 - 3)

##### intensity: int

Quanto illuminare il pixel

#### show

show(port: int, pixels: list\[int\]) -> None

Cambia tutte le luci contemporaneamente.

```
from hub import port
import distance_sensor

# Aggiorna tutte le luci sul sensore di distanza utilizzando la funzione show 

# Crea un elenco con 4 valori di intensità identici 
pixels = [100] * 4 

# Aggiorna tutti i pixel per mostrare la stessa intensità 
distance_sensor.show(port.A, pixels)
```

##### Parametri

___

##### port: int

Una porta del modulo secondario `port` nel modulo `hub`

##### pixels: bytes

Un elenco contenente valori di intensità per tutti e 4 i pixel.

### Sensore di forza

Il modulo `force_sensor` contiene tutte le funzioni e le costanti per utilizzare il sensore di forza.

Per utilizzare il modulo Sensore di forza, aggiungi la seguente istruzione di importazione al progetto:

```
import force_sensor
```

Tutte le funzioni del modulo devono essere chiamate all'interno del modulo `force_sensor` come prefisso nel modo seguente:

```
force_sensor.force(port.A)
```

#### Funzioni

#### force

force(port: int) -> int

Recupera la forza misurata, in decinewton. I valori sono compresi tra 0 e 100

```
from hub import port
import force_sensor


print(force_sensor.force(port.A))
```

##### Parametri

___

##### port: int

Una porta del modulo secondario `port` nel modulo `hub`

#### pressed

pressed(port: int) -> bool

Verifica che il pulsante sul sensore sia premuto. Restituisce vero se viene premuto il sensore di forza collegato alla porta.

```
from hub import port
import force_sensor


print(force_sensor.pressed(port.A))
```

##### Parametri

___

##### port: int

Una porta del modulo secondario `port` nel modulo `hub`

#### raw

raw(port: int) -> int

Restituisce il valore di forza raw del Sensore di forza collegato alla porta `port`

```
from hub import port
import force_sensor


print(force_sensor.raw(port.A))
```

##### Parametri

___

##### port: int

Una porta del modulo secondario `port` nel modulo `hub`

### Hub

#### Moduli secondari

#### Pulsante

Per utilizzare il modulo Pulsante, aggiungi la seguente istruzione di importazione al progetto:

```
from hub import button
```

Tutte le funzioni del modulo devono essere chiamate all'interno del modulo `button` come prefisso nel modo seguente:

```
button.pressed(button.LEFT)
```

##### Funzioni

##### pressed

int pressed(button: int) -> int

Questo modulo consente di reagire ai pulsanti premuti sull'hub. Per utilizzare i pulsanti, prima è necessario importare il modulo `button`.

```
from hub import button

left_button_press_duration = 0

# Attendi che venga premuto il pulsante sinistro 
while not button.pressed(button.LEFT):
    pass

# Aggiorna la variabile `left_button_press_duration` tenendo premuto il pulsante sinistro 
while button.pressed(button.LEFT):
    left_button_press_duration = button.pressed(button.LEFT)

print("Left button was pressed for " + str(left_button_press_duration) + " milliseconds")

```

###### Parametri

___

###### button: int

Un pulsante del modulo secondario `button` nel modulo `hub`

##### Costanti

___

##### hub.button Costanti

**LEFT** = 1  
Pulsante sinistro accanto al pulsante di accensione sull'hub SPIKE Prime  
**RIGHT** = 2  
Pulsante destro accanto al pulsante di accensione sull'hub SPIKE Prime

#### Luce

Il modulo `light` include funzioni per cambiare il colore della luce sull’hub SPIKE Prime.

Per utilizzare il modulo Luce, aggiungi la seguente istruzione di importazione al progetto:

```
from hub import light
```

Tutte le funzioni del modulo devono essere chiamate all'interno del modulo `light` come prefisso nel modo seguente:

```
light.color(color.RED)
```

##### Funzioni

##### color

color(light: int, color: int) -> None

Modifica il colore di una luce sull’hub.

```
from hub import light
import color

# Cambia la luce in rosso 
light.color(light.POWER, color.RED)
```

###### Parametri

___

###### light: int

Luce sull'hub

###### color: int

Un colore del modulo `color`

##### Costanti

___

##### hub.light Costanti

**POWER** = 0  
Pulsante di accensione. Su SPIKE Prime è il pulsante tra i pulsanti sinistro e destro.  
**CONNECT** = 1  
Luce attorno al pulsante di connessione Bluetooth su SPIKE Prime.

#### Matrice luce

Per utilizzare il modulo Matrice luce, aggiungi la seguente istruzione di importazione al progetto:

```
from hub import light_matrix
```

Tutte le funzioni del modulo devono essere chiamate all'interno del modulo `light_matrix` come prefisso nel modo seguente:

```
light_matrix.write("Hello World")
```

##### Funzioni

##### clear

clear() -> None

Disattiva tutti i pixel sulla matrice luce

```
from hub import light_matrix
import time
# Aggiorna i pixel per mostrare un'immagine sulla matrice luce, quindi disattivali utilizzando la funzione clear 

# Mostra un cuoricino 
light_matrix.show_image(2)

# Attendi due secondi 
time.sleep_ms(2000)

# Spegni il cuore 
light_matrix.clear()
```

###### Parametri

___

##### get\_orientation

get\_orientation() -> int

Recupera l'orientamento corrente della matrice luce.  
Può essere utilizzato con le seguenti costanti: `orientation.UP`, `orientation.LEFT`, `orientation.RIGHT`, `orientation.DOWN`

###### Parametri

___

##### get\_pixel

get\_pixel(x: int, y: int) -> int

Recupera l'intensità di un pixel specifico sulla matrice luce.

```
from hub import light_matrix

# Mostra un cuore 
light_matrix.show_image(1)

# Stampa il valore dell'intensità del pixel centrale 
print(light_matrix.get_pixel(2, 2))

```

###### Parametri

___

###### x: int

Il valore X, intervallo (0 - 4)

###### y: int

Il valore Y, intervallo (0 - 4)

##### set\_orientation

set\_orientation(top: int) -> int

Modifica l'orientamento della matrice luce. Tutte le chiamate successive utilizzeranno il nuovo orientamento.  
Può essere utilizzato con le seguenti costanti: `orientation.UP`, `orientation.LEFT`, `orientation.RIGHT`, `orientation.DOWN`

###### Parametri

___

###### top: int

Lato dell'hub da impostare come superiore

##### set\_pixel

set\_pixel(x: int, y: int, intensity: int) -> None

Imposta la luminosità di un pixel (uno dei 25 LED) sulla matrice luce.

```
from hub import light_matrix
# Attiva il pixel al centro dell'hub 
light_matrix.set_pixel(2, 2, 100)
```

###### Parametri

___

###### x: int

Il valore X, intervallo (0 - 4)

###### y: int

Il valore Y, intervallo (0 - 4)

###### intensity: int

Quanto illuminare il pixel

##### show

show(pixels: list\[int\]) -> None

Cambia tutte le luci contemporaneamente.

```
from hub import light_matrix
# Aggiorna tutti i pixel sulla matrice luce usando la funzione show 

# Crea un elenco con 25 valori di intensità identici 
pixels = [100] * 25 

# Aggiorna tutti i pixel per mostrare la stessa intensità 
light_matrix.show(pixels)
```

###### Parametri

___

###### pixels: Iterable

Un elenco contenente i valori di intensità luce per tutti i 25 pixel.

##### show\_image

show\_image(image: int) -> None

Visualizza una delle immagini integrate sul display.

```
from hub import light_matrix
# Aggiorna i pixel per mostrare un'immagine sulla matrice luce usando la funzione show_image 

# Mostra una faccina sorridente 
light_matrix.show_image(light_matrix.IMAGE_HAPPY)
```

###### Parametri

___

###### image: int

ID dell’immagine da mostrare. La gamma di immagini disponibili è compresa tra 1 e 67. Sono presenti costanti sul modulo `light_matrix` per queste.

##### write

write(text: str, intensity: int = 100, time\_per\_character: int = 500) -> Awaitable

Visualizza il testo sulla Matrice luce, una lettera alla volta, scorrendo da destra a sinistra, tranne nel caso in cui sia presente un singolo carattere da visualizzare, il quale non scorrerà

```
from hub import light_matrix
# Scrivi un messaggio nell'hub 
light_matrix.write("Hello, world!")
```

###### Parametri

___

###### text: str

Testo da visualizzare

###### intensity: int

Quanto illuminare il pixel

###### time\_per\_character: int

Durata della visualizzazione di ogni carattere sul display

##### Costanti

___

##### hub.light\_matrix Costanti

**IMAGE\_HEART** = 1

**IMAGE\_HEART\_SMALL** = 2

**IMAGE\_HAPPY** = 3

**IMAGE\_SMILE** = 4

**IMAGE\_SAD** = 5

**IMAGE\_CONFUSED** = 6

**IMAGE\_ANGRY** = 7

**IMAGE\_ASLEEP** = 8

**IMAGE\_SURPRISED** = 9

**IMAGE\_SILLY** = 10

**IMAGE\_FABULOUS** = 11

**IMAGE\_MEH** = 12

**IMAGE\_YES** = 13

**IMAGE\_NO** = 14

**IMAGE\_CLOCK12** = 15

**IMAGE\_CLOCK1** = 16

**IMAGE\_CLOCK2** = 17

**IMAGE\_CLOCK3** = 18

**IMAGE\_CLOCK4** = 19

**IMAGE\_CLOCK5** = 20

**IMAGE\_CLOCK6** = 21

**IMAGE\_CLOCK7** = 22

**IMAGE\_CLOCK8** = 23

**IMAGE\_CLOCK9** = 24

**IMAGE\_CLOCK10** = 25

**IMAGE\_CLOCK11** = 26

**IMAGE\_ARROW\_N** = 27

**IMAGE\_ARROW\_NE** = 28

**IMAGE\_ARROW\_E** = 29

**IMAGE\_ARROW\_SE** = 30

**IMAGE\_ARROW\_S** = 31

**IMAGE\_ARROW\_SW** = 32

**IMAGE\_ARROW\_W** = 33

**IMAGE\_ARROW\_NW** = 34

**IMAGE\_GO\_RIGHT** = 35

**IMAGE\_GO\_LEFT** = 36

**IMAGE\_GO\_UP** = 37

**IMAGE\_GO\_DOWN** = 38

**IMAGE\_TRIANGLE** = 39

**IMAGE\_TRIANGLE\_LEFT** = 40

**IMAGE\_CHESSBOARD** = 41

**IMAGE\_DIAMOND** = 42

**IMAGE\_DIAMOND\_SMALL** = 43

**IMAGE\_SQUARE** = 44

**IMAGE\_SQUARE\_SMALL** = 45

**IMAGE\_RABBIT** = 46

**IMAGE\_COW** = 47

**IMAGE\_MUSIC\_CROTCHET** = 48

**IMAGE\_MUSIC\_QUAVER** = 49

**IMAGE\_MUSIC\_QUAVERS** = 50

**IMAGE\_PITCHFORK** = 51

**IMAGE\_XMAS** = 52

**IMAGE\_PACMAN** = 53

**IMAGE\_TARGET** = 54

**IMAGE\_TSHIRT** = 55

**IMAGE\_ROLLERSKATE** = 56

**IMAGE\_DUCK** = 57

**IMAGE\_HOUSE** = 58

**IMAGE\_TORTOISE** = 59

**IMAGE\_BUTTERFLY** = 60

**IMAGE\_STICKFIGURE** = 61

**IMAGE\_GHOST** = 62

**IMAGE\_SWORD** = 63

**IMAGE\_GIRAFFE** = 64

**IMAGE\_SKULL** = 65

**IMAGE\_UMBRELLA** = 66

**IMAGE\_SNAKE** = 67

#### Sensore di movimento

Per utilizzare il modulo Sensore di movimento, aggiungi la seguente istruzione di importazione al progetto:

```
from hub import motion_sensor
```

Tutte le funzioni del modulo devono essere chiamate all'interno del modulo `motion_sensor` come prefisso nel modo seguente:

```
motion_sensor.up_face()
```

##### Funzioni

##### acceleration

acceleration(raw\_unfiltered: bool) -> tuple\[int, int, int\]

Restituisce una tupla contenente i valori di accelerazione x, y e z come numeri interi. I valori sono in milligrammi, quindi 1/1.000 di grammo

###### Parametri

___

###### raw\_unfiltered: bool

Se vogliamo che i dati tornino raw e non filtrati

##### angular\_velocity

angular\_velocity(raw\_unfiltered: bool) -> tuple\[int, int, int\]

Restituisce una tupla contenente i valori di velocità angolare x, y e z come numeri interi. I valori sono decigradi al secondo

###### Parametri

___

###### raw\_unfiltered: bool

Se vogliamo che i dati tornino raw e non filtrati

##### gesture

gesture() -> int

Restituisce il gesto riconosciuto.

I valori possibili sono:

`motion_sensor.TAPPED`  
`motion_sensor.DOUBLE_TAPPED`  
`motion_sensor.SHAKEN`  
`motion_sensor.FALLING`  
`motion_sensor.UNKNOWN`

###### Parametri

___

##### get\_yaw\_face

get\_yaw\_face() -> int

Recupera il lato dell’hub a cui è relativa l’imbardata.  
Se si appoggia l’hub su una superficie piana con il lato rivolto verso l’alto, quando si ruota l’hub si aggiorna solo l’imbardata.  
`motion_sensor.TOP` Lato dell’hub SPIKE Prime con porta di ricarica USB.  
`motion_sensor.FRONT` Lato dell’hub SPIKE Prime con Matrice luce.  
`motion_sensor.RIGHT` Lato destro dell’hub SPIKE Prime rivolto verso il lato anteriore dell’hub.  
`motion_sensor.BOTTOM` Lato dell’hub SPIKE Prime in cui si trova la batteria.  
`motion_sensor.BACK` Lato dell’hub SPIKE Prime in cui si trova l’altoparlante.  
`motion_sensor.LEFT` Lato sinistro dell’hub SPIKE Prime rivolto verso il lato anteriore dell’hub.

###### Parametri

___

##### quaternion

quaternion() -> tuple\[float, float, float, float\]

Restituisce il quaternione di orientamento dell’hub come tuple\[w: float, x: float, y: float, z: float\].

###### Parametri

___

##### reset\_tap\_count

reset\_tap\_count() -> None

Reimposta il conteggio dei tocchi restituito dalla funzione `tap_count`

###### Parametri

___

##### reset\_yaw

reset\_yaw(angle: int) -> None

Modifica l'offset dell'angolo di imbardata.  
L'angolo impostato sarà il nuovo valore di imbardata.

###### Parametri

___

###### angle: int

##### set\_yaw\_face

set\_yaw\_face(up: int) -> bool

Modifica il lato dell’hub utilizzato come lato di imbardata. Se si posiziona l’hub su una superficie piana con questo lato rivolto verso l’alto, quando si ruota l’hub solo l’imbardata si aggiornerà

###### Parametri

___

###### up: int

Lato dell'hub che deve essere rivolto verso l'alto.  
I valori disponibili sono:

`motion_sensor.TOP` Lato dell'hub SPIKE Prime con porta di ricarica USB.  
`motion_sensor.FRONT` Lato dell'hub SPIKE Prime con Matrice luce.  
`motion_sensor.RIGHT` Lato destro dell'hub SPIKE Prime rivolto verso il lato anteriore dell'hub.  
`motion_sensor.BOTTOM` Lato dell'hub SPIKE Prime in cui si trova la batteria.  
`motion_sensor.BACK` Lato dell'hub SPIKE Prime in cui si trova l'altoparlante.  
`motion_sensor.LEFT` Lato sinistro dell'hub SPIKE Prime rivolto verso il lato anteriore dell'hub.

##### stable

stable() -> bool

Se l’hub è in piano o meno.

###### Parametri

___

##### tap\_count

tap\_count() -> int

Restituisce il numero di tocchi riconosciuti dall’avvio del programma o dall’ultima volta che `motion_sensor.reset_tap_count()` è stato chiamato.

###### Parametri

___

##### tilt\_angles

tilt\_angles() -> tuple\[int, int, int\]

Restituisce una tupla contenente valori di imbardata e rollio come numeri interi. I valori sono decigradi

###### Parametri

___

##### up\_face

up\_face() -> int

Restituisce il lato dell'hub attualmente rivolto verso l'alto  
`motion_sensor.TOP` Lato dell’hub SPIKE Prime con porta di ricarica USB.  
`motion_sensor.FRONT` Lato dell’hub SPIKE Prime con Matrice luce.  
`motion_sensor.RIGHT` Lato destro dell’hub SPIKE Prime rivolto verso il lato anteriore dell’hub.  
`motion_sensor.BOTTOM` Lato dell’hub SPIKE Prime in cui si trova la batteria.  
`motion_sensor.BACK` Lato dell’hub SPIKE Prime in cui si trova l’altoparlante.  
`motion_sensor.LEFT` Lato sinistro dell’hub SPIKE Prime rivolto verso il lato anteriore dell’hub.

###### Parametri

___

##### Costanti

___

##### hub.motion\_sensor Costanti

**TAPPED** = 0

**DOUBLE\_TAPPED** = 1

**SHAKEN** = 2

**FALLING** = 3

**UNKNOWN** = -1

**TOP** = 0  
Lato dell'hub SPIKE Prime con Matrice luce.  
**FRONT** = 1  
Lato dell'hub SPIKE Prime in cui si trova l'altoparlante.  
**RIGHT** = 2  
Lato destro dell'hub SPIKE Prime rivolto verso il lato anteriore dell'hub.  
**BOTTOM** = 3  
Lato dell'hub SPIKE Prime in cui si trova la batteria.  
**BACK** = 4  
Lato dell'hub SPIKE Prime con porta di ricarica USB.  
**LEFT** = 5  
Lato sinistro dell'hub SPIKE Prime rivolto verso il lato anteriore dell'hub.

#### Porta

Questo modulo contiene costanti che consentono di accedere facilmente alle porte sull'hub SPIKE Prime. Utilizza le costanti in tutte le funzioni che accettano un parametro `port`.

Per utilizzare il modulo Porta, aggiungi la seguente istruzione di importazione al progetto:

```
from hub import port
```

Tutte le funzioni del modulo devono essere chiamate all'interno del modulo `port` come prefisso nel modo seguente:

```
port.A
```

##### Costanti

___

##### hub.port Costanti

**A** = 0  
La porta con l'etichetta "A" sull'Hub.  
**B** = 1  
La porta con l'etichetta "B" sull'Hub.  
**C** = 2  
La porta con l'etichetta "C" sull'Hub.  
**D** = 3  
La porta con l'etichetta "D" sull'Hub.  
**E** = 4  
La porta con l'etichetta "E" sull'Hub.  
**F** = 5  
La porta con l'etichetta "F" sull'Hub.

#### Altoparlante

Per utilizzare il modulo Altoparlante, aggiungi la seguente istruzione di importazione al progetto:

```
from hub import sound
```

Tutte le funzioni del modulo devono essere chiamate all'interno del modulo `sound` come prefisso nel modo seguente:

```
sound.stop()
```

##### Funzioni

##### beep

beep(frequency: int = 440, duration: int = 500, volume: int = 100, \*, attack: int = 0, decay: int = 0, sustain: int = 100, release: int = 0, transition: int = 10, waveform: int = WAVEFORM\_SINE, channel: int = DEFAULT) -> Awaitable

Riproduce un segnale acustico dall'hub

###### Parametri

___

###### frequency: int

Frequenza di riproduzione

###### duration: int

Durata in millisecondi.

###### volume: int

Volume (0-100)

###### Argomenti facoltativi delle parole chiave:

###### attack: int

Tempo impiegato per aumentare il livello da zero al picco, a partire da quando viene premuto il tasto.

###### decay: int

Tempo impiegato per diminuire livello di attack al livello di sustain designato.

###### sustain: int

Livello durante la sequenza principale della durata del suono, fino al rilascio del tasto.

###### release: int

Tempo impiegato per far decadere il livello di sustain a zero dopo il rilascio del tasto

###### transition: int

tempo in millisecondi per passare al suono se qualcosa è già in riproduzione nel canale

###### waveform: int

Forma d'onda sintetizzata. Utilizza una delle costanti nel modulo `hub.sound`.

###### channel: int

Il canale desiderato su cui giocare, le opzioni sono `sound.DEFAULT` e `sound.ANY`

##### stop

stop() -> None

Blocca tutti i rumori dall'hub

###### Parametri

___

##### volume

volume(volume: int) -> None

###### Parametri

___

###### volume: int

Volume (0-100)

##### Costanti

___

##### hub.sound Costanti

**ANY** = -2

**DEFAULT** = -1

**WAVEFORM\_SINE** = 1

**WAVEFORM\_SAWTOOTH** = 3

**WAVEFORM\_SQUARE** = 2

**WAVEFORM\_TRIANGLE** = 1

#### Funzioni

#### device\_uuid

device\_uuid() -> str

Recupera l'ID dispositivo.

##### Parametri

___

#### hardware\_id

hardware\_id() -> str

Recupera l'ID hardware.

##### Parametri

___

#### power\_off

power\_off() -> int

Spegne l'hub.

##### Parametri

___

#### temperature

temperature() -> int

Recupera la temperatura dell'hub. Misurato in decigradi Celsius (d°C), che equivale a 1/10 di grado Celsius (°C)

##### Parametri

___

### Motore

Per utilizzare un motore, aggiungi la seguente istruzione di importazione al progetto:

```
import motor
```

Tutte le funzioni del modulo devono essere chiamate all'interno del modulo `motor` come prefisso nel modo seguente:

```
motor.run(port.A, 1000)
```

#### Funzioni

#### absolute\_position

absolute\_position(port: int) -> int

Ottieni la posizione assoluta di un motore

##### Parametri

___

##### port: int

Una porta del modulo secondario `port` nel modulo `hub`

#### get\_duty\_cycle

get\_duty\_cycle(port: int) -> int

Ottieni la pwm di un motore

##### Parametri

___

##### port: int

Una porta del modulo secondario `port` nel modulo `hub`

#### relative\_position

relative\_position(port: int) -> int

Ottieni la posizione relativa di un motore

##### Parametri

___

##### port: int

Una porta del modulo secondario `port` nel modulo `hub`

#### reset\_relative\_position

reset\_relative\_position(port: int, position: int) -> None

Modifica la posizione utilizzata come offset quando utilizzi la funzione `run_to_relative_position`.

##### Parametri

___

##### port: int

Una porta del modulo secondario `port` nel modulo `hub`

##### position: int

Grado del motore

#### run

run(port: int, velocity: int, \*, acceleration: int = 1000) -> None

Avvia un motore a velocità costante

```
from hub import port
import motor, time

# Avvia motore 
motor.run(port.A, 1000)

```

##### Parametri

___

##### port: int

Una porta del modulo secondario `port` nel modulo `hub`

##### velocity: int

La velocità in gradi/sec

Gli intervalli del valore dipendono dal tipo di motore.

Motore piccolo (essenziale): da -660 a 660  
Motore medio: da -1.110 a 1.110  
Motore grande: da -1.050 a 1.050

##### Argomenti facoltativi delle parole chiave:

##### acceleration: int

L’accelerazione (gradi/sec²) (0 - 10.000)

#### run\_for\_degrees

run\_for\_degrees(port: int, degrees: int, velocity: int, \*, stop: int = BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable

Fai girare un motore per un numero specifico di gradi  
Quando “awaiter” restituisce uno stato del movimento che corrisponde a una delle seguenti costanti:

`motor.READY`  
`motor.RUNNING`  
`motor.STALLED`  
`motor.CANCELED`  
`motor.ERROR`  
`motor.DISCONNECTED`

##### Parametri

___

##### port: int

Una porta del modulo secondario `port` nel modulo `hub`

##### degrees: int

Numero di gradi

##### velocity: int

La velocità in gradi/sec

Gli intervalli del valore dipendono dal tipo di motore.

Motore piccolo (essenziale): da -660 a 660  
Motore medio: da -1.110 a 1.110  
Motore grande: da -1.050 a 1.050

##### Argomenti facoltativi delle parole chiave:

##### stop: int

Comportamento del motore dopo che si è arrestato. Utilizza le costanti nel modulo `motor`.

I valori possibili sono  
`motor.COAST` per muovere il motore a inerzia fino all’arresto  
`motor.BREAK` per frenare e continuare a frenare dopo l’arresto  
`motor.HOLD` per dire al motore di mantenere la sua posizione  
`motor.CONTINUE` per dire al motore di continuare a funzionare a qualsiasi velocità stia funzionando fino a quando non riceve un altro comando  
`motor.SMART_COAST` per far frenare il motore fino all’arresto e quindi muoversi a inerzia, compensando le imprecisioni nel comando successivo  
`motor.SMART_BRAKE` per far frenare il motore e continuare a frenare dopo l’arresto e compensare le imprecisioni nel comando successivo

##### acceleration: int

L’accelerazione (gradi/sec²) (0 - 10.000)

##### deceleration: int

La decelerazione (gradi/sec²) (0 - 10.000)

#### run\_for\_time

run\_for\_time(port: int, duration: int, velocity: int, \*, stop: int = BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable

Aziona un motore per un intervallo di tempo limitato  
Quando “await” restituisce uno stato del movimento che corrisponde a una delle seguenti costanti:

`motor.READY`  
`motor.RUNNING`  
`motor.STALLED`  
`motor.ERROR`  
`motor.DISCONNECTED`

```
from hub import port
import runloop
import motor

async def main():
    # Corri a una velocità 1.000 per 1 secondo 
    await motor.run_for_time(port.A, 1000, 1000)

    # Corri a una velocità 280 per 1 secondo 
    await motor_pair.run_for_time(port.A, 1000, 280)

    # Esegui a una velocità 280 per 10 secondi con una decelerazione lenta 
    await motor_pair.run_for_time(port.A, 10000, 280, deceleration=10)

runloop.run(main())
```

##### Parametri

___

##### port: int

Una porta del modulo secondario `port` nel modulo `hub`

##### duration: int

Durata in millisecondi.

##### velocity: int

La velocità in gradi/sec

Gli intervalli del valore dipendono dal tipo di motore.

Motore piccolo (essenziale): da -660 a 660  
Motore medio: da -1.110 a 1.110  
Motore grande: da -1.050 a 1.050

##### Argomenti facoltativi delle parole chiave:

##### stop: int

Comportamento del motore dopo che si è arrestato. Utilizza le costanti nel modulo `motor`.

I valori possibili sono  
`motor.COAST` per muovere il motore a inerzia fino all’arresto  
`motor.BREAK` per frenare e continuare a frenare dopo l’arresto  
`motor.HOLD` per dire al motore di mantenere la sua posizione  
`motor.CONTINUE` per dire al motore di continuare a funzionare a qualsiasi velocità stia funzionando fino a quando non riceve un altro comando  
`motor.SMART_COAST` per far frenare il motore fino all’arresto e quindi muoversi a inerzia, compensando le imprecisioni nel comando successivo  
`motor.SMART_BRAKE` per far frenare il motore e continuare a frenare dopo l’arresto e compensare le imprecisioni nel comando successivo

##### acceleration: int

L’accelerazione (gradi/sec²) (0 - 10.000)

##### deceleration: int

La decelerazione (gradi/sec²) (0 - 10.000)

#### run\_to\_absolute\_position

run\_to\_absolute\_position(port: int, position: int, velocity: int, \*, direction: int, stop: int = BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable

Fai girare un motore in una posizione assoluta.  
Quando “await” restituisce uno stato del movimento che corrisponde a una delle seguenti costanti:

`motor.READY`  
`motor.RUNNING`  
`motor.STALLED`  
`motor.CANCELED`  
`motor.ERROR`  
`motor.DISCONNECTED`

##### Parametri

___

##### port: int

Una porta del modulo secondario `port` nel modulo `hub`

##### position: int

Grado del motore

##### velocity: int

La velocità in gradi/sec

Gli intervalli del valore dipendono dal tipo di motore.

Motore piccolo (essenziale): da -660 a 660  
Motore medio: da -1.110 a 1.110  
Motore grande: da -1.050 a 1.050

##### Argomenti facoltativi delle parole chiave:

##### direction: int

La direzione in cui svoltare.  
Le opzioni sono:

`motor.CLOCKWISE`  
`motor.COUNTERCLOCKWISE`  
`motor.SHORTEST_PATH`  
`motor.LONGEST_PATH`

##### stop: int

Comportamento del motore dopo che si è arrestato. Utilizza le costanti nel modulo `motor`.

I valori possibili sono  
`motor.COAST` per muovere il motore a inerzia fino all’arresto  
`motor.BREAK` per frenare e continuare a frenare dopo l’arresto  
`motor.HOLD` per dire al motore di mantenere la sua posizione  
`motor.CONTINUE` per dire al motore di continuare a funzionare a qualsiasi velocità stia funzionando fino a quando non riceve un altro comando  
`motor.SMART_COAST` per far frenare il motore fino all’arresto e quindi muoversi a inerzia, compensando le imprecisioni nel comando successivo  
`motor.SMART_BRAKE` per far frenare il motore e continuare a frenare dopo l’arresto e compensare le imprecisioni nel comando successivo

##### acceleration: int

L’accelerazione (gradi/sec²) (0 - 10.000)

##### deceleration: int

La decelerazione (gradi/sec²) (0 - 10.000)

#### run\_to\_relative\_position

run\_to\_relative\_position(port: int, position: int, velocity: int, \*, stop: int = BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable

Fai girare un motore in una posizione relativa alla posizione corrente.  
Quando “await” restituisce uno stato del movimento che corrisponde a una delle seguenti costanti:

`motor.READY`  
`motor.RUNNING`  
`motor.STALLED`  
`motor.CANCELED`  
`motor.ERROR`  
`motor.DISCONNECTED`

##### Parametri

___

##### port: int

Una porta del modulo secondario `port` nel modulo `hub`

##### position: int

Grado del motore

##### velocity: int

La velocità in gradi/sec

Gli intervalli del valore dipendono dal tipo di motore.

Motore piccolo (essenziale): da -660 a 660  
Motore medio: da -1.110 a 1.110  
Motore grande: da -1.050 a 1.050

##### Argomenti facoltativi delle parole chiave:

##### stop: int

Comportamento del motore dopo che si è arrestato. Utilizza le costanti nel modulo `motor`.

I valori possibili sono  
`motor.COAST` per muovere il motore a inerzia fino all’arresto  
`motor.BREAK` per frenare e continuare a frenare dopo l’arresto  
`motor.HOLD` per dire al motore di mantenere la sua posizione  
`motor.CONTINUE` per dire al motore di continuare a funzionare a qualsiasi velocità stia funzionando fino a quando non riceve un altro comando  
`motor.SMART_COAST` per far frenare il motore fino all’arresto e quindi muoversi a inerzia, compensando le imprecisioni nel comando successivo  
`motor.SMART_BRAKE` per far frenare il motore e continuare a frenare dopo l’arresto e compensare le imprecisioni nel comando successivo

##### acceleration: int

L’accelerazione (gradi/sec²) (0 - 10.000)

##### deceleration: int

La decelerazione (gradi/sec²) (0 - 10.000)

#### set\_duty\_cycle

set\_duty\_cycle(port: int, pwm: int) -> None

Avvia un motore con una pwm specifica

##### Parametri

___

##### port: int

Una porta del modulo secondario `port` nel modulo `hub`

##### pwm: int

Valore PWM (-10.000-10.000)

#### stop

stop(port: int, \*, stop: int = BRAKE) -> None

Arresta un motore

```
from hub import port
import motor, time

# Avvia motore 
motor.run(port.A, 1000)

# Attendi per 2 secondi 
time.sleep_ms(2000)

# Arresta motore 
motor.stop(port.A)
```

##### Parametri

___

##### port: int

Una porta del modulo secondario `port` nel modulo `hub`

##### Argomenti facoltativi delle parole chiave:

##### stop: int

Comportamento del motore dopo che si è arrestato. Utilizza le costanti nel modulo `motor`.

I valori possibili sono  
`motor.COAST` per muovere il motore a inerzia fino all’arresto  
`motor.BREAK` per frenare e continuare a frenare dopo l’arresto  
`motor.HOLD` per dire al motore di mantenere la sua posizione  
`motor.CONTINUE` per dire al motore di continuare a funzionare a qualsiasi velocità stia funzionando fino a quando non riceve un altro comando  
`motor.SMART_COAST` per far frenare il motore fino all’arresto e quindi muoversi a inerzia, compensando le imprecisioni nel comando successivo  
`motor.SMART_BRAKE` per far frenare il motore e continuare a frenare dopo l’arresto e compensare le imprecisioni nel comando successivo

#### velocity

velocity(port: int) -> int

Ottiene la velocità (m/sec) di un motore

##### Parametri

___

##### port: int

Una porta del modulo secondario `port` nel modulo `hub`

#### Costanti

___

#### motor Costanti

**READY** = 1

**RUNNING** = 2

**STALLED** = -1

**CANCELED** = -2

**ERROR** = -3

**DISCONNECTED** = 0

**COAST** = 1

**BRAKE** = 2

**HOLD** = 3

**CONTINUE** = 0

**SMART\_COAST** = 4

**SMART\_BRAKE** = 5

**CLOCKWISE** = 0

**COUNTERCLOCKWISE** = 1

**SHORTEST\_PATH** = 2

**LONGEST\_PATH** = 3

### Coppia di motori

Il modulo `motor_pair` viene utilizzato per azionare i motori in modo sincronizzato. Questa modalità è ottimale per creare strutture motrici dove poter avviare o arrestare una coppia di motori contemporaneamente.

Per utilizzare il modulo `motor_pair`, è sufficiente importarlo nel modo seguente:

```
import motor_pair
```

Tutte le funzioni del modulo devono essere chiamate all'interno del modulo `motor_pair` come prefisso nel modo seguente:

```
motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)
```

#### Funzioni

#### move

move(pair: int, steering: int, \*, velocity: int = 360, acceleration: int = 1000) -> None

Sposta una coppia di motori a velocità costante fino a quando non viene impartito un nuovo comando.

```
from hub import port
import runloop
import motor_pair

async def main():
    # Accoppia motori sulle porte A e B 
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

    await runloop.sleep_ms(2000)

    # Spostati in avanti alla velocità predefinita 
    motor_pair.move(motor_pair.PAIR_1, 0)

    await runloop.sleep_ms(2000)

    # Spostati in avanti a una velocità specifica 
    motor_pair.move(motor_pair.PAIR_1, 0, velocity=280)

    await runloop.sleep_ms(2000)

    # Spostati in avanti a una velocità e un'accelerazione specifiche 
    motor_pair.move(motor_pair.PAIR_1, 0, velocity=280, acceleration=100)

runloop.run(main())
```

##### Parametri

___

##### pair: int

Slot di coppia della coppia di motori.

##### steering: int

Sterzata (da -100 a 100)

##### Argomenti facoltativi delle parole chiave:

##### velocity: int

La velocità in gradi/sec

Gli intervalli del valore dipendono dal tipo di motore.

Motore piccolo (essenziale): da -660 a 660  
Motore medio: da -1.110 a 1.110  
Motore grande: da -1.050 a 1.050

##### acceleration: int

L’accelerazione (gradi/sec²) (0 - 10.000)

#### move\_for\_degrees

move\_for\_degrees(pair: int, degrees: int, steering: int, \*, velocity: int = 360, stop: int = motor.BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable

Sposta una coppia di motori a velocità costante per un numero specifico di gradi.  
Quando “awaiter” restituisce uno stato del movimento che corrisponde a una delle seguenti costanti dal modulo motore:

`motor.READY`  
`motor.RUNNING`  
`motor.STALLED`  
`motor.CANCELED`  
`motor.ERROR`  
`motor.DISCONNECTED`

```
from hub import port
import runloop
import motor_pair

async def main():
    # Accoppia motori sulle porte A e B 
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

    # Spostati in avanti alla velocità predefinita per 90 gradi 
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 90, 0)

    # Spostati in avanti a una velocità specifica 
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 360, 0, velocity=280)

    # Spostati in avanti a una velocità specifica con una decelerazione lenta 
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 360, 0, velocity=280, deceleration=10)

runloop.run(main())
```

##### Parametri

___

##### pair: int

Slot di coppia della coppia di motori.

##### degrees: int

Numero di gradi

##### steering: int

Sterzata (da -100 a 100)

##### Argomenti facoltativi delle parole chiave:

##### velocity: int

La velocità in gradi/sec

Gli intervalli del valore dipendono dal tipo di motore.

Motore piccolo (essenziale): da -660 a 660  
Motore medio: da -1.110 a 1.110  
Motore grande: da -1.050 a 1.050

##### stop: int

Comportamento del motore dopo che si è arrestato. Utilizza le costanti nel modulo `motor`.

I valori possibili sono  
`motor.COAST` per muovere il motore a inerzia fino all’arresto  
`motor.BREAK` per frenare e continuare a frenare dopo l’arresto  
`motor.HOLD` per dire al motore di mantenere la sua posizione  
`motor.CONTINUE` per dire al motore di continuare a funzionare a qualsiasi velocità stia funzionando fino a quando non riceve un altro comando  
`motor.SMART_COAST` per far frenare il motore fino all’arresto e quindi muoversi a inerzia, compensando le imprecisioni nel comando successivo  
`motor.SMART_BRAKE` per far frenare il motore e continuare a frenare dopo l’arresto e compensare le imprecisioni nel comando successivo

##### acceleration: int

L’accelerazione (gradi/sec²) (0 - 10.000)

##### deceleration: int

La decelerazione (gradi/sec²) (0 - 10.000)

#### move\_for\_time

move\_for\_time(pair: int, duration: int, steering: int, \*, velocity: int = 360, stop: int = motor.BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable

Sposta una coppia di motori a velocità costante per una durata specifica.  
Quando “await” restituisce uno stato del movimento che corrisponde a una delle seguenti costanti dal modulo motore:

`motor.READY`  
`motor.RUNNING`  
`motor.STALLED`  
`motor.CANCELED`  
`motor.ERROR`  
`motor.DISCONNECTED`

```
from hub import port
import runloop
import motor_pair

async def main():
    # Accoppia motori sulle porte A e B 
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

    # Spostati in avanti alla velocità predefinita per 1 secondo 
    await motor_pair.move_for_time(motor_pair.PAIR_1, 1000, 0)

    # Spostati in avanti a una velocità specifica per 1 secondo 
    await motor_pair.move_for_time(motor_pair.PAIR_1, 1000, 0, velocity=280)

    # Spostati in avanti a una velocità specifica per 10 secondi con una decelerazione lenta 
    await motor_pair.move_for_time(motor_pair.PAIR_1, 10000, 0, velocity=280, deceleration=10)

runloop.run(main())
```

##### Parametri

___

##### pair: int

Slot di coppia della coppia di motori.

##### duration: int

Durata in millisecondi.

##### steering: int

Sterzata (da -100 a 100)

##### Argomenti facoltativi delle parole chiave:

##### velocity: int

La velocità in gradi/sec

Gli intervalli del valore dipendono dal tipo di motore.

Motore piccolo (essenziale): da -660 a 660  
Motore medio: da -1.110 a 1.110  
Motore grande: da -1.050 a 1.050

##### stop: int

Comportamento del motore dopo che si è arrestato. Utilizza le costanti nel modulo `motor`.

I valori possibili sono  
`motor.COAST` per muovere il motore a inerzia fino all’arresto  
`motor.BREAK` per frenare e continuare a frenare dopo l’arresto  
`motor.HOLD` per dire al motore di mantenere la sua posizione  
`motor.CONTINUE` per dire al motore di continuare a funzionare a qualsiasi velocità stia funzionando fino a quando non riceve un altro comando  
`motor.SMART_COAST` per far frenare il motore fino all’arresto e quindi muoversi a inerzia, compensando le imprecisioni nel comando successivo  
`motor.SMART_BRAKE` per far frenare il motore e continuare a frenare dopo l’arresto e compensare le imprecisioni nel comando successivo

##### acceleration: int

L’accelerazione (gradi/sec²) (0 - 10.000)

##### deceleration: int

La decelerazione (gradi/sec²) (0 - 10.000)

#### move\_tank

move\_tank(pair: int, left\_velocity: int, right\_velocity: int, \*, acceleration: int = 1000) -> None

Esegui un movimento tipo cingolato su una coppia di motori a velocità costante fino a quando non viene impartito un nuovo comando.

```
from hub import port
import runloop
import motor_pair

async def main():
    # Accoppia motori sulle porte A e B 
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

    # Spostati in avanti alla velocità predefinita 
    motor_pair.move_tank(motor_pair.PAIR_1, 1000, 1000)

    await runloop.sleep_ms(2000)

    # Gira a destra 
    motor_pair.move_tank(motor_pair.PAIR_1, 0, 1000)

    await runloop.sleep_ms(2000)

    # Svolta con movimento tipo cingolato 
    motor_pair.move_tank(motor_pair.PAIR_1, 1000, -1000)

runloop.run(main())
```

##### Parametri

___

##### pair: int

Slot di coppia della coppia di motori.

##### left\_velocity: int

Velocità (grado/sec) del motore sinistro.

##### right\_velocity: int

La velocità (grado/sec) del motore destro.

##### Argomenti facoltativi delle parole chiave:

##### acceleration: int

L’accelerazione (gradi/sec²) (0 - 10.000)

#### move\_tank\_for\_degrees

move\_tank\_for\_degrees(pair: int, degrees: int, left\_velocity: int, right\_velocity: int, \*, stop: int = motor.BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable

Esegui un movimento tipo cingolato su una coppia di motori a velocità costante fino a quando non viene impartito un nuovo comando.  
Quando “await” restituisce uno stato del movimento che corrisponde a una delle seguenti costanti dal modulo motore:

`motor.READY`  
`motor.RUNNING`  
`motor.STALLED`  
`motor.CANCELED`  
`motor.ERROR`  
`motor.DISCONNECTED`

```
from hub import port
import runloop
import motor_pair

async def main():
    # Accoppia motori sulle porte A e B 
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

    # Spostati in avanti alla velocità predefinita per 360 gradi 
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 360, 1000, 1000)

    # Gira a destra per 180 gradi 
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 180, 0, 1000)

    # Svolta con movimento tipo cingolato per 720 gradi 
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 720, 1000, -1000)

runloop.run(main())
```

##### Parametri

___

##### pair: int

Slot di coppia della coppia di motori.

##### degrees: int

Numero di gradi

##### left\_velocity: int

Velocità (grado/sec) del motore sinistro.

##### right\_velocity: int

La velocità (grado/sec) del motore destro.

##### Argomenti facoltativi delle parole chiave:

##### stop: int

Comportamento del motore dopo che si è arrestato. Utilizza le costanti nel modulo `motor`.

I valori possibili sono  
`motor.COAST` per muovere il motore a inerzia fino all’arresto  
`motor.BREAK` per frenare e continuare a frenare dopo l’arresto  
`motor.HOLD` per dire al motore di mantenere la sua posizione  
`motor.CONTINUE` per dire al motore di continuare a funzionare a qualsiasi velocità stia funzionando fino a quando non riceve un altro comando  
`motor.SMART_COAST` per far frenare il motore fino all’arresto e quindi muoversi a inerzia, compensando le imprecisioni nel comando successivo  
`motor.SMART_BRAKE` per far frenare il motore e continuare a frenare dopo l’arresto e compensare le imprecisioni nel comando successivo

##### acceleration: int

L’accelerazione (gradi/sec²) (0 - 10.000)

##### deceleration: int

La decelerazione (gradi/sec²) (0 - 10.000)

#### move\_tank\_for\_time

move\_tank\_for\_time(pair: int, left\_velocity: int, right\_velocity: int, duration: int, \*, stop: int = motor.BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable

Esegui un movimento tipo cingolato su una di motori a velocità costante per un intervallo di tempo specifico.  
Quando “await” restituisce uno stato del movimento che corrisponde a una delle seguenti costanti dal modulo motore:

`motor.READY`  
`motor.RUNNING`  
`motor.STALLED`  
`motor.CANCELLED`  
`motor.ERROR`  
`motor.DISCONNECTED`

```
from hub import port
import runloop
import motor_pair

async def main():
    # Accoppia motori sulle porte A e B 
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

    # Spostati in avanti alla velocità predefinita per 1 secondo 
    await motor_pair.move_tank_for_time(motor_pair.PAIR_1, 1000, 1000, 1000)

    # Gira a destra per 3 secondi 
    await motor_pair.move_tank_for_time(motor_pair.PAIR_1, 0, 1000, 3000)

    # Svolta con movimento tipo cingolato per 2 secondi 
    await motor_pair.move_tank_for_time(motor_pair.PAIR_1, 1000, -1000, 2000)

runloop.run(main())
```

##### Parametri

___

##### pair: int

Slot di coppia della coppia di motori.

##### duration: int

Durata in millisecondi.

##### left\_velocity: int

Velocità (grado/sec) del motore sinistro.

##### right\_velocity: int

La velocità (grado/sec) del motore destro.

##### Argomenti facoltativi delle parole chiave:

##### stop: int

Comportamento del motore dopo che si è arrestato. Utilizza le costanti nel modulo `motor`.

I valori possibili sono  
`motor.COAST` per muovere il motore a inerzia fino all’arresto  
`motor.BREAK` per frenare e continuare a frenare dopo l’arresto  
`motor.HOLD` per dire al motore di mantenere la sua posizione  
`motor.CONTINUE` per dire al motore di continuare a funzionare a qualsiasi velocità stia funzionando fino a quando non riceve un altro comando  
`motor.SMART_COAST` per far frenare il motore fino all’arresto e quindi muoversi a inerzia, compensando le imprecisioni nel comando successivo  
`motor.SMART_BRAKE` per far frenare il motore e continuare a frenare dopo l’arresto e compensare le imprecisioni nel comando successivo

##### acceleration: int

L’accelerazione (gradi/sec²) (0 - 10.000)

##### deceleration: int

La decelerazione (gradi/sec²) (0 - 10.000)

#### pair

pair(pair: int, left\_motor: int, right\_motor: int) -> None

Accoppia due motori (`left_motor` e `right_motor`) e memorizza i motori accoppiati in `pair`.  
Utilizza `pair` in tutte le chiamate di funzione successive correlate a `motor_pair`.

```
import motor_pair
from hub import port

motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)
```

##### Parametri

___

##### pair: int

Slot di coppia della coppia di motori.

##### left\_motor: int

Porta del motore sinistro. Utilizza il modulo secondario `port` nel modulo `hub`.

##### right\_motor: int

Porta del motore destro. Utilizza il modulo secondario `port` nel modulo `hub`.

#### stop

stop(pair: int, \*, stop: int = motor.BRAKE) -> None

Arresta una coppia di motori.

```
import motor_pair

motor_pair.stop(motor_pair.PAIR_1)
```

##### Parametri

___

##### pair: int

Slot di coppia della coppia di motori.

##### Argomenti facoltativi delle parole chiave:

##### stop: int

Comportamento del motore dopo che si è arrestato. Utilizza le costanti nel modulo `motor`.

I valori possibili sono  
`motor.COAST` per muovere il motore a inerzia fino all’arresto  
`motor.BREAK` per frenare e continuare a frenare dopo l’arresto  
`motor.HOLD` per dire al motore di mantenere la sua posizione  
`motor.CONTINUE` per dire al motore di continuare a funzionare a qualsiasi velocità stia funzionando fino a quando non riceve un altro comando  
`motor.SMART_COAST` per far frenare il motore fino all’arresto e quindi muoversi a inerzia, compensando le imprecisioni nel comando successivo  
`motor.SMART_BRAKE` per far frenare il motore e continuare a frenare dopo l’arresto e compensare le imprecisioni nel comando successivo

#### unpair

unpair(pair: int) -> None

Annulla l'accoppiamento di una coppia di motori.

```
import motor_pair

motor_pair.unpair(motor_pair.PAIR_1)
```

##### Parametri

___

##### pair: int

Slot di coppia della coppia di motori.

#### Costanti

___

#### motor\_pair Costanti

**PAIR\_1** = 0  
Prima coppia di motori  
**PAIR\_2** = 1  
Seconda coppia di motori  
**PAIR\_3** = 2  
Terza coppia di motori

### Orientamento

Il modulo `orientation` contiene tutte le costanti di orientamento da utilizzare con il modulo `light_matrix`.

Per utilizzare il modulo Orientamento, aggiungere la seguente istruzione di importazione al progetto:

```
import orientation
```

#### Costanti

___

#### orientation Costanti

**UP** = 0

**RIGHT** = 1

**DOWN** = 2

**LEFT** = 3

### Runloop

Il modulo `runloop` contiene tutte le funzioni e le costanti per utilizzare il Runloop.

Per utilizzare il modulo Runloop, aggiungi la seguente istruzione di importazione al progetto:

```
import runloop
```

Tutte le funzioni del modulo devono essere chiamate all'interno del modulo `runloop` come prefisso nel modo seguente:

```
runloop.run(some_async_function())
```

#### Funzioni

#### run

run(\*functions: Awaitable) -> None

Avvia un numero qualsiasi di funzioni `async` parallele. Questa è la funzione da utilizzare per creare programmi con una struttura simile a Blocchi parole.

##### Parametri

___

##### \*functions: awaitable

The functions to run

#### sleep\_ms

sleep\_ms(duration: int) -> Awaitable

Sospendi l'esecuzione dell'applicazione per un numero qualsiasi di millisecondi.

```
from hub import light_matrix
import runloop

async def main():
    light_matrix.write("Hi!")
    # Attendi dieci secondi 
    await runloop.sleep_ms(10000)
    light_matrix.write("Are you still here?")

runloop.run(main())

```

##### Parametri

___

##### duration: int

Durata in millisecondi.

#### until

until(function: Callable\[\[\], bool\], timeout: int = 0) -> Awaitable

Restituisce un awaitable che ritornerà quando la condizione nella funzione o lambda passata è `True` o quando va in time out

```
import color_sensor
import color
from hub import port
import runloop

def is_color_red():
    return color_sensor.color(port.A) is color.RED

async def main():
    # Attendi fino a quando il sensore di colore non vede rosso 
    await runloop.until(is_color_red)
    print("Red!")

runloop.run(main())

```

##### Parametri

___

##### function: Callable\[\[\], bool\]

Oggetto richiamabile senza parametri che restituisce `True` o `False`.  
Chiamabile è tutto ciò che può essere chiamato, quindi una `def` o una `lambda`.

##### timeout: int

Timeout per la funzione in millisecondi.  
Se il chiamabile non restituisce `True` entro il timeout, `until` si risolve comunque dopo il timeout.  
0 significa nessun timeout; in tal caso non si risolverà fino a quando il chiamabile non restituisce `True`

piccolissima prova di programmazione\*

piccolissima prova di programmazione

Motors

Movement

Light

Sound

Events

Control

Sensors

Operators

Variables

My Blocks

A1eseguiperrotazioniA0vaial percorso più cortoalla posizioneAavvia motoreAarresta motoreA75imposta velocità sul%AposizioneAvelocità10muoviperrotazioniavvia movimentodestra: 3010muoviperrotazionidestra: 30avvia movimentoarresta movimento50imposta velocità di movimento sul%A+Bimposta motori di movimento su17.5imposta rotazione di 1 motore acmcon spostamento2attivapersecondiattivaHelloscrividisattiva pixel75imposta la luminosità dei pixel sul%11100imposta pixel su, dalal%ruotaverticaleimposta l'orientamento suimposta la luce del pulsante centrale suAillumina diCat Meow 1riproduci suonofino al completamento dell'operazioneCat Meow 1avvia suono600.2riproduci segnale acusticopersecondi60avvia riproduzione segnale acusticoarresta tutti i suoni10cambia effettofrequenzadi100porta effettofrequenzaarimuovi effetti audio\-10cambia volume di100porta volume a%volumeall'avvio del programmaAquando il colore èAquandopremutoA8quandodistanza minore di%quando è inclinatoquandoparte anterioreè suquandoscossoquando il pulsantesinistrapremuto10quando il timer >quandoquando ricevomessaggio1messaggio1invia a tuttimessaggio1invia a tuttie attendi1attendisecondi10ripetivolteper sempreseallorasealloraaltrimentiattendi fino a quandoripeti fino a quandoarresta altri stackarrestatuttiAil colore è?AcoloreA50riflesso del<%?Aluce riflessaAèpremuto?Apressione in%A15èdistanza minore di%?Adistanza in%È inclinato?parte anterioreè su?èscosso?angolo diinclinazioneimposta angolo di imbardata su 0èsinistrail pulsantepremuto?timerreimposta timer110numero a caso trae  +  \-  \*  / 100< 100\= 100\>eonon0\-1010è trae?applebananaunione die1appleletteradiapplelunghezza diappleacontiene  resto della divisione didiviso arrotonda valore assolutodiMotorsMovementLightSoundEventsControlSensorsOperatorsVariablesCrea una VariabileCrea una ListaMy BlocksCrea un Blocco

scratch.toolbox.movement

scratch.toolbox.movement

connetti

SPIKE™ Prime

connetti

1

2

3

4

5

6

7

8

9

from hub import light\_matrix

import runloop

async def main():

    # write your code here

    await light\_matrix.write("Hi!")

runloop.run(main())

Enter to Rename, Shift+Enter to Preview

Console

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTg4IiBoZWlnaHQ9IjQzNiIgdmlld0JveD0iMCAwIDU4OCA0MzYiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxnIGNsaXAtcGF0aD0idXJsKCNjbGlwMF81MDAwXzIyNDU0KSI+CjxwYXRoIGQ9Ik0zMS4xOSAyODUuMDIzTDI4LjM5IDI4My41ODNDMjcuNjM0OSAyODQuOCAyNy4wNDM4IDI4Ni4xMTEgMjYuNjMyIDI4Ny40ODNMMjkuNjcyIDI4OC40NzNDMzAuMDU3MSAyODcuMjc0IDMwLjU2NTggMjg2LjExNyAzMS4xOSAyODUuMDIzWiIgZmlsbD0iIzE4MTcxNiIvPgo8cGF0aCBkPSJNMTAwLjYzOSAzNjYuNjIyQzk1LjQzOSAzNDUuMzUgODIuNzcyIDMzNS4zNzYgNzEuNTk3IDMyNi41NzVDNjIuMzA4IDMxOS4yNjEgNTQuMjg4IDMxMi45NDQgNTEuNDE3IDMwMS4xOTdDNDkuOTcxIDI5NS4yODYgNTMuNDM4IDI4OC4wMjUgNTYuNzkyIDI4MS4wMDVDNTkuNjEgMjc1LjEwNSA2Mi41MjUgMjY5LjAwNSA2Mi45MDkgMjYzLjAxNEM2My4zODggMjU1LjU4MyA1OS44OTcgMjQ5LjU0OCA1Mi41MzQgMjQ1LjA3OUM0My4wMzQgMjM5LjMwNyAzMS4yMTUgMjQwLjM2MyAyMC45MzQgMjQ3LjkwMUMxMy4yMDggMjUzLjU1MyA2Ljk4NTAyIDI2Mi4zMTMgMy40MDMwMiAyNzIuNTUzQy0wLjU1MzUzOSAyODQuMDY0IC0xLjA4MDkxIDI5Ni40NzYgMS44ODUwMiAzMDguMjhDNy43MTEwMiAzMzIuMTE0IDIyLjUyNSAzNDQuNjMxIDM0LjQyNiAzNTQuNjg5QzQyLjYwNSAzNjEuNjAxIDQ5LjY2NyAzNjcuNTY5IDUxLjU2MiAzNzUuMzE2QzUzLjQ0MyAzODMuMDE2IDUwLjMzMSAzODguMzE2IDQ2LjcyNiAzOTQuNDQxQzQxLjk3NCA0MDIuNTIyIDM2LjA1OSA0MTIuNTggNDcuMDI2IDQyN0M1My4xNDQgNDM1LjA0IDYyLjExOSA0MzcuODEzIDcxLjU3OCA0MzQuNzk0QzcyLjg2MSA0MzQuMzgzIDc0LjExNDMgNDMzLjg4NCA3NS4zMjkgNDMzLjMwMUM4NC40NSA0MjguOTUgOTIuNTIxIDQxOS44MzUgOTcuNDcgNDA4LjI5MkMxMDMuMDYxIDM5NS4xMjQgMTA0LjE3NCAzODAuNDg0IDEwMC42MzkgMzY2LjYyMlpNODkuMjU0IDQwNC43NjRDODUuMjA5IDQxNC4xOTggNzguNTY3IDQyMS44NDUgNzEuNDg0IDQyNS4yMjRDNjYuNjExIDQyNy41NDcgNTkuNjU0IDQyOC44MDIgNTQuMTU0IDQyMS41ODJDNDYuODE5IDQxMS45NCA0OS44NTQgNDA2Ljc4MiA1NC40NDEgMzk4Ljk4MkM1OC4yNTUgMzkyLjQ5NyA2MyAzODQuNDI1IDYwLjI1NiAzNzMuMTk0QzU3LjY3IDM2Mi42MTcgNDkuMTg2IDM1NS40NDggNDAuMjA0IDM0Ny44NTdDMjguNzI0IDMzOC4xNTcgMTUuNzE0IDMyNy4xNTcgMTAuNTggMzA2LjE1N0M0Ljk0NDAyIDI4My4wOTUgMTQuNzM2IDI2My41MzUgMjYuMjE5IDI1NS4xMkMyOC40NTU5IDI1My40NDUgMzAuOTQ5MSAyNTIuMTQzIDMzLjYwMiAyNTEuMjY0QzM1Ljk0NTEgMjUwLjQ0NSAzOC40Mzk2IDI1MC4xNTIgNDAuOTA4NyAyNTAuNDA1QzQzLjM3NzggMjUwLjY1OSA0NS43NjA5IDI1MS40NTIgNDcuODg5IDI1Mi43MjlDNTYuNzM3IDI1OC4xMDEgNTUuMTQyIDI2My42OTIgNDguNzE2IDI3Ny4xNDhDNDQuODc0IDI4NS4xOTIgNDAuNTE2IDI5NC4zMSA0Mi43MTYgMzAzLjMyMkM0Ni4zMjEgMzE4LjA2OCA1Ni4zNTMgMzI1Ljk2OSA2Ni4wNTQgMzMzLjYwOEM3Ni41ODUgMzQxLjkgODcuNDczIDM1MC40NzQgOTEuOTM5IDM2OC43NDhDOTUuMDEzIDM4MC43MjMgOTQuMDY5NyAzOTMuMzc3IDg5LjI1NCA0MDQuNzY0WiIgZmlsbD0iIzE4MTcxNiIvPgo8cGF0aCBkPSJNNDAuMzU0IDI3NS41ODlDNDIuMjk1IDI3NC45NyA0NC4wMDg3IDI3My43ODkgNDUuMjc4NSAyNzIuMTk2QzQ2LjU0ODIgMjcwLjYwMiA0Ny4zMTcgMjY4LjY2OCA0Ny40ODc2IDI2Ni42MzhDNDcuNjU4MSAyNjQuNjA4IDQ3LjIyMjggMjYyLjU3MyA0Ni4yMzY2IDI2MC43OUM0NS4yNTA0IDI1OS4wMDggNDMuNzU3NyAyNTcuNTU3IDQxLjk0NzMgMjU2LjYyM0M0MC4xMzY5IDI1NS42ODkgMzguMDkgMjU1LjMxMiAzNi4wNjU2IDI1NS41NDFDMzQuMDQxMyAyNTUuNzcgMzIuMTMwMyAyNTYuNTk1IDMwLjU3NDQgMjU3LjkxQzI5LjAxODUgMjU5LjIyNSAyNy44ODc2IDI2MC45NzIgMjcuMzI0NyAyNjIuOTNDMjYuNzYxOCAyNjQuODg4IDI2Ljc5MjIgMjY2Ljk2OSAyNy40MTIgMjY4LjkxQzI4LjI0MyAyNzEuNTEyIDMwLjA3MzEgMjczLjY3NyAzMi41MDAxIDI3NC45MjlDMzQuOTI3MSAyNzYuMTgyIDM3Ljc1MjEgMjc2LjQxOSA0MC4zNTQgMjc1LjU4OVoiIGZpbGw9IiMxODE3MTYiLz4KPHBhdGggZD0iTTY0LjMyMiAzOTkuODM3QzYyLjM4MTIgNDAwLjQ1NiA2MC42Njc2IDQwMS42MzcgNTkuMzk4MSA0MDMuMjMxQzU4LjEyODYgNDA0LjgyNCA1Ny4zNjAxIDQwNi43NTggNTcuMTg5OCA0MDguNzg4QzU3LjAxOTYgNDEwLjgxOSA1Ny40NTUyIDQxMi44NTQgNTguNDQxNyA0MTQuNjM2QzU5LjQyODEgNDE2LjQxOSA2MC45MjEgNDE3Ljg2OSA2Mi43MzE2IDQxOC44MDNDNjQuNTQyMiA0MTkuNzM3IDY2LjU4OTEgNDIwLjExMyA2OC42MTM1IDQxOS44ODRDNzAuNjM3OCA0MTkuNjU0IDcyLjU0ODcgNDE4LjgzIDc0LjEwNDQgNDE3LjUxNEM3NS42NjAxIDQxNi4xOTkgNzYuNzkwNyA0MTQuNDUyIDc3LjM1MzMgNDEyLjQ5M0M3Ny45MTU5IDQxMC41MzUgNzcuODg1MiA0MDguNDU0IDc3LjI2NSA0MDYuNTE0Qzc2LjQzMzcgNDAzLjkxMiA3NC42MDMyIDQwMS43NDggNzIuMTc2IDQwMC40OTVDNjkuNzQ4OSAzOTkuMjQzIDY2LjkyMzggMzk5LjAwNiA2NC4zMjIgMzk5LjgzN1oiIGZpbGw9IiMxODE3MTYiLz4KPHBhdGggZD0iTTc3LjQ3MSAzODUuOTg0TDc0LjMzIDM4NS4zODRDNzQuMTQxNSAzODYuNSA3My44MTc3IDM4Ny41OSA3My4zNjYgMzg4LjYyOEw3Ni4yMTggMzkwLjA3MUM3Ni44MTI5IDM4OC43NjkgNzcuMjM0MiAzODcuMzk1IDc3LjQ3MSAzODUuOTg0WiIgZmlsbD0iIzE4MTcxNiIvPgo8cGF0aCBkPSJNNzYuMDkgMzcwLjIwMUw3My4wNTEgMzcxLjE5Mkw3My4xNDEgMzcxLjQ3M0M3My44NTcyIDM3My42ODMgNzQuMzQwOCAzNzUuOTYyIDc0LjU4NCAzNzguMjczTDc3Ljc2NCAzNzcuOTU0Qzc3LjQ5OTcgMzc1LjQyMSA3Ni45NzA4IDM3Mi45MjMgNzYuMTg2IDM3MC41TDc2LjA5IDM3MC4yMDFaIiBmaWxsPSIjMTgxNzE2Ii8+CjxwYXRoIGQ9Ik02NC4xMzggMzUwLjIxNkM2Mi41MjIgMzQ4LjM0NCA2MC43MzggMzQ2LjQ0OCA1OC44NDggMzQ0LjU4Mkw1Ni42MDUgMzQ2Ljg1OUM1OC40MzcgMzQ4LjY2NiA2MC4xNTkgMzUwLjQ5OCA2MS43MjEgMzUyLjMwNUw2NC4xMzggMzUwLjIxNloiIGZpbGw9IiMxODE3MTYiLz4KPHBhdGggZD0iTTM1Ljc4NyAzMjQuMzk3QzM3LjIxMiAzMjYuNDE4IDM4Ljc5OCAzMjguNDc3IDQwLjUwNCAzMzAuNTJMNDIuOTU3IDMyOC40NzFDNDEuMzA3IDMyNi40OTUgMzkuNzc1IDMyNC41MDUgMzguNCAzMjIuNTU1TDM1Ljc4NyAzMjQuMzk3WiIgZmlsbD0iIzE4MTcxNiIvPgo8cGF0aCBkPSJNNzMuMDAzIDM2Mi45NzNDNzEuNzg2NCAzNjAuNjcxIDcwLjQyMyAzNTguNDUgNjguOTIxIDM1Ni4zMjNMNjYuMzA2IDM1OC4xNjFDNjcuNzI4OCAzNjAuMTc2IDY5LjAyMDUgMzYyLjI4IDcwLjE3MyAzNjQuNDYxTDczLjAwMyAzNjIuOTczWiIgZmlsbD0iIzE4MTcxNiIvPgo8cGF0aCBkPSJNMjguNjc1IDI5NS40NEwyNS40ODIgMjk1LjI2NEMyNS4zNTExIDI5Ny45MjggMjUuNTQ1MiAzMDAuNTk5IDI2LjA2IDMwMy4yMTZMMjkuMiAzMDIuNjE2QzI4LjczMjUgMzAwLjI1NSAyOC41NTYyIDI5Ny44NDUgMjguNjc1IDI5NS40NFoiIGZpbGw9IiMxODE3MTYiLz4KPHBhdGggZD0iTTI4LjI3OSAzMTAuNzgxQzI5LjIzNjggMzEzLjIwNiAzMC4zNTg3IDMxNS41NjMgMzEuNjM3IDMxNy44MzVMMzQuNDI3IDMxNi4yNzVDMzMuMjE5NyAzMTQuMTMxIDMyLjE2MDIgMzExLjkwNiAzMS4yNTYgMzA5LjYxN0wyOC4yNzkgMzEwLjc4MVoiIGZpbGw9IiMxODE3MTYiLz4KPHBhdGggZD0iTTQ3Ljk1NCAzMzQuMDZMNDUuNjM5IDMzNi4yNjVDNDcuMzQ1IDMzOC4wNTcgNDkuMTggMzM5Ljg4IDUxLjA4OCAzNDEuNjgzTDUzLjI4OCAzMzkuMzU5QzUxLjQxMSAzMzcuNTk1IDQ5LjYxOSAzMzUuODEyIDQ3Ljk1NCAzMzQuMDZaIiBmaWxsPSIjMTgxNzE2Ii8+CjxwYXRoIGQ9Ik0yNTUuNTk0IDI4Mi40MTZDMjU0LjQ0NiAyNzMuMTQ1IDI1MS40ODQgMjY0LjE5IDI0Ni44NzYgMjU2LjA2NEMyNDIuMjY4IDI0Ny45MzcgMjM2LjEwNCAyNDAuNzk4IDIyOC43MzcgMjM1LjA1NEMyMjEuMzY5IDIyOS4zMDkgMjEyLjk0MyAyMjUuMDcyIDIwMy45MzggMjIyLjU4NEMxOTQuOTMzIDIyMC4wOTcgMTg1LjUyNyAyMTkuNDA3IDE3Ni4yNTYgMjIwLjU1NEMxNjYuOTg0IDIyMS43MDIgMTU4LjAzIDIyNC42NjQgMTQ5LjkwMyAyMjkuMjczQzE0MS43NzcgMjMzLjg4MSAxMzQuNjM4IDI0MC4wNDQgMTI4Ljg5MyAyNDcuNDEyQzEyMy4xNDkgMjU0Ljc3OSAxMTguOTEyIDI2My4yMDYgMTE2LjQyNCAyNzIuMjFDMTEzLjkzNiAyODEuMjE1IDExMy4yNDYgMjkwLjYyMiAxMTQuMzk0IDI5OS44OTNMMTI4Ljg5NCA0MTYuOTQ2QzEyOS4wMjcgNDE4LjA0NSAxMjkuNTg4IDQxOS4wNDggMTMwLjQ1NSA0MTkuNzM3QzEzMS4zMjIgNDIwLjQyNiAxMzIuNDI1IDQyMC43NDYgMTMzLjUyNiA0MjAuNjI3QzEzNC42MjcgNDIwLjUwOSAxMzUuNjM4IDQxOS45NjIgMTM2LjMzOCA0MTkuMTA1QzEzNy4wMzkgNDE4LjI0NyAxMzcuMzc0IDQxNy4xNDggMTM3LjI3MSA0MTYuMDQ2SDEzNy4yOEwxMzcuMjcgNDE1Ljk2QzEzNy4yNyA0MTUuOTYgMTM3LjI3IDQxNS45NSAxMzcuMjcgNDE1Ljk0NVY0MTUuOTI4TDEzNS44MTUgNDA0LjIwN0wxNTEuNzIzIDQwMi4yMzlMMTUzLjE1NSA0MTMuNzk5QzE1My4yODggNDE0LjkwOSAxNTMuODU2IDQxNS45MjIgMTU0LjczNSA0MTYuNjEzQzE1NS42MTQgNDE3LjMwNSAxNTYuNzMyIDQxNy42MTkgMTU3Ljg0MyA0MTcuNDg2QzE1OC45NTMgNDE3LjM1NCAxNTkuOTY2IDQxNi43ODUgMTYwLjY1NyA0MTUuOTA2QzE2MS4zNDkgNDE1LjAyNyAxNjEuNjYzIDQxMy45MDkgMTYxLjUzIDQxMi43OTlMMTU0LjQwMyAzNTUuMzQ2QzE2NS45MTMgMzYwLjg0NCAxNzguNjkgMzYzLjE0NSAxOTEuMzk0IDM2Mi4wMDZDMjA0LjA5OSAzNjAuODY3IDIxNi4yNjMgMzU2LjMzMSAyMjYuNjExIDM0OC44NzNDMjM2Ljk1OSAzNDEuNDE2IDI0NS4xMSAzMzEuMzExIDI1MC4yMDkgMzE5LjYxOUMyNTUuMzA5IDMwNy45MjcgMjU3LjE2OCAyOTUuMDc5IDI1NS41OTMgMjgyLjQyMUwyNTUuNTk0IDI4Mi40MTZaTTI0Ni4yMjUgMzA0LjczOUwyMzAuNzAxIDMwMC41NThDMjMxLjU0MSAyOTYuNTAxIDIzMS44MzMgMjkyLjM1IDIzMS41NjkgMjg4LjIxNUwyNDcuNTIgMjg2LjI0QzI0OC4wMTIgMjkyLjQzNiAyNDcuNTc2IDI5OC42NzIgMjQ2LjIyNSAzMDQuNzM5Wk0xOTMuNSAzMzcuMDM5QzE5Ny43NzUgMzM2LjI1MSAyMDEuOTE4IDMzNC44NjYgMjA1LjgwNyAzMzIuOTI0TDIxMy44MjggMzQ2Ljg1OUMyMDguMDY3IDM0OS44NDYgMjAxLjg3NSAzNTEuOTE0IDE5NS40NzUgMzUyLjk5TDE5My41IDMzNy4wMzlaTTE4OS43IDMyOS4xMjZDMTc5LjYzNCAzMzAuMzYxIDE2OS40ODkgMzI3LjU1NCAxNjEuNDkgMzIxLjMyQzE1My40OTEgMzE1LjA4NiAxNDguMjkxIDMwNS45MzQgMTQ3LjAzMSAyOTUuODcxVjI5NS44NTZDMTQ2LjEwMSAyODguMzQ2IDE0Ny40MTkgMjgwLjcyOCAxNTAuODE4IDI3My45NjdDMTU0LjIxNyAyNjcuMjA2IDE1OS41NDUgMjYxLjYwNCAxNjYuMTI4IDI1Ny44NzFDMTcyLjcxMSAyNTQuMTM4IDE4MC4yNTMgMjUyLjQ0MSAxODcuOCAyNTIuOTk0QzE5NS4zNDcgMjUzLjU0NyAyMDIuNTYxIDI1Ni4zMjYgMjA4LjUyOSAyNjAuOTc5QzIxNC40OTcgMjY1LjYzMiAyMTguOTUxIDI3MS45NTEgMjIxLjMyOCAyNzkuMTM1QzIyMy43MDUgMjg2LjMyIDIyMy44OTkgMjk0LjA0OCAyMjEuODg0IDMwMS4zNDJDMjE5Ljg2OCAzMDguNjM3IDIxNS43MzUgMzE1LjE3IDIxMC4wMDcgMzIwLjExNUMyMDQuMjc5IDMyNS4wNiAxOTcuMjEzIDMyOC4xOTYgMTg5LjcwMyAzMjkuMTI2SDE4OS43Wk0xNDguNDc3IDM3NS45ODVMMTMyLjU1OSAzNzcuOTUzTDEzMC42NjggMzYyLjcwNkwxNDYuNTg0IDM2MC43MzZMMTQ4LjQ3NyAzNzUuOTg1Wk0xMjkuOTc3IDM1Ny4xNDJMMTI4LjI0IDM0My4xNDJMMTQ0LjE2MSAzNDEuMTcyTDE0NS44OTUgMzU1LjE3MkwxMjkuOTc3IDM1Ny4xNDJaTTEyMy43NjcgMjc3LjU3MUwxMzkuMjkxIDI4MS43NTFDMTM4LjQ1MSAyODUuODA4IDEzOC4xNTkgMjg5Ljk1OSAxMzguNDI0IDI5NC4wOTRMMTIyLjQ3MiAyOTYuMDY5QzEyMS45NzggMjg5Ljg3MiAxMjIuNDE1IDI4My42MzcgMTIzLjc2NyAyNzcuNTdWMjc3LjU3MVpNMTQwLjc0NCAyNzYuMzM1TDEyNS4yMzcgMjcyLjE1OUMxMjcuMjEgMjY1Ljk4MSAxMzAuMTI2IDI2MC4xNDYgMTMzLjg4MiAyNTQuODU5TDE0Ni41NTYgMjY0Ljc0MUMxNDQuMDkgMjY4LjMxNyAxNDIuMTM0IDI3Mi4yMTkgMTQwLjc0NCAyNzYuMzM0VjI3Ni4zMzVaTTEzOS4wMjEgMjk5LjY3MUwxNDAuOTA5IDMxNC45MThMMTI0Ljk4MyAzMTYuODg5TDEyMy4wOTEgMzAxLjY0MkwxMzkuMDIxIDI5OS42NzFaTTE0MS41OTkgMzIwLjQ4NEwxNDMuNDcyIDMzNS42MDZMMTI3LjU1NCAzMzcuNTc2TDEyNS42NzMgMzIyLjQ1M0wxNDEuNTk5IDMyMC40ODRaTTE1MC4zMSAzMjIuMzQzQzE1MS41MTkgMzIzLjY4MiAxNTIuODAzIDMyNC45NTEgMTU0LjE1OCAzMjYuMTQzTDE1MS4yNDYgMzI5Ljg3OEwxNTAuMzEgMzIyLjM0M1pNMTc2LjQ5MSAyNDUuMjcxQzE3Mi4yMTYgMjQ2LjA1OSAxNjguMDc0IDI0Ny40NDUgMTY0LjE4NSAyNDkuMzg3TDE1Ni4xNjQgMjM1LjQ1M0MxNjEuOTI1IDIzMi40NjYgMTY4LjExNyAyMzAuMzk4IDE3NC41MTcgMjI5LjMyMkwxNzYuNDkxIDI0NS4yNzFaTTE5OS44MTcgMjQ2LjkwM0wyMDMuOTkyIDIzMS4zOTdDMjEwLjE3IDIzMy4zNyAyMTYuMDA1IDIzNi4yODUgMjIxLjI5MiAyNDAuMDQxTDIxMS40MDkgMjUyLjcxNUMyMDcuODMzIDI1MC4yNDkgMjAzLjkzMiAyNDguMjkzIDE5OS44MTcgMjQ2LjkwMlYyNDYuOTAzWk0yMzAuODggMjgyLjY1M0MyMzAuMDkyIDI3OC4zNzkgMjI4LjcwNyAyNzQuMjM2IDIyNi43NjUgMjcwLjM0OEwyNDAuNjk5IDI2Mi4zMjZDMjQzLjY4NiAyNjguMDg3IDI0NS43NTUgMjc0LjI3OSAyNDYuODMxIDI4MC42NzlMMjMwLjg4IDI4Mi42NTNaTTIyOS4yNDggMzA1Ljk3OUwyNDQuNzU0IDMxMC4xNTNDMjQyLjc4MiAzMTYuMzMxIDIzOS44NjYgMzIyLjE2NiAyMzYuMTEgMzI3LjQ1M0wyMjMuNDM2IDMxNy41NzFDMjI1LjkwMiAzMTMuOTk0IDIyNy44NTggMzEwLjA5MSAyMjkuMjQ4IDMwNS45NzVWMzA1Ljk3OVpNMjM3Ljg5NSAyNTcuNDdMMjIzLjk2MSAyNjUuNDkxQzIyMS42NzcgMjYyLjAzNyAyMTguOTQ0IDI1OC45MDIgMjE1LjgzNSAyNTYuMTY3TDIyNS43MTcgMjQzLjQ5MkMyMzAuNDQ0IDI0Ny41MjMgMjM0LjU0NyAyNTIuMjMzIDIzNy44OTUgMjU3LjQ2NlYyNTcuNDdaTTE5OC41ODEgMjI5LjkyOUwxOTQuNCAyNDUuNDUzQzE5MC4zNDMgMjQ0LjYxNCAxODYuMTkyIDI0NC4zMjIgMTgyLjA1NyAyNDQuNTg1TDE4MC4wODIgMjI4LjYzNEMxODYuMjc4IDIyOC4xNCAxOTIuNTE0IDIyOC41NzUgMTk4LjU4MSAyMjkuOTI1VjIyOS45MjlaTTE1MS4zMDcgMjM4LjI1OUwxNTkuMzI5IDI1Mi4xOTNDMTU1Ljg3NSAyNTQuNDc4IDE1Mi43NCAyNTcuMjEgMTUwLjAwNCAyNjAuMzE5TDEzNy4zMyAyNTAuNDM3QzE0MS4zNjIgMjQ1LjcwOCAxNDYuMDcyIDI0MS42MDIgMTUxLjMwNyAyMzguMjUzVjIzOC4yNTlaTTEzNS4xMjYgMzk4LjY0TDEzMy4yNTQgMzgzLjUxOEwxNDkuMTY2IDM4MS41NDlMMTUxLjAzOSAzOTYuNjcyTDEzNS4xMjYgMzk4LjY0Wk0xNTIuMjI2IDMzNy43NDhMMTU4LjU4MyAzMjkuNTk0QzE2Mi4xNjEgMzMyLjA2IDE2Ni4wNjUgMzM0LjAxNyAxNzAuMTgzIDMzNS40MDdMMTY2LjAwNiAzNTAuOTE5QzE2MS41MTcgMzQ5LjQ4NCAxNTcuMjAzIDM0Ny41NDkgMTUzLjE0NyAzNDUuMTQ5TDE1Mi4yMjYgMzM3Ljc0OFpNMTcxLjQxNiAzNTIuMzgyTDE3NS41OTUgMzM2Ljg1OUMxNzkuNjUyIDMzNy42OTkgMTgzLjgwNCAzMzcuOTkxIDE4Ny45MzkgMzM3LjcyN0wxODkuOTE0IDM1My42ODJDMTgzLjcxNiAzNTQuMTc1IDE3Ny40OCAzNTMuNzM2IDE3MS40MTIgMzUyLjM4MkgxNzEuNDE2Wk0yMTguNjg5IDM0NC4wNTNMMjEwLjY2NyAzMzAuMTE5QzIxNC4xMjEgMzI3LjgzNCAyMTcuMjU3IDMyNS4xMDIgMjE5Ljk5MiAzMjEuOTkzTDIzMi42NjYgMzMxLjg3NUMyMjguNjMyIDMzNi42MDIgMjIzLjkyMSAzNDAuNzA2IDIxOC42ODUgMzQ0LjA1M0gyMTguNjg5WiIgZmlsbD0iIzE4MTcxNiIvPgo8cGF0aCBkPSJNMzI4LjQxMyAzMjQuMjUzQzMyNi44OTEgMzIxLjQ5NiAzMjQuNjk3IDMxOS4xNjggMzIyLjAzNSAzMTcuNDg1QzMxOS4zNzMgMzE1LjgwMiAzMTYuMzI5IDMxNC44MTkgMzEzLjE4NiAzMTQuNjI2QzMxMy4zMzkgMzEzLjU5OSAzMTMuNTQzIDMxMi41OCAzMTMuNzk4IDMxMS41NzNDMzE1LjQ2NyAzMDUuMDA2IDMxNi41MTIgMzAyLjEwNiAzMTcuODE1IDI5Ny40NDZDMzE5LjMyOCAyOTIuMDM2IDMxOS40MzQgMjkxLjc3IDMyMS4wNTMgMjg1LjQ3NEMzMjMuNDMyIDI3Ni4yMTcgMzIzLjU1MyAyNjUuMTE1IDMxOS40OTcgMjU2LjI4MkMzMTguMTE4IDI1My4yNDEgMzE2LjEyNyAyNTAuNTE2IDMxMy42NDcgMjQ4LjI4QzMxMS4xNjcgMjQ2LjA0MyAzMDguMjUzIDI0NC4zNDIgMzA1LjA4NiAyNDMuMjgyQzI5Ny42OTQgMjQxLjA1MSAyODcuMDAxIDI0Mi4xNjUgMjgxLjUzOSAyNDguM0MyNzguMTQ4IDI1Mi4xMDkgMjc2LjQyMiAyNTUuNDYgMjc2LjA4MSAyNjAuNzc2QzI3NS43OTIgMjY1LjI4MyAyNzcuNDQ5IDI3MC43OTYgMjgwLjYzMSAyNzQuMTE2QzI4Mi4xOTEgMjc1LjY2NyAyODMuOTQ1IDI3Ny4wMDggMjg1Ljg1IDI3OC4xMDdDMjg1LjYxNiAyODAuMDczIDI4NS4yNjMgMjgyLjAyMiAyODQuNzkzIDI4My45NDVDMjgwLjk5MyAyOTkuNTk3IDI3OC4xNTggMzAyLjg3NiAyNzYuNTE3IDMxMi42NDVDMjc0LjgxMSAzMjIuODA0IDI3OC4xNTYgMzM0LjU2OCAyODUuNjY4IDM0MS45ODVDMjk1LjA5IDM1MS4yODUgMzA3LjkwNyAzNTQuMzE0IDMyMC4yMDkgMzQ4Ljk3OUMzMjkuMDYzIDM0NS4xMyAzMzMuMDcgMzMyLjYwMiAzMjguNDEzIDMyNC4yNTNaTTMwNC44ODkgMjUwLjc1M0MzMDcuODU0IDI1Mi44OTIgMzExLjAwMSAyNTcuODA1IDMxMi40NiAyNjAuODg0QzMxNS4yNjkgMjY2LjU1IDMxNi40NzYgMjcyLjg3NSAzMTUuOTUyIDI3OS4xNzdDMzE1LjU0NSAyODUuMjI2IDMxMy45NTIgMjkyLjU2MyAzMTMuMjEyIDI5Mi40NTlDMzEyLjQ3MiAyOTIuMzU1IDMxNC4yNjYgMjc5LjI2OSAzMDguMTM1IDI2OC43NTlDMzAyLjU4MSAyNTkuMjM0IDI5NC40MTggMjU3LjExNiAyOTQuNjkgMjUxLjM3NUMyOTQuODYgMjQ3Ljc4IDI5OS45NDcgMjQ3LjE4MyAzMDQuODg5IDI1MC43NTNaIiBmaWxsPSIjMTgxNzE2Ii8+CjxwYXRoIGQ9Ik0zMjAuMjk2IDIxMi4yNjZDMzE5Ljg0OSAyMDIuMjg5IDMxMi4yMDUgMTkzLjg1MSAzMDEuODgxIDE5My44NTFDMjkyLjI0OSAxOTMuODUxIDI4My4wMjEgMjAyLjMyMSAyODMuNDY2IDIxMi4yNjZDMjgzLjkxMyAyMjIuMjQzIDI5MS41NTcgMjMwLjY4MSAzMDEuODgxIDIzMC42ODFDMzExLjUxMyAyMzAuNjgxIDMyMC43NDEgMjIyLjIxMSAzMjAuMjk2IDIxMi4yNjZaTTMxMi40ODIgMjIwLjI1NUMzMTEuMjc2IDIyMS45MTkgMzEyLjc4MiAyMTAuOTM1IDMwNS4xMTUgMjA3LjYyNEMzMDAuMTY3IDIwNS40ODcgMjk2LjA3MSAyMDUuMDQ4IDI5NS44MTUgMjAyLjE4NUMyOTUuNzMxIDIwMS43MTcgMjk1Ljc5OCAyMDEuMjMzIDI5Ni4wMDcgMjAwLjgwNkMyOTYuMjE2IDIwMC4zNzggMjk2LjU1NiAyMDAuMDI4IDI5Ni45NzggMTk5LjgwN0MyOTcuODU3IDE5OS4xNTQgMjk5LjE2OCAxOTguOTM4IDMwMS4yOTggMTk5LjEwN0MzMDMuOTk3IDE5OS4yNDggMzA2LjU5OSAyMDAuMTU1IDMwOC44MDEgMjAxLjcyMkMzMTEuMDAzIDIwMy4yODkgMzEyLjcxNCAyMDUuNDUgMzEzLjczMiAyMDcuOTUzQzMxNC41OTggMjA5LjkzOCAzMTQuOTM4IDIxMi4xMTIgMzE0LjcxOSAyMTQuMjY3QzMxNC41IDIxNi40MjEgMzEzLjcyOSAyMTguNDgzIDMxMi40ODIgMjIwLjI1M1YyMjAuMjU1WiIgZmlsbD0iIzE4MTcxNiIvPgo8cGF0aCBkPSJNMzc4Ljc2IDMyMy4xNjlDMzc2LjA2MSAzMjMuMTcxIDM3My40MjggMzIyLjMyOCAzNzEuMjMyIDMyMC43NThDMzY5LjAzNiAzMTkuMTg4IDM2Ny4zODcgMzE2Ljk3IDM2Ni41MTUgMzE0LjQxNUMzNjUuNjQ0IDMxMS44NiAzNjUuNTk0IDMwOS4wOTcgMzY2LjM3NCAzMDYuNTEyQzM2Ny4xNTMgMzAzLjkyNyAzNjguNzIyIDMwMS42NTIgMzcwLjg2IDMwMC4wMDRMMzU5LjE2IDI5MS42MDRWMzUxLjM5M0MzNTkuMTYgMzU2LjU5MSAzNjEuMjI1IDM2MS41NzcgMzY0LjkwMSAzNjUuMjUyQzM2OC41NzYgMzY4LjkyOCAzNzMuNTYyIDM3MC45OTMgMzc4Ljc2IDM3MC45OTNDMzgzLjk1OCAzNzAuOTkzIDM4OC45NDQgMzY4LjkyOCAzOTIuNjE5IDM2NS4yNTJDMzk2LjI5NSAzNjEuNTc3IDM5OC4zNiAzNTYuNTkxIDM5OC4zNiAzNTEuMzkzVjMxOS43NTNMMzkwLjk3OCAzMTQuNDUzQzM5MC4xMDEgMzE2Ljk5NiAzODguNDUzIDMxOS4yMDMgMzg2LjI2MyAzMjAuNzY1QzM4NC4wNzMgMzIyLjMyNyAzODEuNDUgMzIzLjE2OCAzNzguNzYgMzIzLjE2OVpNMzc4Ljc2IDM2Mi4zNjlDMzc2LjIwMSAzNjIuMzY5IDM3My43IDM2MS42MSAzNzEuNTczIDM2MC4xODlDMzY5LjQ0NiAzNTguNzY3IDM2Ny43ODggMzU2Ljc0NyAzNjYuODA5IDM1NC4zODNDMzY1LjgzIDM1Mi4wMiAzNjUuNTczIDM0OS40MTkgMzY2LjA3MyAzNDYuOTA5QzM2Ni41NzIgMzQ0LjQgMzY3LjgwNCAzNDIuMDk1IDM2OS42MTMgMzQwLjI4NkMzNzEuNDIyIDMzOC40NzcgMzczLjcyNyAzMzcuMjQ1IDM3Ni4yMzYgMzM2Ljc0NkMzNzguNzQ2IDMzNi4yNDYgMzgxLjM0NyAzMzYuNTAzIDM4My43MSAzMzcuNDgyQzM4Ni4wNzQgMzM4LjQ2MSAzODguMDk0IDM0MC4xMTkgMzg5LjUxNiAzNDIuMjQ2QzM5MC45MzcgMzQ0LjM3MyAzOTEuNjk2IDM0Ni44NzUgMzkxLjY5NiAzNDkuNDMzQzM5MS42OTYgMzUxLjEzMiAzOTEuMzYxIDM1Mi44MTQgMzkwLjcxMSAzNTQuMzgzQzM5MC4wNjEgMzU1Ljk1MiAzODkuMTA4IDM1Ny4zNzggMzg3LjkwNyAzNTguNTc5QzM4Ni43MDUgMzU5Ljc4IDM4NS4yNzkgMzYwLjczMyAzODMuNzEgMzYxLjM4M0MzODIuMTQxIDM2Mi4wMzMgMzgwLjQ1OSAzNjIuMzY3IDM3OC43NiAzNjIuMzY3VjM2Mi4zNjlaIiBmaWxsPSIjMTgxNzE2Ii8+CjxwYXRoIGQ9Ik0zNzEuMTA3IDE5Ni4xNzNDMzcxLjEwNiAxOTQuMTEgMzcxLjcxOCAxOTIuMDk0IDM3Mi44NjUgMTkwLjM3OUMzNzQuMDEyIDE4OC42NjUgMzc1LjY0MyAxODcuMzMgMzc3LjU1IDE4Ni41NDRDMzc5LjQ1NyAxODUuNzU4IDM4MS41NTUgMTg1LjU1NiAzODMuNTc3IDE4NS45NjVDMzg1LjU5OSAxODYuMzczIDM4Ny40NTQgMTg3LjM3MyAzODguOTA3IDE4OC44MzhDMzg4LjMxOCAxODcuNDE4IDM4Ny40MjIgMTg2LjE0NSAzODYuMjgyIDE4NS4xMTJDMzg1LjE0MyAxODQuMDggMzgzLjc4OSAxODMuMzEyIDM4Mi4zMTggMTgyLjg2NUMzODAuODQ3IDE4Mi40MTggMzc5LjI5NCAxODIuMzAyIDM3Ny43NzMgMTgyLjUyNkMzNzYuMjUyIDE4Mi43NSAzNzQuNzk5IDE4My4zMDkgMzczLjUxOSAxODQuMTYxQzM3Mi4yMzkgMTg1LjAxNCAzNzEuMTY0IDE4Ni4xNCAzNzAuMzcxIDE4Ny40NTdDMzY5LjU3OCAxODguNzc1IDM2OS4wODcgMTkwLjI1MSAzNjguOTMzIDE5MS43ODJDMzY4Ljc3OSAxOTMuMzEyIDM2OC45NjYgMTk0Ljg1NyAzNjkuNDggMTk2LjMwNkMzNjkuOTk0IDE5Ny43NTUgMzcwLjgyMyAxOTkuMDczIDM3MS45MDcgMjAwLjE2M0MzNzEuMzc5IDE5OC44OTkgMzcxLjEwNyAxOTcuNTQzIDM3MS4xMDcgMTk2LjE3M1oiIGZpbGw9IiMxODE3MTYiLz4KPHBhdGggZD0iTTM3MS4xMDcgMjM1LjIxMkMzNzEuMTA2IDIzMy4xNDkgMzcxLjcxOCAyMzEuMTMyIDM3Mi44NjUgMjI5LjQxOEMzNzQuMDEyIDIyNy43MDMgMzc1LjY0MyAyMjYuMzY4IDM3Ny41NSAyMjUuNTgyQzM3OS40NTcgMjI0Ljc5NiAzODEuNTU1IDIyNC41OTUgMzgzLjU3NyAyMjUuMDAzQzM4NS41OTkgMjI1LjQxMiAzODcuNDU0IDIyNi40MTIgMzg4LjkwNyAyMjcuODc3QzM4OC4zMTggMjI2LjQ1NiAzODcuNDIyIDIyNS4xODQgMzg2LjI4MiAyMjQuMTUxQzM4NS4xNDMgMjIzLjExOCAzODMuNzg5IDIyMi4zNTEgMzgyLjMxOCAyMjEuOTAzQzM4MC44NDcgMjIxLjQ1NiAzNzkuMjk0IDIyMS4zNDEgMzc3Ljc3MyAyMjEuNTY1QzM3Ni4yNTIgMjIxLjc4OSAzNzQuNzk5IDIyMi4zNDcgMzczLjUxOSAyMjMuMkMzNzIuMjM5IDIyNC4wNTMgMzcxLjE2NCAyMjUuMTc4IDM3MC4zNzEgMjI2LjQ5NkMzNjkuNTc4IDIyNy44MTMgMzY5LjA4NyAyMjkuMjkgMzY4LjkzMyAyMzAuODJDMzY4Ljc3OSAyMzIuMzUgMzY4Ljk2NiAyMzMuODk1IDM2OS40OCAyMzUuMzQ1QzM2OS45OTQgMjM2Ljc5NCAzNzAuODIzIDIzOC4xMTEgMzcxLjkwNyAyMzkuMjAyQzM3MS4zNzkgMjM3LjkzOCAzNzEuMTA3IDIzNi41ODIgMzcxLjEwNyAyMzUuMjEyWiIgZmlsbD0iIzE4MTcxNiIvPgo8cGF0aCBkPSJNMzcxLjEwNyAzNTMuNDQ2QzM3MS4xMDYgMzUxLjM4MyAzNzEuNzE3IDM0OS4zNjYgMzcyLjg2NSAzNDcuNjUyQzM3NC4wMTIgMzQ1LjkzNyAzNzUuNjQyIDM0NC42MDIgMzc3LjU1IDM0My44MTZDMzc5LjQ1NyAzNDMuMDMgMzgxLjU1NSAzNDIuODI4IDM4My41NzcgMzQzLjIzN0MzODUuNTk5IDM0My42NDUgMzg3LjQ1NCAzNDQuNjQ1IDM4OC45MDcgMzQ2LjExQzM4OC4zMTggMzQ0LjY5IDM4Ny40MjIgMzQzLjQxNyAzODYuMjgyIDM0Mi4zODRDMzg1LjE0MyAzNDEuMzUyIDM4My43ODkgMzQwLjU4NCAzODIuMzE4IDM0MC4xMzdDMzgwLjg0NyAzMzkuNjkgMzc5LjI5NCAzMzkuNTc0IDM3Ny43NzMgMzM5Ljc5OEMzNzYuMjUyIDM0MC4wMjIgMzc0Ljc5OSAzNDAuNTgxIDM3My41MTkgMzQxLjQzM0MzNzIuMjM5IDM0Mi4yODYgMzcxLjE2NCAzNDMuNDExIDM3MC4zNzEgMzQ0LjcyOUMzNjkuNTc4IDM0Ni4wNDcgMzY5LjA4NyAzNDcuNTIzIDM2OC45MzMgMzQ5LjA1NEMzNjguNzc5IDM1MC41ODQgMzY4Ljk2NiAzNTIuMTI5IDM2OS40OCAzNTMuNTc4QzM2OS45OTQgMzU1LjAyNyAzNzAuODIzIDM1Ni4zNDUgMzcxLjkwNyAzNTcuNDM1QzM3MS4zNzkgMzU2LjE3MiAzNzEuMTA3IDM1NC44MTYgMzcxLjEwNyAzNTMuNDQ2WiIgZmlsbD0iIzE4MTcxNiIvPgo8cGF0aCBkPSJNNDU0Ljc0NiAzMDMuNTE2TDQyMi4wNzUgMjc4Ljg5MUw0MTQuODI4IDI4Mi43MDVDNDE3LjI2IDI4My40NzYgNDE5LjQxIDI4NC45NDggNDIxLjAwNyAyODYuOTM4QzQyMi42MDQgMjg4LjkyNyA0MjMuNTc4IDI5MS4zNDUgNDIzLjgwNCAyOTMuODg2QzQyNC4wMyAyOTYuNDI3IDQyMy41IDI5OC45NzkgNDIyLjI4IDMwMS4yMTlDNDIxLjA1OSAzMDMuNDYgNDE5LjIwMyAzMDUuMjg5IDQxNi45NDYgMzA2LjQ3N0M0MTQuNjg4IDMwNy42NjUgNDEyLjEyOSAzMDguMTU5IDQwOS41OTIgMzA3Ljg5N0M0MDcuMDU0IDMwNy42MzQgNDA0LjY1IDMwNi42MjcgNDAyLjY4NCAzMDUuMDAxQzQwMC43MTcgMzAzLjM3NiAzOTkuMjc2IDMwMS4yMDUgMzk4LjU0IDI5OC43NjJDMzk3LjgwNCAyOTYuMzE5IDM5Ny44MDggMjkzLjcxMyAzOTguNTUgMjkxLjI3MkwzOTEuMDc3IDI5NS4yMDRDMzg4LjQxMiAyOTYuNTA0IDM4NS42MzQgMjk3LjU1OSAzODIuNzc3IDI5OC4zNTVMNDMxLjE1NCAzMzQuODE5QzQzMy4yMDYgMzM2LjQwOSA0MzUuNTUzIDMzNy41NzYgNDM4LjA2IDMzOC4yNTFDNDQwLjU2NiAzMzguOTI3IDQ0My4xODIgMzM5LjA5OCA0NDUuNzU1IDMzOC43NTRDNDQ4LjMyOCAzMzguNDEgNDUwLjgwNyAzMzcuNTU5IDQ1My4wNDggMzM2LjI0OUM0NTUuMjkgMzM0LjkzOSA0NTcuMjQ4IDMzMy4xOTcgNDU4LjgxMSAzMzEuMTI0QzQ2MC4zNzQgMzI5LjA1MiA0NjEuNTA5IDMyNi42ODkgNDYyLjE1MSAzMjQuMTc0QzQ2Mi43OTMgMzIxLjY1OCA0NjIuOTI5IDMxOS4wNDEgNDYyLjU1MSAzMTYuNDcyQzQ2Mi4xNzMgMzEzLjkwNCA0NjEuMjg4IDMxMS40MzcgNDU5Ljk0OSAzMDkuMjEzQzQ1OC42MDkgMzA2Ljk4OSA0NTYuODQyIDMwNS4wNTQgNDU0Ljc0OCAzMDMuNTE5TDQ1NC43NDYgMzAzLjUxNlpNNDUyLjU0NiAzMjYuNDAzQzQ1MS4wMDYgMzI4LjQ0NiA0NDguODk1IDMyOS45ODcgNDQ2LjQ4IDMzMC44M0M0NDQuMDY0IDMzMS42NzMgNDQxLjQ1MyAzMzEuNzgxIDQzOC45NzYgMzMxLjE0QzQzNi41IDMzMC40OTkgNDM0LjI2OSAzMjkuMTM5IDQzMi41NjUgMzI3LjIzQzQzMC44NjIgMzI1LjMyMSA0MjkuNzYzIDMyMi45NSA0MjkuNDA3IDMyMC40MTdDNDI5LjA1MSAzMTcuODgzIDQyOS40NTUgMzE1LjMwMSA0MzAuNTY2IDMxMi45OTdDNDMxLjY3OCAzMTAuNjkzIDQzMy40NDggMzA4Ljc3IDQzNS42NTMgMzA3LjQ3MkM0MzcuODU3IDMwNi4xNzQgNDQwLjM5NyAzMDUuNTU4IDQ0Mi45NTEgMzA1LjcwM0M0NDUuNTA1IDMwNS44NDkgNDQ3Ljk1OSAzMDYuNzQ4IDQ1MC4wMDIgMzA4LjI4OEM0NTEuMzU5IDMwOS4zMSA0NTIuNTAyIDMxMC41ODkgNDUzLjM2NSAzMTIuMDUyQzQ1NC4yMjcgMzEzLjUxNiA0NTQuNzkzIDMxNS4xMzUgNDU1LjAzIDMxNi44MTdDNDU1LjI2NyAzMTguNDk5IDQ1NS4xNzEgMzIwLjIxMiA0NTQuNzQ2IDMyMS44NTZDNDU0LjMyMSAzMjMuNTAxIDQ1My41NzYgMzI1LjA0NiA0NTIuNTU0IDMyNi40MDNINDUyLjU0NloiIGZpbGw9IiMxODE3MTYiLz4KPHBhdGggZD0iTTM4NC44NTQgMjg5LjY3MkMzODQuOTU0IDI4OS42MjIgMzg1LjA1NCAyODkuNTcyIDM4NS4xNiAyODkuNTI1TDQ1Ny40NDUgMjUxLjgyNUM0NTkuNzQgMjUwLjY0MiA0NjEuNzc5IDI0OS4wMTcgNDYzLjQ0NCAyNDcuMDQ0QzQ2NS4xMDkgMjQ1LjA3MSA0NjYuMzY4IDI0Mi43ODggNDY3LjE0OCAyNDAuMzI3QzQ2Ny45MjkgMjM3Ljg2NiA0NjguMjE1IDIzNS4yNzUgNDY3Ljk5MSAyMzIuNzAzQzQ2Ny43NjcgMjMwLjEzMSA0NjcuMDM3IDIyNy42MjggNDY1Ljg0MyAyMjUuMzM5QzQ2NC42NDkgMjIzLjA1IDQ2My4wMTUgMjIxLjAxOSA0NjEuMDM0IDIxOS4zNjNDNDU5LjA1MiAyMTcuNzA4IDQ1Ni43NjQgMjE2LjQ2IDQ1NC4yOTkgMjE1LjY5MUM0NTEuODM0IDIxNC45MjMgNDQ5LjI0MiAyMTQuNjQ5IDQ0Ni42NyAyMTQuODg1QzQ0NC4wOTkgMjE1LjEyMiA0NDEuNiAyMTUuODY0IDQzOS4zMTcgMjE3LjA2OUwzOTguMzYgMjM4LjQzMVYxOTEuNDYyQzM5OC4zNiAxODYuMjY0IDM5Ni4yOTUgMTgxLjI3OCAzOTIuNjE5IDE3Ny42MDNDMzg4Ljk0NCAxNzMuOTI3IDM4My45NTggMTcxLjg2MiAzNzguNzYgMTcxLjg2MkMzNzMuNTYyIDE3MS44NjIgMzY4LjU3NiAxNzMuOTI3IDM2NC45MDEgMTc3LjYwM0MzNjEuMjI1IDE4MS4yNzggMzU5LjE2IDE4Ni4yNjQgMzU5LjE2IDE5MS40NjJWMjYyLjI4NkMzNTcuNDkzIDI2NS4xNDYgMzU2LjU3OCAyNjguMzgyIDM1Ni41IDI3MS42OTFDMzU2LjQyMyAyNzUuMDAxIDM1Ny4xODUgMjc4LjI3NiAzNTguNzE3IDI4MS4yMTFDMzU4Ljg1NyAyODEuNDc4IDM1OS4wMSAyODEuNzMzIDM1OS4xNiAyODEuOTkxTDM1OS4zMjMgMjgyLjI3OUMzNjEuNzM5IDI4Ni4yOTQgMzY1LjUxNyAyODkuMzA4IDM2OS45NjkgMjkwLjc3MkMzNzQuNDIxIDI5Mi4yMzUgMzc5LjI1MSAyOTIuMDUxIDM4My41NzggMjkwLjI1M0wzODQuODU0IDI4OS42NzJaTTM3OC43NiAyODMuNzA4QzM3Ni4yMDEgMjgzLjcwOCAzNzMuNyAyODIuOTQ5IDM3MS41NzMgMjgxLjUyOEMzNjkuNDQ2IDI4MC4xMDYgMzY3Ljc4OCAyNzguMDg2IDM2Ni44MDkgMjc1LjcyMkMzNjUuODMgMjczLjM1OCAzNjUuNTczIDI3MC43NTcgMzY2LjA3MyAyNjguMjQ4QzM2Ni41NzIgMjY1LjczOCAzNjcuODA0IDI2My40MzMgMzY5LjYxMyAyNjEuNjI0QzM3MS40MjIgMjU5LjgxNSAzNzMuNzI3IDI1OC41ODMgMzc2LjIzNyAyNTguMDg0QzM3OC43NDYgMjU3LjU4NSAzODEuMzQ3IDI1Ny44NDIgMzgzLjcxMSAyNTguODIxQzM4Ni4wNzUgMjU5LjggMzg4LjA5NSAyNjEuNDU4IDM4OS41MTYgMjYzLjU4NkMzOTAuOTM4IDI2NS43MTMgMzkxLjY5NiAyNjguMjE0IDM5MS42OTYgMjcwLjc3M0MzOTEuNjk2IDI3Mi40NzIgMzkxLjM2MSAyNzQuMTU0IDM5MC43MTEgMjc1LjcyM0MzOTAuMDYxIDI3Ny4yOTIgMzg5LjEwOCAyNzguNzE4IDM4Ny45MDcgMjc5LjkyQzM4Ni43MDYgMjgxLjEyMSAzODUuMjggMjgyLjA3NCAzODMuNzEgMjgyLjcyM0MzODIuMTQxIDI4My4zNzMgMzgwLjQ1OSAyODMuNzA4IDM3OC43NiAyODMuNzA4Wk0zNzguNzYgMjQ0LjUwOEMzNzYuMjAxIDI0NC41MDggMzczLjcgMjQzLjc0OSAzNzEuNTczIDI0Mi4zMjhDMzY5LjQ0NiAyNDAuOTA2IDM2Ny43ODggMjM4Ljg4NiAzNjYuODA5IDIzNi41MjJDMzY1LjgzIDIzNC4xNTggMzY1LjU3MyAyMzEuNTU3IDM2Ni4wNzMgMjI5LjA0OEMzNjYuNTcyIDIyNi41MzkgMzY3LjgwNCAyMjQuMjM0IDM2OS42MTMgMjIyLjQyNUMzNzEuNDIyIDIyMC42MTYgMzczLjcyNyAyMTkuMzg0IDM3Ni4yMzYgMjE4Ljg4NEMzNzguNzQ2IDIxOC4zODUgMzgxLjM0NyAyMTguNjQxIDM4My43MSAyMTkuNjIxQzM4Ni4wNzQgMjIwLjYgMzg4LjA5NCAyMjIuMjU4IDM4OS41MTYgMjI0LjM4NUMzOTAuOTM3IDIyNi41MTIgMzkxLjY5NiAyMjkuMDEzIDM5MS42OTYgMjMxLjU3MkMzOTEuNjk2IDIzMy4yNzEgMzkxLjM2MiAyMzQuOTUzIDM5MC43MTIgMjM2LjUyM0MzOTAuMDYyIDIzOC4wOTMgMzg5LjEwOSAyMzkuNTE5IDM4Ny45MDggMjQwLjcyQzM4Ni43MDcgMjQxLjkyMiAzODUuMjggMjQyLjg3NSAzODMuNzExIDI0My41MjVDMzgyLjE0MSAyNDQuMTc1IDM4MC40NTkgMjQ0LjUxIDM3OC43NiAyNDQuNTFWMjQ0LjUwOFpNMzc4Ljc2IDIwNS4zMDhDMzc2LjIwMSAyMDUuMzA4IDM3My43IDIwNC41NDkgMzcxLjU3MyAyMDMuMTI4QzM2OS40NDYgMjAxLjcwNiAzNjcuNzg4IDE5OS42ODYgMzY2LjgwOSAxOTcuMzIyQzM2NS44MyAxOTQuOTU4IDM2NS41NzMgMTkyLjM1NyAzNjYuMDczIDE4OS44NDhDMzY2LjU3MiAxODcuMzM5IDM2Ny44MDQgMTg1LjAzNCAzNjkuNjEzIDE4My4yMjVDMzcxLjQyMiAxODEuNDE2IDM3My43MjcgMTgwLjE4NCAzNzYuMjM2IDE3OS42ODRDMzc4Ljc0NiAxNzkuMTg1IDM4MS4zNDcgMTc5LjQ0MSAzODMuNzEgMTgwLjQyMUMzODYuMDc0IDE4MS40IDM4OC4wOTQgMTgzLjA1OCAzODkuNTE2IDE4NS4xODVDMzkwLjkzNyAxODcuMzEyIDM5MS42OTYgMTg5LjgxMyAzOTEuNjk2IDE5Mi4zNzJDMzkxLjY5NyAxOTQuMDcxIDM5MS4zNjIgMTk1Ljc1MyAzOTAuNzEyIDE5Ny4zMjNDMzkwLjA2MyAxOTguODkzIDM4OS4xMSAyMDAuMzIgMzg3LjkwOCAyMDEuNTIxQzM4Ni43MDcgMjAyLjcyMyAzODUuMjgxIDIwMy42NzYgMzgzLjcxMSAyMDQuMzI2QzM4Mi4xNDIgMjA0Ljk3NiAzODAuNDU5IDIwNS4zMTEgMzc4Ljc2IDIwNS4zMTFWMjA1LjMwOFpNNDE4Ljc5OCAyNjQuNDYxQzQxNi41MyAyNjUuNjQ0IDQxMy45NjIgMjY2LjEyOCA0MTEuNDE4IDI2NS44NTFDNDA4Ljg3NSAyNjUuNTc1IDQwNi40NzEgMjY0LjU1IDQwNC41MSAyNjIuOTA3QzQwMi41NDkgMjYxLjI2NCA0MDEuMTE5IDI1OS4wNzcgNDAwLjQwMSAyNTYuNjIxQzM5OS42ODMgMjU0LjE2NiAzOTkuNzEgMjUxLjU1MyA0MDAuNDc3IDI0OS4xMTJDNDAxLjI0NCAyNDYuNjcyIDQwMi43MTggMjQ0LjUxNCA0MDQuNzEyIDI0Mi45MTFDNDA2LjcwNiAyNDEuMzA4IDQwOS4xMyAyNDAuMzMyIDQxMS42NzkgMjQwLjEwN0M0MTQuMjI3IDIzOS44ODIgNDE2Ljc4NSAyNDAuNDE4IDQxOS4wMjkgMjQxLjY0NkM0MjEuMjczIDI0Mi44NzUgNDIzLjEwMiAyNDQuNzQyIDQyNC4yODUgMjQ3LjAxQzQyNS4wNzEgMjQ4LjUxNiA0MjUuNTUyIDI1MC4xNjIgNDI1LjcwMiAyNTEuODU1QzQyNS44NTIgMjUzLjU0NyA0MjUuNjY2IDI1NS4yNTMgNDI1LjE1NyAyNTYuODczQzQyNC42NDcgMjU4LjQ5NCA0MjMuODI0IDI1OS45OTkgNDIyLjczMiAyNjEuMzAxQzQyMS42NDEgMjYyLjYwMyA0MjAuMzA0IDI2My42NzggNDE4Ljc5OCAyNjQuNDY0VjI2NC40NjFaTTQ1My41NTQgMjQ2LjMzN0M0NTEuMjg1IDI0Ny41MiA0NDguNzE3IDI0OC4wMDQgNDQ2LjE3MyAyNDcuNzI3QzQ0My42MyAyNDcuNDUxIDQ0MS4yMjYgMjQ2LjQyNiA0MzkuMjY0IDI0NC43ODNDNDM3LjMwMyAyNDMuMTQgNDM1Ljg3MyAyNDAuOTUyIDQzNS4xNTUgMjM4LjQ5NkM0MzQuNDM4IDIzNi4wNDEgNDM0LjQ2NCAyMzMuNDI3IDQzNS4yMzIgMjMwLjk4NkM0MzUuOTk5IDIyOC41NDYgNDM3LjQ3MyAyMjYuMzg3IDQzOS40NjcgMjI0Ljc4NEM0NDEuNDYyIDIyMy4xODIgNDQzLjg4NiAyMjIuMjA2IDQ0Ni40MzUgMjIxLjk4MUM0NDguOTg0IDIyMS43NTYgNDUxLjU0MiAyMjIuMjkyIDQ1My43ODYgMjIzLjUyMUM0NTYuMDMgMjI0Ljc1IDQ1Ny44NTkgMjI2LjYxNyA0NTkuMDQyIDIyOC44ODZDNDU5LjgyOCAyMzAuMzkyIDQ2MC4zMDkgMjMyLjAzOCA0NjAuNDU4IDIzMy43M0M0NjAuNjA3IDIzNS40MjIgNDYwLjQyMiAyMzcuMTI3IDQ1OS45MTIgMjM4Ljc0OEM0NTkuNDAzIDI0MC4zNjggNDU4LjU3OSAyNDEuODczIDQ1Ny40ODggMjQzLjE3NUM0NTYuMzk3IDI0NC40NzcgNDU1LjA2IDI0NS41NTEgNDUzLjU1NCAyNDYuMzM3WiIgZmlsbD0iIzE4MTcxNiIvPgo8cGF0aCBkPSJNMzcxLjEwNyAyNzQuMzQ1QzM3MS4xMDYgMjcyLjI4MiAzNzEuNzE3IDI3MC4yNjUgMzcyLjg2NSAyNjguNTUxQzM3NC4wMTIgMjY2LjgzNiAzNzUuNjQyIDI2NS41MDEgMzc3LjU1IDI2NC43MTVDMzc5LjQ1NyAyNjMuOTI5IDM4MS41NTUgMjYzLjcyNyAzODMuNTc3IDI2NC4xMzZDMzg1LjU5OSAyNjQuNTQ0IDM4Ny40NTQgMjY1LjU0NCAzODguOTA3IDI2Ny4wMDlDMzg4LjMxOCAyNjUuNTg5IDM4Ny40MjIgMjY0LjMxNiAzODYuMjgyIDI2My4yODNDMzg1LjE0MyAyNjIuMjUxIDM4My43ODkgMjYxLjQ4MyAzODIuMzE4IDI2MS4wMzZDMzgwLjg0NyAyNjAuNTg5IDM3OS4yOTQgMjYwLjQ3MyAzNzcuNzczIDI2MC42OTdDMzc2LjI1MiAyNjAuOTIxIDM3NC43OTkgMjYxLjQ4IDM3My41MTkgMjYyLjMzMkMzNzIuMjM5IDI2My4xODUgMzcxLjE2NCAyNjQuMzEgMzcwLjM3MSAyNjUuNjI4QzM2OS41NzggMjY2Ljk0NiAzNjkuMDg3IDI2OC40MjIgMzY4LjkzMyAyNjkuOTUyQzM2OC43NzkgMjcxLjQ4MiAzNjguOTY2IDI3My4wMjggMzY5LjQ4IDI3NC40NzdDMzY5Ljk5NCAyNzUuOTI2IDM3MC44MjMgMjc3LjI0MyAzNzEuOTA3IDI3OC4zMzRDMzcxLjM3OSAyNzcuMDcgMzcxLjEwNyAyNzUuNzE1IDM3MS4xMDcgMjc0LjM0NVoiIGZpbGw9IiMxODE3MTYiLz4KPHBhdGggZD0iTTQwNS4zMTMgMjU2LjkxNkM0MDUuMzEyIDI1NC44NTMgNDA1LjkyNCAyNTIuODM2IDQwNy4wNzEgMjUxLjEyMkM0MDguMjE4IDI0OS40MDcgNDA5Ljg0OSAyNDguMDcyIDQxMS43NTYgMjQ3LjI4NkM0MTMuNjY0IDI0Ni41IDQxNS43NjEgMjQ2LjI5OSA0MTcuNzgzIDI0Ni43MDdDNDE5LjgwNSAyNDcuMTE2IDQyMS42NiAyNDguMTE2IDQyMy4xMTMgMjQ5LjU4MUM0MjIuNTI0IDI0OC4xNiA0MjEuNjI4IDI0Ni44ODggNDIwLjQ4OCAyNDUuODU1QzQxOS4zNDkgMjQ0LjgyMiA0MTcuOTk1IDI0NC4wNTUgNDE2LjUyNCAyNDMuNjA4QzQxNS4wNTMgMjQzLjE2IDQxMy41IDI0My4wNDUgNDExLjk3OSAyNDMuMjY5QzQxMC40NTggMjQzLjQ5MyA0MDkuMDA1IDI0NC4wNTIgNDA3LjcyNSAyNDQuOTA0QzQwNi40NDUgMjQ1Ljc1NyA0MDUuMzcgMjQ2Ljg4MiA0MDQuNTc3IDI0OC4yQzQwMy43ODQgMjQ5LjUxNyA0MDMuMjkzIDI1MC45OTQgNDAzLjEzOSAyNTIuNTI0QzQwMi45ODUgMjU0LjA1NCA0MDMuMTcyIDI1NS41OTkgNDAzLjY4NiAyNTcuMDQ5QzQwNC4yIDI1OC40OTggNDA1LjAyOSAyNTkuODE1IDQwNi4xMTMgMjYwLjkwNkM0MDUuNTg1IDI1OS42NDIgNDA1LjMxMyAyNTguMjg2IDQwNS4zMTMgMjU2LjkxNloiIGZpbGw9IiMxODE3MTYiLz4KPHBhdGggZD0iTTQzOS44MjEgMjM4Ljg2MUM0MzkuODIgMjM2Ljc5OCA0NDAuNDMxIDIzNC43ODEgNDQxLjU3OSAyMzMuMDY2QzQ0Mi43MjYgMjMxLjM1MiA0NDQuMzU2IDIzMC4wMTcgNDQ2LjI2NCAyMjkuMjNDNDQ4LjE3MSAyMjguNDQ0IDQ1MC4yNjkgMjI4LjI0MyA0NTIuMjkxIDIyOC42NTFDNDU0LjMxMyAyMjkuMDYgNDU2LjE2OCAyMzAuMDYgNDU3LjYyMSAyMzEuNTI1QzQ1Ny4wMzIgMjMwLjEwNCA0NTYuMTM2IDIyOC44MzIgNDU0Ljk5NiAyMjcuNzk5QzQ1My44NTcgMjI2Ljc2NiA0NTIuNTAzIDIyNS45OTkgNDUxLjAzMiAyMjUuNTUxQzQ0OS41NjEgMjI1LjEwNCA0NDguMDA4IDIyNC45ODkgNDQ2LjQ4NyAyMjUuMjEzQzQ0NC45NjYgMjI1LjQzNyA0NDMuNTEzIDIyNS45OTUgNDQyLjIzMyAyMjYuODQ4QzQ0MC45NTMgMjI3LjcwMSA0MzkuODc4IDIyOC44MjYgNDM5LjA4NSAyMzAuMTQ0QzQzOC4yOTIgMjMxLjQ2MSA0MzcuODAxIDIzMi45MzggNDM3LjY0NyAyMzQuNDY4QzQzNy40OTMgMjM1Ljk5OCA0MzcuNjggMjM3LjU0MyA0MzguMTk0IDIzOC45OTJDNDM4LjcwOCAyNDAuNDQyIDQzOS41MzcgMjQxLjc1OSA0NDAuNjIxIDI0Mi44NUM0NDAuMDkzIDI0MS41ODYgNDM5LjgyMSAyNDAuMjMgNDM5LjgyMSAyMzguODYxWiIgZmlsbD0iIzE4MTcxNiIvPgo8cGF0aCBkPSJNNDM0LjgwMiAzMjIuNTE2QzQzNC44MDIgMzIwLjQ1NCA0MzUuNDE0IDMxOC40MzkgNDM2LjU2MSAzMTYuNzI1QzQzNy43MDggMzE1LjAxMiA0MzkuMzM4IDMxMy42NzggNDQxLjI0NCAzMTIuODkyQzQ0My4xNTEgMzEyLjEwNiA0NDUuMjQ3IDMxMS45MDQgNDQ3LjI2OCAzMTIuMzEyQzQ0OS4yOSAzMTIuNzE5IDQ1MS4xNDQgMzEzLjcxOCA0NTIuNTk3IDMxNS4xODFDNDUyLjAwOCAzMTMuNzYxIDQ1MS4xMTIgMzEyLjQ4OCA0NDkuOTcyIDMxMS40NTVDNDQ4LjgzMyAzMTAuNDIyIDQ0Ny40NzkgMzA5LjY1NSA0NDYuMDA4IDMwOS4yMDhDNDQ0LjUzNyAzMDguNzYxIDQ0Mi45ODQgMzA4LjY0NSA0NDEuNDYzIDMwOC44NjlDNDM5Ljk0MiAzMDkuMDkzIDQzOC40ODkgMzA5LjY1MiA0MzcuMjA5IDMxMC41MDRDNDM1LjkyOSAzMTEuMzU3IDQzNC44NTQgMzEyLjQ4MiA0MzQuMDYxIDMxMy44QzQzMy4yNjggMzE1LjExNyA0MzIuNzc3IDMxNi41OTQgNDMyLjYyMyAzMTguMTI0QzQzMi40NjkgMzE5LjY1NCA0MzIuNjU2IDMyMS4xOTkgNDMzLjE3IDMyMi42NDlDNDMzLjY4NCAzMjQuMDk4IDQzNC41MTMgMzI1LjQxNSA0MzUuNTk3IDMyNi41MDZDNDM1LjA3MiAzMjUuMjQxIDQzNC44MDEgMzIzLjg4NSA0MzQuODAyIDMyMi41MTZaIiBmaWxsPSIjMTgxNzE2Ii8+CjxwYXRoIGQ9Ik00MDMuMDgzIDI5OC43NDRDNDAzLjA4MiAyOTYuNjgxIDQwMy42OTQgMjk0LjY2NCA0MDQuODQxIDI5Mi45NUM0MDUuOTg4IDI5MS4yMzUgNDA3LjYxOSAyODkuOTAxIDQwOS41MjYgMjg5LjExNUM0MTEuNDMzIDI4OC4zMjkgNDEzLjUzMSAyODguMTI3IDQxNS41NTMgMjg4LjUzNkM0MTcuNTc1IDI4OC45NDQgNDE5LjQzIDI4OS45NDQgNDIwLjg4MyAyOTEuNDA5QzQyMC4yOTQgMjg5Ljk4OSA0MTkuMzk4IDI4OC43MTYgNDE4LjI1OCAyODcuNjgzQzQxNy4xMTkgMjg2LjY1IDQxNS43NjUgMjg1Ljg4MyA0MTQuMjk0IDI4NS40MzZDNDEyLjgyMyAyODQuOTg5IDQxMS4yNyAyODQuODczIDQwOS43NDkgMjg1LjA5N0M0MDguMjI4IDI4NS4zMjEgNDA2Ljc3NSAyODUuODggNDA1LjQ5NSAyODYuNzMyQzQwNC4yMTUgMjg3LjU4NSA0MDMuMTQgMjg4LjcxIDQwMi4zNDcgMjkwLjAyOEM0MDEuNTU0IDI5MS4zNDUgNDAxLjA2MyAyOTIuODIyIDQwMC45MDkgMjk0LjM1MkM0MDAuNzU1IDI5NS44ODIgNDAwLjk0MiAyOTcuNDI3IDQwMS40NTYgMjk4Ljg3N0M0MDEuOTcgMzAwLjMyNiA0MDIuNzk5IDMwMS42NDMgNDAzLjg4MyAzMDIuNzM0QzQwMy4zNTUgMzAxLjQ3IDQwMy4wODMgMzAwLjExNCA0MDMuMDgzIDI5OC43NDRaIiBmaWxsPSIjMTgxNzE2Ii8+CjxwYXRoIGQ9Ik0zNzYuNjcgMzA0LjE3NUwzNzMuMTQ2IDMwMS42NDVDMzcxLjkzNSAzMDIuNTI4IDM3MC45MyAzMDMuNjYzIDM3MC4xOTggMzA0Ljk3MUMzNjkuNDY3IDMwNi4yNzkgMzY5LjAyNyAzMDcuNzMgMzY4LjkwOSAzMDkuMjI0QzM2OC43OTEgMzEwLjcxOCAzNjguOTk4IDMxMi4yMiAzNjkuNTE0IDMxMy42MjZDMzcwLjAzMSAzMTUuMDMzIDM3MC44NDYgMzE2LjMxMiAzNzEuOTAzIDMxNy4zNzRDMzcwLjkwNiAzMTQuOTc2IDM3MC44NDIgMzEyLjI5MSAzNzEuNzI0IDMwOS44NDlDMzcyLjYwNiAzMDcuNDA2IDM3NC4zNzEgMzA1LjM4MiAzNzYuNjcgMzA0LjE3NFYzMDQuMTc1WiIgZmlsbD0iIzE4MTcxNiIvPgo8cGF0aCBkPSJNNTY3Ljg0NSAyNjYuNDkxVjI3OC43MDdINTY2LjE1NFYyNjYuNDkxSDU2MS44MVYyNjQuODc4SDU3Mi4xOTJWMjY2LjQ5MUg1NjcuODQ1WiIgZmlsbD0iIzE4MTcxNiIvPgo8cGF0aCBkPSJNNTg3LjQ0IDI3OC43MDdINTg1Ljc0NlYyNjcuMTI5TDU4MS43IDI3OC43MDdINTc5Ljg4N0w1NzUuODQxIDI2Ny4xMjlWMjc4LjcwN0g1NzQuMTQ4VjI2NC44NzhINTc2LjczOEw1ODAuODAzIDI3Ni41MzVMNTg0Ljg2OSAyNjQuODc4SDU4Ny40NFYyNzguNzA3WiIgZmlsbD0iIzE4MTcxNiIvPgo8cGF0aCBkPSJNNTg2Ljg2OSAzMTguODI0TDU4Ni4yNDUgMzE3LjM3M0M1ODYuMjM1IDMxNy4zNTEgNTg2LjIyIDMxNy4zMzMgNTg2LjIxIDMxNy4zMUM1ODMuMTI3IDMxMC4yODUgNTc4LjY5MSAzMDMuOTM2IDU3My4xNTUgMjk4LjYyNkM1NjcuNjE5IDI5My4zMTYgNTYxLjA5MSAyODkuMTQ4IDU1My45NDQgMjg2LjM2QzU0Ni43OTYgMjgzLjU3MyA1MzkuMTcgMjgyLjIyMSA1MzEuNTAxIDI4Mi4zOEM1MjMuODMxIDI4Mi41NCA1MTYuMjY4IDI4NC4yMDkgNTA5LjI0MyAyODcuMjkyTDUwOS4xODYgMjg3LjMxN0M0OTUuMTUgMjkzLjQ4NiA0ODQuMTAyIDMwNC45MjcgNDc4LjQyOCAzMTkuMTdDNDcyLjc1MyAzMzMuNDE0IDQ3Mi45MDcgMzQ5LjMxNyA0NzguODU1IDM2My40NDhDNDg0LjgwMyAzNzcuNTc5IDQ5Ni4wNyAzODguODA1IDUxMC4yMjIgMzk0LjcwMkM1MjQuMzc0IDQwMC42IDU0MC4yNzggNDAwLjY5NiA1NTQuNTAxIDM5NC45N0w1NTMuNTkxIDM5Ny4yN0M1NTMuNDI3IDM5Ny43MDIgNTUzLjQ0IDM5OC4xODEgNTUzLjYyNiAzOTguNjA0QzU1My44MTMgMzk5LjAyNyA1NTQuMTU5IDM5OS4zNiA1NTQuNTg4IDM5OS41M0M1NTUuMDE4IDM5OS43IDU1NS40OTggMzk5LjY5NCA1NTUuOTIzIDM5OS41MTNDNTU2LjM0OSAzOTkuMzMyIDU1Ni42ODYgMzk4Ljk5MSA1NTYuODYyIDM5OC41NjRMNTYxLjU2MiAzODYuNjgzQzU2MS42NDcgMzg2LjQ2NyA1NjEuNjg5IDM4Ni4yMzcgNTYxLjY4NSAzODYuMDA1QzU2MS42OCAzODUuNzczIDU2MS42MyAzODUuNTQ0IDU2MS41MzcgMzg1LjMzMkM1NjEuNDQ1IDM4NS4xMiA1NjEuMzEgMzg0LjkyOCA1NjEuMTQzIDM4NC43NjdDNTYwLjk3NiAzODQuNjA3IDU2MC43NzggMzg0LjQ4MSA1NjAuNTYyIDM4NC4zOTdMNTQ4LjcyNyAzNzkuODA0QzU0OC41MSAzNzkuNzIgNTQ4LjI3OCAzNzkuNjc5IDU0OC4wNDUgMzc5LjY4NUM1NDcuODEzIDM3OS42OTEgNTQ3LjU4MyAzNzkuNzQ0IDU0Ny4zNzEgMzc5LjgzOUg1NDcuMzU4QzU0Ny4wNDEgMzc5Ljk4MSA1NDYuNzc0IDM4MC4yMTMgNTQ2LjU4OSAzODAuNTA3QzU0Ni40MDQgMzgwLjggNTQ2LjMxIDM4MS4xNDIgNTQ2LjMxOSAzODEuNDg5QzU0Ni4zMjggMzgxLjgzNiA1NDYuNDM5IDM4Mi4xNzIgNTQ2LjYzOSAzODIuNDU2QzU0Ni44MzggMzgyLjc0IDU0Ny4xMTcgMzgyLjk1OCA1NDcuNDQxIDM4My4wODRMNTUwLjEwOSAzODQuMTJDNTQ1LjMyNyAzODYuMDQ5IDU0MC4yNTggMzg3LjE3MSA1MzUuMTA5IDM4Ny40NDFMNTM0LjkzNCAzODEuMjg3TDUzMy4wMTggMzgxLjM0TDUzMy4xOTQgMzg3LjUwM0M1MjcuNTc1IDM4Ny41NTUgNTIxLjk5MiAzODYuNTg5IDUxNi43MTcgMzg0LjY1M0w1MTguOTU2IDM3OC45MUw1MTcuMTczIDM3OC4yMUw1MTQuOTQgMzgzLjkzOEM1MDkuOTY2IDM4MS44OTUgNTA1LjM4NCAzNzkuMDA3IDUwMS4zOTUgMzc1LjQwMUw1MDUuNjM5IDM3MC45MDlMNTA0LjI0NyAzNjkuNTk0TDQ5OS45ODcgMzc0LjEwNkM0OTUuOTgyIDM3MC4xNTcgNDkyLjcyNSAzNjUuNTE2IDQ5MC4zNzUgMzYwLjQwNkw0OTYuMDI5IDM1Ny45MjZMNDk1LjI1OSAzNTYuMTc0TDQ4OS41ODUgMzU4LjY2M0M0ODcuNTE0IDM1My42OTUgNDg2LjMyIDM0OC40MDYgNDg2LjA1NCAzNDMuMDMxTDQ5Mi4yNjggMzQyLjg1M0w0OTIuMjEyIDM0MC45MzlMNDg1Ljk5OCAzNDEuMTE4QzQ4NS45NjIgMzM1LjQ5NSA0ODYuOTQ1IDMyOS45MTEgNDg4Ljg5OCAzMjQuNjM4TDQ5NC42NTQgMzI2Ljg4NUw0OTUuMzU0IDMyNS4xMDNMNDg5LjYzMiAzMjIuODY5QzQ5MS42ODYgMzE3LjkwNCA0OTQuNTg0IDMxMy4zMzIgNDk4LjE5OCAzMDkuMzU1TDUwMi42NTYgMzEzLjU2N0w1MDMuOTY5IDMxMi4xNzVMNDk5LjUwNCAzMDcuOTU3QzUwMy40NTQgMzAzLjk3IDUwOC4wOTEgMzAwLjczIDUxMy4xOTIgMjk4LjM5MUw1MTUuNjM0IDMwMy45NThMNTE3LjM4NyAzMDMuMTg4TDUxNC45MzkgMjk3LjYwOUM1MTkuODk3IDI5NS41NTQgNTI1LjE3MiAyOTQuMzcgNTMwLjUzMyAyOTQuMTA5TDUzMC43MDYgMzAwLjE5MUw1MzIuNjIgMzAwLjEzNkw1MzIuNDQ3IDI5NC4wNTZDNTM4LjA1MSAyOTQuMDI3IDU0My42MTQgMjk1LjAxIDU0OC44NjkgMjk2Ljk1Nkw1NDYuNjggMzAyLjU3TDU0OC40NjIgMzAzLjI2NUw1NTAuNjQxIDI5Ny42NzhDNTU1LjU4OSAyOTkuNzI1IDU2MC4xNDcgMzAyLjYxMSA1NjQuMTE1IDMwNi4yMDdMNTU5Ljk5NyAzMTAuNTY4TDU2MS4zODkgMzExLjg4MUw1NjUuNTE4IDMwNy41MDlDNTY4LjI5NyAzMTAuMjYyIDU3MC43MTYgMzEzLjM1NSA1NzIuNzE4IDMxNi43MTVMNTM5LjY1MyAzMzAuODIzQzUzNy40OTEgMzI5LjQ2NiA1MzQuOTUyIDMyOC44MzcgNTMyLjQwNiAzMjkuMDI5QzUyOS44NjEgMzI5LjIyMSA1MjcuNDQ1IDMzMC4yMjQgNTI1LjUxMSAzMzEuODlDNTIzLjU3OCAzMzMuNTU2IDUyMi4yMjkgMzM1Ljc5OSA1MjEuNjY0IDMzOC4yODhDNTIxLjA5OCAzNDAuNzc2IDUyMS4zNDUgMzQzLjM4MSA1MjIuMzY4IDM0NS43MTlDNTIzLjM5MiAzNDguMDU4IDUyNS4xMzcgMzUwLjAwNiA1MjcuMzUgMzUxLjI4QzUyOS41NjIgMzUyLjU1MyA1MzIuMTI0IDM1My4wODQgNTM0LjY2IDM1Mi43OTRDNTM3LjE5NiAzNTIuNTA0IDUzOS41NzIgMzUxLjQxIDU0MS40NCAzNDkuNjdDNTQzLjMwOCAzNDcuOTMxIDU0NC41NjkgMzQ1LjYzOSA1NDUuMDM5IDM0My4xM0w1ODMuNzc0IDMyNi42MDFDNTg1LjIxNCAzMjUuOTc5IDU4Ni4zNDkgMzI0LjgxIDU4Ni45MjkgMzIzLjM1MkM1ODcuNTEgMzIxLjg5NCA1ODcuNDg4IDMyMC4yNjYgNTg2Ljg2OSAzMTguODI0WiIgZmlsbD0iIzE4MTcxNiIvPgo8cGF0aCBkPSJNNTg3LjQ0IDBIMTcwLjA2VjUuNjY5SDU4Ny40NFYwWiIgZmlsbD0iIzAwNkNCNyIvPgo8cGF0aCBkPSJNNDU4LjM0MSAxMzYuMDYySDE3MC4wNlYxNDEuNzMxSDQ1OC4zNDFWMTM2LjA2MloiIGZpbGw9IiMwMDZDQjciLz4KPHBhdGggZD0iTTU4Ny40MzkgMTM2LjA2Mkg0OTYuMTQ3VjE0MS43MzFINTg3LjQzOVYxMzYuMDYyWiIgZmlsbD0iIzAwNkNCNyIvPgo8cGF0aCBkPSJNMjAxLjYwNCA4MS44NDUxSDIxMi44OThDMjEyLjg5OCA4OC41NjcxIDIxMC45MyA5Mi45NjcxIDIwNi45OTMgOTUuMDQ1MUMyMDQuMTkzIDk2LjUzNTEgMTk4Ljg1MyA5Ny4yNzg0IDE5MC45NzIgOTcuMjc1MUMxODIuMTQ3IDk3LjI3NTEgMTc2LjI0MSA5NS40NTgxIDE3My4yNTYgOTEuODI0MUMxNzAuNjI4IDg4LjY3MDcgMTY5LjMxNiA4Mi41Mzc0IDE2OS4zMjEgNzMuNDI0MUMxNjkuMzIxIDY0LjM4MDcgMTcwLjU3NCA1OC4yNDkxIDE3My4wODEgNTUuMDI5MUMxNzUuOTk5IDUxLjIxMzcgMTgxLjk2MyA0OS4zMDc0IDE5MC45NzIgNDkuMzEwMUMyMDAuMzk5IDQ5LjMxMDEgMjA2LjQ4NyA1MS4wOTI3IDIwOS4yMzUgNTQuNjU4MUMyMTEuNjc3IDU3LjgwNjEgMjEyLjg5OCA2NC42OTM3IDIxMi44OTggNzUuMzIxMUgxODAuNTM1QzE4MC41MzUgODAuODEzNyAxODEuMDE0IDg0LjMwNDcgMTgxLjk3MiA4NS43OTQxQzE4My4yMjkgODcuNzAwNyAxODYuMjE3IDg4LjY1NDQgMTkwLjkzNyA4OC42NTUxQzE5NC44NzYgODguNjU1MSAxOTcuNDQ2IDg4LjM4ODQgMTk4LjY0NyA4Ny44NTUxQzIwMC42MTkgODYuOTc4NCAyMDEuNjA1IDg0Ljk3NTEgMjAxLjYwNCA4MS44NDUxWk0xODAuNTM1IDY4LjE3OTFIMjAxLjYyMkMyMDEuNjIyIDYzLjU4NjQgMjAxLjAyNCA2MC43MzA3IDE5OS44MjkgNTkuNjEyMUMxOTguNjM0IDU4LjQ5MzQgMTk1LjY3MiA1Ny45MzQ0IDE5MC45NDUgNTcuOTM1MUMxODYuMjc4IDU3LjkzNTEgMTgzLjMxOCA1OC42MTExIDE4Mi4wNjUgNTkuOTYzMUMxODEuMDQ1IDYxLjA4OTcgMTgwLjUzNSA2My44Mjg0IDE4MC41MzUgNjguMTc5MVoiIGZpbGw9IiMxODE3MTYiLz4KPHBhdGggZD0iTTI1NC40ODIgOTYuNzkyMUwyNTQuODI1IDg5LjcxOTFIMjU0LjQ4MkMyNTIuMTU0IDk0Ljc2MTggMjQ3LjI1OSA5Ny4yODE0IDIzOS43OTYgOTcuMjc4MUMyMzEuOTE4IDk3LjI3ODEgMjI2LjcyNyA5NC44MzY0IDIyNC4yMjQgODkuOTUzMUMyMjIuNjA4IDg2LjgwMzEgMjIxLjgwMSA4MC43ODk4IDIyMS44MDIgNzEuOTEzMUMyMjEuODAyIDY0LjExMzEgMjIyLjc5IDU4LjYzNDggMjI0Ljc2NSA1NS40NzgxQzIyNy4zNCA1MS4zNjg4IDIzMi4zNjggNDkuMzE0OCAyMzkuODQ5IDQ5LjMxNjFDMjQ3LjM4NyA0OS4zMTYxIDI1Mi4xMTUgNTEuNTY4NCAyNTQuMDM0IDU2LjA3MzFIMjU0LjQ4MlYyOS42NDExSDI2NS42OThWOTYuNzkyMUgyNTQuNDgyWk0yNDMuMjA1IDU3LjkzNTFDMjM4LjY2MSA1Ny45MzUxIDIzNS43MjEgNTkuMjEyNCAyMzQuMzg2IDYxLjc2NzFDMjMzLjQ3NiA2My40ODkxIDIzMy4wMjEgNjYuODczNCAyMzMuMDIyIDcxLjkyMDFDMjMzLjAyMiA3OC4zMjk0IDIzMy40MTYgODIuNDU1OCAyMzQuMjAzIDg0LjI5OTFDMjM1LjQ3NCA4Ny4yMDkxIDIzOC40NzQgODguNjYzMSAyNDMuMjAzIDg4LjY2MTFDMjQ4LjUzNiA4OC42NjExIDI1MS44NyA4Ny4yNjYxIDI1My4yMDMgODQuNDc2MUMyNTQuMDU2IDgyLjY5NTQgMjU0LjQ4MiA3OC41MTAxIDI1NC40OCA3MS45MjAxQzI1NC40OCA2Ni44MTYxIDI1My45MDQgNjMuMzcyMSAyNTIuNzUyIDYxLjU4ODFDMjUxLjIzNSA1OS4xNTM0IDI0OC4wNTMgNTcuOTM1OCAyNDMuMjA1IDU3LjkzNTFaIiBmaWxsPSIjMTgxNzE2Ii8+CjxwYXRoIGQ9Ik0zMTcuODY1IDk2Ljc5MjFIMzA2Ljk3NFY4OS41NDQxSDMwNi42NDhDMzA0LjQ5MyA5NC43MDAxIDI5OS41MiA5Ny4yNzgxIDI5MS43MyA5Ny4yNzgxQzI4MS4xODkgOTcuMjc4MSAyNzUuOTE5IDkyLjc3ODEgMjc1LjkyMiA4My43NzgxVjQ5LjgwNzFIMjg3LjEzMlY3OS4zNzAxQzI4Ny4xMzIgODMuMDA3NSAyODcuNTUzIDg1LjM5MDUgMjg4LjM5NCA4Ni41MTkxQzI4OS40MTEgODcuOTQ4MSAyOTEuNjE5IDg4LjY2MTEgMjk1LjAzNyA4OC42NjExQzI5OS4yMjYgODguNjYxMSAzMDIuMTg3IDg3Ljc1NDUgMzAzLjkyIDg1Ljk0MTFDMzA1LjY1MyA4NC4xMjc4IDMwNi41MjIgODEuMTAzNSAzMDYuNTI4IDc2Ljg2ODFMMzA2LjY0OCA0OS44MDcxSDMxNy44NjVWOTYuNzkyMVoiIGZpbGw9IiMxODE3MTYiLz4KPHBhdGggZD0iTTM1OC4yODUgNzguODk1OUgzNjkuNTg1QzM2OS41ODUgODYuNDUxMiAzNjcuODU0IDkxLjUwNzYgMzY0LjM5MyA5NC4wNjQ5QzM2MS41MjYgOTYuMjA1NiAzNTYuMTI2IDk3LjI3NjYgMzQ4LjE5MyA5Ny4yNzc5QzMzOS40MiA5Ny4yNzc5IDMzMy42MzIgOTUuNDMxOSAzMzAuODI5IDkxLjczOTlDMzI4LjM4OCA4OC41ODY2IDMyNy4xNjYgODIuNDU1MiAzMjcuMTYxIDczLjM0NTlDMzI3LjE2MSA2NC4zNTUzIDMyOC4zNTMgNTguMjgwOSAzMzAuNzM4IDU1LjEyMjlDMzMzLjY2NSA1MS4yNTI5IDMzOS40ODQgNDkuMzE3MyAzNDguMTkzIDQ5LjMxNTlDMzU1LjgyOSA0OS4zMTU5IDM2MS4xMzkgNTAuMjk3NiAzNjQuMTI0IDUyLjI2MDlDMzY3Ljc1OSA1NC42NDgzIDM2OS41NzggNTkuMzE4NiAzNjkuNTgyIDY2LjI3MTlIMzU4LjI4MkMzNTguMjgyIDYyLjY3MTkgMzU3LjQ3NSA2MC4zMzg2IDM1NS44NiA1OS4yNzE5QzM1NC42MDQgNTguMzgyNiAzNTIuMDMzIDU3LjkzODYgMzQ4LjE0OCA1Ny45Mzk5QzM0My42MDggNTcuOTM5OSAzNDAuNzcgNTkuMDA4OSAzMzkuNjMzIDYxLjE0NjlDMzM4Ljc5IDYyLjc1MTYgMzM4LjM3MSA2Ni44MTgyIDMzOC4zNzYgNzMuMzQ2OUMzMzguMzc2IDc5LjgxODIgMzM4Ljc2NSA4My44MjUyIDMzOS41NDIgODUuMzY3OUMzNDAuNjE2IDg3LjU2NzkgMzQzLjQ4NSA4OC42NjU5IDM0OC4xNDggODguNjYxOUMzNTIuNDUyIDg4LjY2MTkgMzU1LjIxNyA4OC4wODQ5IDM1Ni40NDMgODYuOTMwOUMzNTcuNjY5IDg1Ljc3NjkgMzU4LjI4MyA4My4wOTg2IDM1OC4yODUgNzguODk1OVoiIGZpbGw9IiMxODE3MTYiLz4KPHBhdGggZD0iTTQwOC4xNDggOTYuNzkyTDQwOC41MTIgOTAuODg0SDQwOC4yNDVDNDA3Ljc1IDkyLjIyMzMgNDA2LjkzOCA5My40MjMgNDA1Ljg3OSA5NC4zODA3QzQwNC44MTkgOTUuMzM4NCA0MDMuNTQ0IDk2LjAyNTcgNDAyLjE2MiA5Ni4zODRDMzk5LjM4NSA5Ny4wNzk1IDM5Ni41MjMgOTcuMzc5OCAzOTMuNjYyIDk3LjI3NkMzODcuNjMzIDk3LjI3NiAzODMuMzA3IDk2LjMyNDMgMzgwLjY4NCA5NC40MjFDMzc3LjY0IDkyLjIxNyAzNzYuMTE5IDg4LjIwMiAzNzYuMTIgODIuMzc2QzM3Ni4xMiA3Ni43ODczIDM3Ny43MDQgNzIuODkyMyAzODAuODczIDcwLjY5MUMzODMuNTA5IDY4LjkwNTYgMzg3Ljc4NiA2OC4wMTIzIDM5My43MDUgNjguMDExQzM5Ni40NDUgNjcuOTExNCAzOTkuMTg3IDY4LjE1MDkgNDAxLjg2OSA2OC43MjRDNDAzLjEyOCA2OS4wMjcgNDA0LjMwOCA2OS41OTYgNDA1LjMyOSA3MC4zOTI5QzQwNi4zNSA3MS4xODk4IDQwNy4xODkgNzIuMTk2IDQwNy43ODkgNzMuMzQ0SDQwOC4xNDhWNjcuMjUzQzQwOC4xNDggNjMuMTk3IDQwNy42NCA2MC41NDA2IDQwNi42MjUgNTkuMjg0QzQwNS4zNjQgNTcuNzM1MyA0MDIuNTIxIDU2Ljk1OTYgMzk4LjA5NiA1Ni45NTdDMzk1LjEwNSA1Ni45NTcgMzkzLjAxMiA1Ny4yODU2IDM5MS44MTYgNTcuOTQzQzM5MC4wODMgNTguODk5NiAzODkuMjE2IDYwLjc1MiAzODkuMjE2IDYzLjVIMzc3LjkxNkMzNzcuOTE2IDU3LjM3NCAzNzkuOTQ3IDUzLjI5OTYgMzg0LjAwOSA1MS4yNzdDMzg2LjYzNCA0OS45NjcgMzkxLjMxOSA0OS4zMTI2IDM5OC4wNjIgNDkuMzE0QzQwNi4xMTYgNDkuMzE0IDQxMS41NDcgNTAuMzU2NiA0MTQuMzU1IDUyLjQ0MkM0MTcuNjk4IDU0Ljg4OTMgNDE5LjM3IDU5Ljg2NjYgNDE5LjM3MSA2Ny4zNzRWOTYuNzlMNDA4LjE0OCA5Ni43OTJaTTM5Ny42OTkgNzUuNjUzQzM5My45NzEgNzUuNjUzIDM5MS41MzggNzUuOTIzMyAzOTAuMzk5IDc2LjQ2NEMzODguMzU4IDc3LjQyMDYgMzg3LjMzNyA3OS4zOTEgMzg3LjMzOCA4Mi4zNzVDMzg3LjMzOCA4NS41NDUgMzg4LjExOSA4Ny41NzYzIDM4OS42ODIgODguNDY5QzM5MS4wMDEgODkuMjQ2MyAzOTMuNjczIDg5LjYzNiAzOTcuNyA4OS42MzhDNDAxLjM2MiA4OS42MzggNDAzLjg1NCA4OS4yOCA0MDUuMTc3IDg4LjU2NEM0MDcuMTU2IDg3LjQ4OCA0MDguMTQ3IDg1LjQyNSA0MDguMTQ5IDgyLjM3NUM0MDguMTQ5IDc5LjQ0OSA0MDcuMDk4IDc3LjUwOTMgNDA0Ljk5NyA3Ni41NTZDNDAzLjY3MiA3NS45NTQgNDAxLjI0IDc1LjY1MyAzOTcuNjk5IDc1LjY1M1oiIGZpbGw9IiMxODE3MTYiLz4KPHBhdGggZD0iTTQyNC42OTMgNTguNDIyOVY0OS44MDY5SDQzMC41NTRWMzkuMjMzOUg0NDEuNzczVjQ5LjgwNjlINDU5Ljg2N1Y1OC40MjI5SDQ0MS43NjhWODIuNDE2OUM0NDEuNzY4IDg0Ljg1NTkgNDQxLjk3NSA4Ni40MzA5IDQ0Mi4zOTggODcuMTQzOUM0NDIuOTk4IDg4LjE1NTkgNDQ0LjQwOCA4OC42NjE2IDQ0Ni42MjcgODguNjYwOUM0NDkuNDQzIDg4LjY2MDkgNDUxLjE4NCA4Ny42MTgyIDQ1MS44NSA4NS41MzI5QzQ1Mi4yNDkgODMuMjk0IDQ1Mi4zOTcgODEuMDE3NiA0NTIuMjkxIDc4Ljc0NTlINDYyLjI4MUM0NjIuNDAyIDg1LjQyNzkgNDYxLjUwNSA5MC4wODI2IDQ1OS41OTIgOTIuNzA5OUM0NTcuMzc4IDk1Ljc1NjUgNDUzLjA3NSA5Ny4yNzkyIDQ0Ni42ODIgOTcuMjc3OUM0NDAuNTg5IDk3LjI3NzkgNDM2LjQzNyA5Ni4zNTQyIDQzNC4yMjUgOTQuNTA2OUM0MzEuNzc0IDkyLjQyNjkgNDMwLjU0OCA4OC40Mzg2IDQzMC41NDkgODIuNTQxOVY1OC40MjI5SDQyNC42OTNaIiBmaWxsPSIjMTgxNzE2Ii8+CjxwYXRoIGQ9Ik00ODIuMzIzIDI5LjY0MTFWMzkuMjM0MUg0NzEuMTAzVjI5LjY0MTFINDgyLjMyM1pNNDgyLjMyMyA0OS44MDcxVjk2Ljc5MjFINDcxLjEwM1Y0OS44MDcxSDQ4Mi4zMjNaIiBmaWxsPSIjMTgxNzE2Ii8+CjxwYXRoIGQ9Ik01MTMuMzU0IDQ5LjMxNTlDNTIyLjc4NCA0OS4zMTU5IDUyOC45MyA1MS4wNDQyIDUzMS43OTEgNTQuNTAwOUM1MzQuMjM5IDU3LjQ3NTYgNTM1LjQ2MyA2My43NTcyIDUzNS40NjMgNzMuMzQ1OUM1MzUuNDYzIDgyLjg2ODYgNTM0LjIzOSA4OS4xMTk2IDUzMS43OTEgOTIuMDk4OUM1MjguOTI0IDk1LjU1MDkgNTIyLjc3OSA5Ny4yNzcyIDUxMy4zNTQgOTcuMjc3OUM1MDMuOTI5IDk3LjI3ODYgNDk3Ljc4MiA5NS41NTIyIDQ5NC45MTMgOTIuMDk4OUM0OTIuNDY1IDg5LjEyNDIgNDkxLjI0MSA4Mi44NzMyIDQ5MS4yNDIgNzMuMzQ1OUM0OTEuMjQyIDYzLjc1NTkgNDkyLjQ2NiA1Ny40NzQyIDQ5NC45MTMgNTQuNTAwOUM0OTcuNzc4IDUxLjA0NDIgNTAzLjkyNSA0OS4zMTU5IDUxMy4zNTQgNDkuMzE1OVpNNTEzLjM1NCA1Ny45MzQ5QzUwOC41NSA1Ny45MzQ5IDUwNS40ODkgNTguOTQ0MiA1MDQuMTcxIDYwLjk2MjlDNTAzLjAyOCA2Mi43NDY5IDUwMi40NTkgNjYuOTAyNiA1MDIuNDYzIDczLjQyOTlDNTAyLjQ2MyA3OS45MDM5IDUwMy4wMzIgODQuMDAzOSA1MDQuMTcxIDg1LjcyOTlDNTA1LjQyOCA4Ny42ODU5IDUwOC40ODkgODguNjY0NiA1MTMuMzU0IDg4LjY2NTlDNTE4LjI3NiA4OC42NjU5IDUyMS4zNjUgODcuNjg3MyA1MjIuNjIyIDg1LjcyOTlDNTIzLjcwMiA4NC4wNjMzIDUyNC4yNDUgNzkuOTYzMiA1MjQuMjUgNzMuNDI5OUM1MjQuMjUgNjYuNzgyNiA1MjMuNzA3IDYyLjYyNjkgNTIyLjYyMiA2MC45NjI5QzUyMS4zMDYgNTguOTQ4MiA1MTguMjE3IDU3LjkzODkgNTEzLjM1NCA1Ny45MzQ5WiIgZmlsbD0iIzE4MTcxNiIvPgo8cGF0aCBkPSJNNTQ0Ljk1NCA0OS44MDY5SDU1Ni4xNjVWNTYuODc3OUg1NTYuNTI0QzU1Ni45ODggNTUuNDU2OCA1NTcuNzU4IDU0LjE1NDggNTU4Ljc3OSA1My4wNjM1QzU1OS44MDEgNTEuOTcyMyA1NjEuMDUgNTEuMTE4MyA1NjIuNDM3IDUwLjU2MTlDNTY1LjI4NSA0OS42MDU0IDU2OC4yODUgNDkuMTgyOSA1NzEuMjg2IDQ5LjMxNTlDNTc3LjI0NiA0OS4zMTU5IDU4MS40MTkgNTAuNTgyNiA1ODMuODA1IDUzLjExNTlDNTg2LjE5MSA1NS42NDkyIDU4Ny4zODQgNTkuODk1OSA1ODcuMzgzIDY1Ljg1NTlWOTYuNzg5OUg1NzYuMTY5VjY3LjA0NjlDNTc2LjE2OSA2My41MzM2IDU3NS41NzIgNjEuMTM2NiA1NzQuMzc4IDU5Ljg1NTlDNTczLjE4NCA1OC41NzUyIDU3MC44NTMgNTcuOTM0OSA1NjcuMzg1IDU3LjkzNDlDNTYyLjgzOCA1Ny45MzQ5IDU1OS43NTggNTkuMDM0OSA1NTguMTQ3IDYxLjIzNDlDNTU2LjgyNiA2My4wMjU2IDU1Ni4xNjcgNjYuMjcyMiA1NTYuMTY4IDcwLjk3NDlWOTYuNzg3OUg1NDQuOTU0VjQ5LjgwNjlaIiBmaWxsPSIjMTgxNzE2Ii8+CjxwYXRoIGQ9Ik01NzYuMzMzIDQ0Ljk4MzJWMzguNjcwMkg1NzMuOTc0VjM3LjgyNTJINTc5LjY0OFYzOC42NzAySDU3Ny4yOFY0NC45ODMySDU3Ni4zMzNaIiBmaWxsPSIjMTgxNzE2Ii8+CjxwYXRoIGQ9Ik01ODAuNTkxIDQ0Ljk4MzJWMzcuODI1Mkg1ODIuMDE2TDU4My43MTYgNDIuODkzMkM1ODMuODcyIDQzLjM2NjIgNTgzLjk4NiA0My43MTgyIDU4NC4wNTggNDMuOTUzMkM1ODQuMTM5IDQzLjY5MzIgNTg0LjI2NiA0My4zMTA1IDU4NC40MzggNDIuODA1Mkw1ODYuMTUyIDM3LjgyNTJINTg3LjQyN1Y0NC45ODMySDU4Ni41MTRWMzguOTkyMkw1ODQuNDMzIDQ0Ljk4MzJINTgzLjU3OUw1ODEuNTA5IDM4Ljg4OTJWNDQuOTgzMkg1ODAuNTkxWiIgZmlsbD0iIzE4MTcxNiIvPgo8cGF0aCBkPSJNMC45NjE5NzUgMC45NDQ4MjRWMTQwLjc4NkgxNDAuODAyVjAuOTQ0ODI0SDAuOTYxOTc1WiIgZmlsbD0id2hpdGUiLz4KPHBhdGggZD0iTTAuOTYxOTc1IDAuOTQ0ODI0VjE0MC43ODZIMTQwLjgwMlYwLjk0NDgyNEgwLjk2MTk3NVpNMTMxLjQ5OCA1OS4wNzM4QzEzMS4xMDMgNjMuNjQzNCAxMzAuMTUgNjguMTQ3NCAxMjguNjU5IDcyLjQ4NDhDMTIzLjc0MiA4Ny4wOTY4IDExOC4wNDEgOTYuMTUyOCAxMDQuODM3IDk2LjE1MjhDMTAwLjk1MSA5Ni4xNTI4IDk0LjA1NCA5NS4xMTk4IDkxLjUxNCA4OC4yMDM4TDkwLjkxNCA4Ni41NjQ4TDg5LjgzMSA4Ny45MzY4Qzg3LjgzMzQgOTAuNDk4NiA4NS4yODEzIDkyLjU3NDQgODIuMzY2NCA5NC4wMDgzQzc5LjQ1MTQgOTUuNDQyMiA3Ni4yNDk1IDk2LjE5NyA3My4wMDEgOTYuMjE1OEM2Ny45NjIgOTYuMjM5OCA2My45MTUgOTQuNTUwOCA2MS4zMDEgOTEuMzMyOEw2MC41ODIgOTAuNDQ5OEw1OS44MTggOTEuMjkzOEM1Ny4wMTggOTQuMzgxOCA1Mi4xNSA5Ni4xNTI4IDQ2LjQ1NCA5Ni4xNTI4QzQxLjk4MSA5Ni4xNTI4IDM4LjExOSA5NC42MzM4IDM1LjU3OCA5MS44NzU4TDM0Ljg4NSA5MS4xMjE4TDM0LjE2NSA5MS44NTA4QzMxLjM0IDk0LjcwMTggMjYuODg5IDk2LjEzOTggMjEuMjkzIDk2LjAwNzhDMTQuNTAzIDk1Ljg0NjggMTAuMzY5IDkyLjA1NzggMTAuMjM3IDg1Ljg2NzhDMTAuMDMxIDc2LjMyNDggMTkuMjY4IDU2LjI0ODggMjMuMDg5IDUwLjE0MzhDMjUuNTcyIDQ2LjA2NTggMjguOTg5IDQ0LjA4ODggMzMuNTI3IDQ0LjA4ODhDMzYuNjE5IDQ0LjA4ODggMzguNzMzIDQ0LjczNTggMzkuOTkgNDYuMDY1OEM0MS4xMzMgNDcuMjc1OCA0MS4zNiA0OC4yOTc4IDQxLjQ2MSA1MC43NTI4TDQxLjU5MiA1My45Mjc4TDQzLjI2NyA1MS4yMjc4QzQ3LjMyMiA0NC42OTM4IDU0LjA0MSA0My43OTM4IDYwLjY5OCA0My43OTM4QzY1LjMyNyA0My43OTM4IDY5LjM2NSA0NS40OTM4IDcwLjk4NyA0OC4xMjk4TDcxLjU4NyA0OS4xMDA4TDcyLjQ1NSA0OC4zNjI4Qzc2LjMyMzUgNDUuMjk3MiA4MS4xNTAxIDQzLjY5NTcgODYuMDg0IDQzLjg0MDhDOTEuOTMxIDQzLjg0MDggOTYuMTg0IDQ1LjI5NDggOTguNzE3IDQ4LjE2MThDOTkuMzMxOCA0OC44MTQ5IDk5LjgzNDUgNDkuNTY1IDEwMC4yMDUgNTAuMzgxOEwxMDAuODU2IDUxLjc0NzhMMTAxLjgzMiA1MC41OTI4QzEwNS41NDIgNDYuMjAyOCAxMTAuNjExIDQzLjk3NzggMTE2Ljg5OSA0My45Nzc4QzEyMS44NzkgNDMuOTc3OCAxMjUuNjYgNDUuMzAwOCAxMjguMTM1IDQ3LjkxMDhDMTMxLjIyOSA1MS4xODM4IDEzMS42NzIgNTUuNzg3OCAxMzEuNDk4IDU5LjA3MzhaIiBmaWxsPSIjRkZFRDAwIi8+CjxwYXRoIGQ9Ik0wLjk2MTk3NSAwLjk0NDgyNFYxNDAuNzg2SDE0MC44MDJWMC45NDQ4MjRIMC45NjE5NzVaTTEzNS40MzYgNjQuNDM4OEMxMzQuODAyIDY5LjUyNTggMTMxLjM2MyA3OC45NTQ4IDEyOS41MzYgODIuNzIzOEMxMjQuNjM2IDkyLjgyMzggMTE4LjA4MyAxMDAuNTg3IDEwNS40NjIgMTAwLjU4N0M5OC43MiAxMDAuNTg3IDkzLjE3NCA5OC40MzY4IDg5LjkzMSA5NC4zMDM4Qzg1LjI1MDggOTguNDI5OCA3OS4yMTUgMTAwLjY4NyA3Mi45NzYgMTAwLjY0NkM2OC40ODM5IDEwMC43NjEgNjQuMDg2MSA5OS4zNDU5IDYwLjUwNCA5Ni42MzI4QzU2LjM3MTYgOTkuMzUxOSA1MS41MDYgMTAwLjc0MSA0Ni41NjEgMTAwLjYxNEM0Mi4zNTMgMTAwLjcwNCAzOC4yMjM4IDk5LjQ2NDMgMzQuNzYxIDk3LjA3MThDMzEuMjMzIDk5LjQxMzggMjYuNjA4IDEwMC41NzIgMjEuMTc4IDEwMC40NDdDMTIuMTQ1IDEwMC4yMzQgNS45MDc5OCA5NC41MDM4IDUuNzI4OTggODYuMTg3OEM1LjQ5MDk4IDc1LjEzNzggMTQuOCA1NC45MTE4IDE5LjE4NSA0Ny45MDc4QzIwLjYyMTQgNDUuMzU0NCAyMi43MTk5IDQzLjIzNTcgMjUuMjU5NSA0MS43NzVDMjcuNzk5IDQwLjMxNDMgMzAuNjg1NiAzOS41NjU2IDMzLjYxNSAzOS42MDc4QzQwLjI3OCAzOS42MDc4IDQyLjY5MyA0MS41MTM4IDQzLjg4MSA0My45MzY4QzQ5LjAyMiAzOS41Njg4IDU1LjgzNyAzOS4zMTg4IDYwLjY4OSAzOS4zMTg4QzY2LjA0NSAzOS4zMTg4IDY5LjQwNCA0MC43Mzk4IDcyLjI2NCA0My4wMTg4Qzc2LjQ2MzYgNDAuNTUzOSA4MS4yNjY3IDM5LjMwNzMgODYuMTM1IDM5LjQxODhDOTMuMDM1IDM5LjQxODggOTguMTU2IDQxLjAxODggMTAxLjcyOSA0NC41NTU4QzEwNS44OTggNDEuMDg3OCAxMTEuMTE2IDM5LjUwNTggMTE2Ljk2MSAzOS41MDU4QzEyNC42ODUgMzkuNTA1OCAxMjkuNzY4IDQyLjI5MjggMTMyLjc1MyA0Ni40NDY4QzEzNi45NjMgNTIuMzA1OCAxMzYuMjExIDU4LjIwNDggMTM1LjQzNiA2NC40Mzg4WiIgZmlsbD0iI0UzMDAwQiIvPgo8cGF0aCBkPSJNMC4wMDA5NzY1NjIgMFYxNDEuNzMzSDE0MS43MzNWMEgwLjAwMDk3NjU2MlpNMTM5Ljc4MiAxLjk1M1YxMzkuNzgxSDEuOTUzOThWMS45NTNIMTM5Ljc4MloiIGZpbGw9IiMxODE3MTYiLz4KPHBhdGggZD0iTTEzNC43NTQgNDIuNTI3OVY0MS41NjM5SDEzNS40MDlDMTM1Ljg4OCA0MS41NjM5IDEzNi4xMzYgNDEuNzMxOSAxMzYuMTM2IDQyLjA0MTlDMTM2LjEzNiA0Mi4yODg5IDEzNS45NzYgNDIuNTI3OSAxMzUuNDg5IDQyLjUyNzlIMTM0Ljc1NFpNMTM3LjEwNCA0NC41Mjc5TDEzNi42OTYgNDMuODE5OUMxMzYuMzQxIDQzLjIwMTkgMTM2LjI0MyA0My4xMDQ5IDEzNS45NDIgNDIuOTk3OVY0Mi45Nzk5QzEzNi4xOTggNDIuOTczNCAxMzYuNDQxIDQyLjg2NjQgMTM2LjYxOSA0Mi42ODJDMTM2Ljc5NiA0Mi40OTc3IDEzNi44OTQgNDIuMjUwOSAxMzYuODkxIDQxLjk5NDlDMTM2Ljg5MSA0MS40MzY5IDEzNi41MzYgNDEuMDEwOSAxMzUuNzgyIDQxLjAxMDlIMTM0LjAyOFY0NC41Mjc5SDEzNC43NTRWNDMuMDg3OUgxMzQuODg2QzEzNC45ODkgNDMuMDcxIDEzNS4wOTUgNDMuMDc4MiAxMzUuMTk1IDQzLjEwODlDMTM1LjI5NSA0My4xMzk2IDEzNS4zODcgNDMuMTkzIDEzNS40NjMgNDMuMjY0OUMxMzUuNjUzIDQzLjQ3MjMgMTM1LjgxNCA0My43MDQ0IDEzNS45NDIgNDMuOTU0OUwxMzYuMjI1IDQ0LjUyOTlMMTM3LjEwNCA0NC41Mjc5Wk0xMzUuMzczIDQwLjAyNzlDMTM1LjkxMyA0MC4wMjYgMTM2LjQ0MiA0MC4xODQzIDEzNi44OTIgNDAuNDgyOEMxMzcuMzQyIDQwLjc4MTQgMTM3LjY5MyA0MS4yMDY4IDEzNy45MDEgNDEuNzA1MkMxMzguMTA5IDQyLjIwMzUgMTM4LjE2NSA0Mi43NTI1IDEzOC4wNjEgNDMuMjgyNEMxMzcuOTU3IDQzLjgxMjQgMTM3LjY5OCA0NC4yOTk2IDEzNy4zMTcgNDQuNjgyNEMxMzYuOTM2IDQ1LjA2NTEgMTM2LjQ1IDQ1LjMyNjIgMTM1LjkyIDQ1LjQzMjVDMTM1LjM5MSA0NS41Mzg4IDEzNC44NDIgNDUuNDg1NyAxMzQuMzQyIDQ1LjI3OTdDMTMzLjg0MyA0NS4wNzM4IDEzMy40MTYgNDQuNzI0MyAxMzMuMTE2IDQ0LjI3NTZDMTMyLjgxNSA0My44MjY4IDEzMi42NTQgNDMuMjk5IDEzMi42NTQgNDIuNzU4OUMxMzIuNjU1IDQyLjAzNzcgMTMyLjk0MiA0MS4zNDYzIDEzMy40NTEgNDAuODM1NkMxMzMuOTYgNDAuMzI0OSAxMzQuNjUxIDQwLjAzNjQgMTM1LjM3MiA0MC4wMzI5TDEzNS4zNzMgNDAuMDI3OVpNMTM1LjM3MyAzOS4zNTY5QzEzNC43MDIgMzkuMzU3OSAxMzQuMDQ2IDM5LjU1NzcgMTMzLjQ4OSAzOS45MzEyQzEzMi45MzEgNDAuMzA0NiAxMzIuNDk3IDQwLjgzNDkgMTMyLjI0MSA0MS40NTVDMTMxLjk4NCA0Mi4wNzUyIDEzMS45MTcgNDIuNzU3NCAxMzIuMDQ5IDQzLjQxNTVDMTMyLjE4IDQ0LjA3MzYgMTMyLjUwMyA0NC42NzgxIDEzMi45NzcgNDUuMTUyNkMxMzMuNDUyIDQ1LjYyNzEgMTM0LjA1NiA0NS45NTAzIDEzNC43MTQgNDYuMDgxNUMxMzUuMzczIDQ2LjIxMjYgMTM2LjA1NSA0Ni4xNDU4IDEzNi42NzUgNDUuODg5NUMxMzcuMjk1IDQ1LjYzMzEgMTM3LjgyNSA0NS4xOTg3IDEzOC4xOTkgNDQuNjQxMkMxMzguNTcyIDQ0LjA4MzcgMTM4Ljc3MiA0My40MjggMTM4Ljc3MyA0Mi43NTY5QzEzOC43NzQgNDIuMzEwMyAxMzguNjg3IDQxLjg2NzkgMTM4LjUxNiA0MS40NTUyQzEzOC4zNDUgNDEuMDQyNSAxMzguMDk1IDQwLjY2NzYgMTM3Ljc3OSA0MC4zNTIxQzEzNy40NjMgNDAuMDM2NiAxMzcuMDg3IDM5Ljc4NjcgMTM2LjY3NCAzOS42MTY4QzEzNi4yNjEgMzkuNDQ2OCAxMzUuODE5IDM5LjM2MDIgMTM1LjM3MiAzOS4zNjE5TDEzNS4zNzMgMzkuMzU2OVoiIGZpbGw9IiMxODE3MTYiLz4KPHBhdGggZD0iTTExNi44ODkgNDMuMDAwOUMxMDkuNTY0IDQzLjAwMDkgMTA0LjUwNCA0NS45MDA5IDEwMS4wNzYgNDkuOTYxOUMxMDAuNjY3IDQ5LjA2MjQgMTAwLjExNCA0OC4yMzU4IDk5LjQzOSA0Ny41MTQ5Qzk2LjYzOSA0NC4zNDM5IDkyLjEyNSA0Mi44NjM5IDg2LjA3NCA0Mi44NjM5QzgwLjkwNyA0Mi43MDc2IDc1Ljg1MjcgNDQuMzkyNSA3MS44MTMgNDcuNjE3OUM3MC4wMzQgNDQuNzI5OSA2NS43OTkgNDIuODE3OSA2MC42OTEgNDIuODE3OUM1NC4wMTcgNDIuODE3OSA0Ni43NDQgNDMuNzYxOSA0Mi40MyA1MC43MTI5QzQyLjMzIDQ4LjIxMjkgNDIuMSA0Ni44ODU5IDQwLjY5MyA0NS4zOTU5QzM4Ljk4MyA0My41ODU5IDM2LjIxNiA0My4xMTI5IDMzLjUyIDQzLjExMjlDMjguNjA4IDQzLjExMjkgMjQuOTE0IDQ1LjI1NzkgMjIuMjU0IDQ5LjYyNjlDMTguMzk0IDU1Ljc5MDkgOS4wNDEwMSA3Ni4wNjc5IDkuMjU0MDEgODUuODg5OUM5LjM5MDAxIDkyLjIzMzkgMTMuNjQ2IDk2LjgwNjkgMjEuMjY0IDk2Ljk4MzlDMjcuMjE1IDk3LjEyNjkgMzEuODgzIDk1LjUzNjkgMzQuODU0IDkyLjUzODlDMzcuNTE5IDk1LjQzMjkgNDEuNTg1IDk3LjEzMDkgNDYuNDQ4IDk3LjEzMDlDNTEuODY1IDk3LjEzMDkgNTcuMzE3IDk1LjUwNDkgNjAuNTM3IDkxLjk0ODlDNjMuMjQ5IDk1LjI4MjkgNjcuNTE4IDk3LjIxOTkgNzMuMDA1IDk3LjE5MjlDNzYuNDAwMiA5Ny4xNzM2IDc5Ljc0NyA5Ni4zODUzIDgyLjc5MzkgOTQuODg3MUM4NS44NDA3IDkzLjM4ODkgODguNTA4NiA5MS4yMTk5IDkwLjU5NyA4OC41NDI5QzkyLjg1NiA5NC42OTE5IDk4LjU4NCA5Ny4xMzA5IDEwNC44MzggOTcuMTMwOUMxMTguNTQ4IDk3LjEzMDkgMTI0LjU2OSA4Ny43MDQ5IDEyOS41ODYgNzIuNzk3OUMxMzEuMTA1IDY4LjM3NjQgMTMyLjA3NiA2My43ODUgMTMyLjQ3NSA1OS4xMjY5QzEzMi44OSA1MS4yOTE5IDEyOS41NzQgNDMuMDAwOSAxMTYuODg5IDQzLjAwMDlaTTI1LjY3MiA4MC40NzQ5QzMyLjc2NSA3OS4yNDI5IDM0LjU0OSA4MS44MDc5IDM0LjMyNSA4NC4xODE5QzMzLjY1NiA5MS4yOTA5IDI3LjEzNCA5Mi44ODE5IDIxLjQ3MiA5Mi43NDc5QzE3LjM2NSA5Mi42NDc5IDEzLjY3MiA5MC43NzA5IDEzLjU3MiA4Ni4wMDA5QzEzLjM5MyA3Ny42NTg5IDIxLjkwMSA1OC4zNjA5IDI1LjkwNiA1MS45NjI5QzI3Ljc1NSA0OC45Mjc5IDMwLjAwNiA0Ny40MjQ5IDMzLjYwNiA0Ny40MjQ5QzM3LjAxMiA0Ny40MjQ5IDM3Ljg1NiA0OS4xNzM5IDM3LjgwNiA1MS4yNjg5QzM3LjY2NSA1Ni44NTI5IDI4LjYzNSA3My44Mzk5IDI1LjY3MiA4MC40NzQ5Wk00OC43NzIgNzMuOTIyOUM0OC4zMDMgNzUuMTkxOSA0Ny40MTQgNzcuODUyOSA0Ni42OTcgODAuNjczOUM0OC45OTAxIDgwLjAwNTEgNTEuMzczMiA3OS42OTY0IDUzLjc2MSA3OS43NTg5QzU3LjE2OSA3OS44NDI5IDU5LjM0NyA4MS4yNTg5IDU5LjM0NyA4NC4wNzI5QzU5LjM0NyA5MC45MDM5IDUxLjc5NyA5Mi45MTA5IDQ2LjU1OSA5Mi45MTA5QzQwLjgwNyA5Mi45MTA5IDM1Ljc1OSA4OS42MzU5IDM1Ljc1OSA4My4zNDY5QzM1Ljc1OSA3NS45NzM5IDM5Ljc1OSA2NC43OTI5IDQzLjUwNyA1Ny4zNDY5QzQ4LjExNCA0OC4yMDE5IDUyLjgxOSA0Ni45ODQ5IDYwLjkyNSA0Ni45ODQ5QzY0LjQ4OSA0Ni45ODQ5IDY4LjU5MyA0OC41MDg5IDY4LjU5MyA1MS44Njk5QzY4LjU5MyA1Ni41MzI5IDY0LjY0MyA1OC4zMTI5IDYwLjcyNiA1OC41MzY5QzU4LjggNTguNjY0IDU2Ljg2ODcgNTguNjkgNTQuOTQgNTguNjE0OUM1My44NzMxIDYwLjM2ODIgNTIuOTcyOCA2Mi4yMTc2IDUyLjI1MSA2NC4xMzg5QzU5LjUwMyA2My4xMTg5IDYyLjU3NyA2NC43NjQ5IDYxLjM1MSA2OC45NTg5QzU5LjY5NSA3NC42MjU5IDU0Ljc4NCA3NC45OTg5IDQ4Ljc3IDczLjkyMjlINDguNzcyWk04NC40NDEgNTYuMjkxOUM4My41ODA5IDU2LjMzOCA4Mi43NDYxIDU2LjU5ODYgODIuMDEyNSA1Ny4wNDk5QzgxLjI3ODkgNTcuNTAxMiA4MC42Njk5IDU4LjEyOSA4MC4yNDEgNTguODc1OUM3OC4xNDEgNjEuODI1OSA3My41ODUgNzMuNjU0OSA3Mi44NzYgNzguNTEzOUM3Mi4zOSA4MS44NDI5IDczLjgyNyA4Mi41MjA5IDc1LjM5OSA4Mi41MjA5Qzc3LjkxOCA4Mi41MjA5IDgwLjc0MiA3OS44NTQ5IDgxLjcwNyA3NS40NTM5QzgxLjcwNyA3NS40NTM5IDc2LjkwNyA3NS4zMzc5IDc4LjIzNCA3MS4wODQ5Qzc5LjUxOCA2Ni45NTY5IDgxLjk1NSA2Ni4wNjI5IDg1Ljk5NiA2NS44OTY5QzkzLjk1NyA2NS41NzA5IDkzLjE3MSA3MS40NDk5IDkyLjUzMyA3NC41ODQ5QzkwLjQ2NSA4NC43NjM5IDgzLjIyIDkyLjk0MTkgNzIuOTcyIDkyLjk0MTlDNjUuOTU2IDkyLjk0MTkgNjEuNiA4OS4wNjE5IDYxLjYgODEuOTA0OUM2MS42IDc2LjgwNDkgNjQuMTI5IDY4LjgwNDkgNjYuMTM0IDY0LjEyMjlDNzAuNDAyIDU0LjE1NDkgNzQuODc2IDQ3LjE3NzkgODYuMjc3IDQ3LjE3NzlDOTMuMTE3IDQ3LjE3NzkgOTguNTEzIDQ5LjYzNDkgOTcuNzIyIDU2LjA0MzlDOTcuMTQxIDYwLjc0MzkgOTQuNzg3IDYzLjUwODkgOTAuNTExIDYzLjg0MzlDODkuMzE2IDYzLjkzNzkgODQuNDIzIDYzLjgxNDkgODYuMDQ2IDU5LjE4NDlDODYuNjExIDU3LjU2NDkgODYuODQ0IDU2LjI5MTkgODQuNDM5IDU2LjI5MTlIODQuNDQxWk0xMjcuNDk4IDY0LjcwNDlDMTI2LjEwMiA3MS4xMzE4IDEyMy43OTIgNzcuMzI1NCAxMjAuNjM4IDgzLjA5NjlDMTE1LjgzOCA5MS43MzA5IDExMC4wMDYgOTIuOTM4OSAxMDQuOTE1IDkyLjg3ODlDOTkuODI0IDkyLjgxODkgOTQuMDg1IDkwLjkzNzkgOTQuMDQyIDgzLjA3ODlDOTQuMDEgNzcuNDM5OSA5Ni40NDIgNjkuNDc4OSA5OC41MDggNjQuMjYzOUMxMDIuMTA4IDU0LjgwNTkgMTA1Ljc4NSA0Ny4wOTQ5IDExNy40MDggNDcuMjMyOUMxMzAuOTY5IDQ3LjM5NzkgMTI4LjU1NCA1OS40NTI5IDEyNy40OTYgNjQuNzA0OUgxMjcuNDk4Wk0xMTcuODMgNTguNzkyOUMxMTcuNjg2IDYyLjQxMzkgMTEyLjM3OCA3Ni44OTI5IDExMC40OTIgODAuMDkyOUMxMDkuNjc1IDgxLjQ3NzkgMTA4Ljc1NCA4Mi42MjI5IDEwNy4wOTIgODIuNjIyOUMxMDYuODAzIDgyLjYzNDYgMTA2LjUxNSA4Mi41ODUyIDEwNi4yNDYgODIuNDc3OEMxMDUuOTc4IDgyLjM3MDUgMTA1LjczNSA4Mi4yMDc3IDEwNS41MzQgODJDMTA1LjMzMiA4MS43OTIzIDEwNS4xNzcgODEuNTQ0NSAxMDUuMDc4IDgxLjI3MjdDMTA0Ljk4IDgxLjAwMDkgMTA0LjkzOSA4MC43MTEzIDEwNC45NiA4MC40MjI5QzEwNC44NTUgNzcuMTU1OSAxMTAuODUxIDYwLjc3MDkgMTEyLjkwMiA1OC4xMTI5QzExMy4yMDQgNTcuNTcxNSAxMTMuNjU3IDU3LjEzIDExNC4yMDYgNTYuODQyNEMxMTQuNzU1IDU2LjU1NDggMTE1LjM3NiA1Ni40MzM3IDExNS45OTMgNTYuNDkzOUMxMTcuNjk1IDU2LjUwOTkgMTE3Ljg3IDU3LjczNzkgMTE3LjgyOCA1OC43OTI5SDExNy44M1oiIGZpbGw9IiMxODE3MTYiLz4KPC9nPgo8ZGVmcz4KPGNsaXBQYXRoIGlkPSJjbGlwMF81MDAwXzIyNDU0Ij4KPHJlY3Qgd2lkdGg9IjU4Ny40NDEiIGhlaWdodD0iNDM1Ljk4NSIgZmlsbD0id2hpdGUiLz4KPC9jbGlwUGF0aD4KPC9kZWZzPgo8L3N2Zz4K)

Questa operazione potrebbe richiedere alcuni minuti![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzYiIGhlaWdodD0iMzYiIHZpZXdCb3g9IjAgMCAzNiAzNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTguMDAwMiAzNC41M0wxOC4wMDAyIDI1LjUzIiBzdHJva2U9IiM5RDlEOUQiIHN0cm9rZS13aWR0aD0iMS43MDU0OCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIvPjxwYXRoIGQ9Ik0xLjUgMTguMDNMMTAuNSAxOC4wMyIgc3Ryb2tlPSIjOUQ5RDlEIiBzdHJva2Utd2lkdGg9IjEuNzA1NDgiIHN0cm9rZS1saW5lam9pbj0icm91bmQiLz48cGF0aCBkPSJNMzQuNTAwMyAxOC4wMjk5TDI1LjUwMDMgMTguMDI5OSIgc3Ryb2tlPSIjOUQ5RDlEIiBzdHJva2Utd2lkdGg9IjEuNzA1NDgiIHN0cm9rZS1saW5lam9pbj0icm91bmQiLz48cGF0aCBkPSJNMTguMDAwMyAxLjQ3MDE0VjEwLjQ3MDEiIHN0cm9rZT0iIzlEOUQ5RCIgc3Ryb2tlLXdpZHRoPSIxLjcwNTQ4IiBzdHJva2UtbGluZWpvaW49InJvdW5kIi8+PHBhdGggZD0iTTYuMzExODkgMjkuNjg4NUwxMi42NzU5IDIzLjMyNDYiIHN0cm9rZT0iIzlEOUQ5RCIgc3Ryb2tlLXdpZHRoPSIxLjcwNTQ4IiBzdHJva2UtbGluZWpvaW49InJvdW5kIi8+PHBhdGggZD0iTTYuMzExODkgNi4zNTM5TDEyLjY3NTggMTIuNzE3OSIgc3Ryb2tlPSIjOUQ5RDlEIiBzdHJva2Utd2lkdGg9IjEuNzA1NDgiIHN0cm9rZS1saW5lam9pbj0icm91bmQiLz48cGF0aCBkPSJNMjkuNjQ2NCAyOS42ODg1TDIzLjI4MjUgMjMuMzI0NSIgc3Ryb2tlPSIjOUQ5RDlEIiBzdHJva2Utd2lkdGg9IjEuNzA1NDgiIHN0cm9rZS1saW5lam9pbj0icm91bmQiLz48cGF0aCBkPSJNMjkuNjg4NyA2LjMxMTc0TDIzLjMyNDcgMTIuNjc1NyIgc3Ryb2tlPSIjOUQ5RDlEIiBzdHJva2Utd2lkdGg9IjEuNzA1NDgiIHN0cm9rZS1saW5lam9pbj0icm91bmQiLz48L3N2Zz4K)

# Browser non supportato

Il browser non può eseguire l'app SPIKE, perché non supporta:Ti consigliamo di utilizzare Google Chrome su Chromebook, Windows o macOS.

Mostra blocchi da

SPIKE™ Prime

SPIKE™ Essential

Tutti i prodotti

Rinomina progetto...

Scarica

Incolla

Knowledge Base

# 7\. Controllo del sensore

Nei capitoli precedenti, hai provato a usare variabili e numeri casuali per controllare i motori e la luce. Ora utilizzerai un valore del sensore per controllare un motore.

Connetti un motore alla porta A e un sensore di forza alla porta B e prova il programma riportato di seguito.

![](https://spike.legoeducation.com/content/v3/assets/blt293eea581807678a/bltb1f58f66da0fcb3e/63e0d376260a9a2054c6d1ad/sensor_control.png)

```
import force_sensor
import motor
from hub import port

# Memorizza la forza del sensore di forza in una variabile.
force = force_sensor.force(port.B)

# Stampa la variabile nella console.
print(force)

# Aziona il motore e utilizza la variabile per impostare la velocità.
motor.run(port.A, force)
```

Premi il sensore di forza mentre il programma è in esecuzione. Questa operazione non è servita a molto, giusto? Fortunatamente, l'esempio utilizza la funzione integrata `print()` per scrivere la variabile `force` nella console, in modo da poter vedere facilmente cosa è andato storto.

## La console

A volte il tuo programma non fa quello che ti aspetti che faccia. Quando ciò accade, puoi utilizzare la funzione `print()` per eseguire il _debug_ del programma. La funzione `print()` scrive qualsiasi cosa passi come argomento nella finestra Console sotto l'editor di codice, in questo caso la forza del sensore di forza. Esegui nuovamente il programma e osserva il valore visualizzato nella console.

Vedrai un singolo numero nella console e, a meno che tu non stia premendo il sensore di forza quando hai avviato il programma, quel numero è `0`. Azionare un motore a 0 gradi al secondo non serve a molto, quindi il problema è che il programma controlla il valore del sensore solo una volta all'inizio del programma. Per aggiornare la velocità del motore in base alla forza per tutta da durata dell'esecuzione del programma, è necessario utilizzare di nuovo il ciclo `while True`.

Inoltre, nella console vengono visualizzati i messaggi di errore quando si verifica un problema durante l'esecuzione del programma. Un errore comune si verifica quando si esegue un programma per controllare un motore o leggere un sensore non connesso. Disconnetti il sensore di forza ed esegui lo stesso programma un'ultima volta. Nella console viene visualizzato un messaggio di errore che informa che c'è stato un problema, la relativa descrizione e su quale riga di codice si è verificato.

## Correzione dei bug

La console ti ha aiutato a trovare due bug. Connetti di nuovo il sensore di forza alla porta B per correggere il secondo bug, quindi esegui il programma sottostante che corregge il primo bug _racchiudendo_ il codice in un ciclo `while True`.

```
import force_sensor
import motor
from hub import port

while True:
    # Memorizza la forza del sensore di forza in una variabile.
    force = force_sensor.force(port.B)

    # Stampa la variabile nella console.
    print(force)

    # Aziona il motore e utilizza la variabile per impostare la velocità.
    motor.run(port.A, force)
```

Premi il sensore di forza mentre il programma è in esecuzione. Vedrai il motore accelerare o rallentare a seconda di quanto forte premi il sensore di forza. Nella console vengono visualizzati anche molti valori variabili. La forza del sensore di forza viene misurata in decinewton (dN) e poiché la forza massima misurabile è di 10 newton, il valore massimo in dN è pari a 100. Un motore che gira a 100 gradi al secondo non è ancora molto veloce!

## Valori restituiti dalla funzione

Invece di memorizzare il valore del sensore di forza in una variabile, è anche possibile definire una funzione che _restituisce_ questo valore. Separare le diverse parti del programma in questo modo semplifica l'organizzazione del codice e la correzione di eventuali bug.

Il programma successivo definisce una funzione `motor_velocity()` che restituisce la velocità del motore desiderata in base alla forza del sensore di forza anziché utilizzare una variabile.

```
import force_sensor
import motor
from hub import port

# Questa funzione restituisce la velocità del motore desiderata.
def motor_velocity():
    # La velocità è cinque volte la forza del sensore di forza.
    return force_sensor.force(port.B) * 5

while True:
    # Aziona il motore come prima.
    # Utilizza il valore restituito dalla funzione `motor_velocity()` per la velocità.
    motor.run(port.A, motor_velocity())
```

Premi il sensore di forza mentre il programma è in esecuzione. Vedrai il motore accelerare o rallentare a seconda di quanto forte premi il sensore di forza. La funzione `motor_velocity()` moltiplica il valore della forza per 5, quindi la velocità sarà compresa tra 0 e 500 gradi al secondo.

## Sfida

Puoi modificare il codice per azionare il motore a 1000 gradi al secondo quando il sensore di forza è completamente premuto?