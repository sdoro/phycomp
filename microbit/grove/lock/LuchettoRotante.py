class LucchettoRotante:
    def __init__(self, combinazione):
        ''' prende la combinazione come argomento e inizializza la rotazione a 0. '''

        self.combinazione = combinazione
        self.rotazione = 0
    
    def reset(self):
        ''' azzera la rotazione '''

        self.rotazione = 0
    
    def giraSinistra(self, scatti):
        ''' aggiorna la rotazione a seconda del numero di scatti specificato come argomento. '''

        self.rotazione -= scatti   # ----
        self.rotazione %= 40
    
    def giraDestra(self, scatti):
        ''' aggiorna la rotazione a seconda del numero di scatti specificato come argomento. '''

        self.rotazione += scatti   # ++++
        self.rotazione %= 40
    
    def apri(self):
        '''
        Tenta di aprire il lucchetto e restituisce True se la combinazione è stata
        inserita correttamente, False altrimenti.
        Per determinare se la combinazione è corretta, si controlla che la rotazione sia stata
        fatta verso destra per il primo numero della combinazione, poi verso sinistra per il
        secondo numero e infine di nuovo verso destra per il terzo numero.
        '''

        # generalizzato per una combinazione di n cifre (anche se sono 3)
        pos = self.combinazione[0]
        segno = -1
        for r in range(1, len(self.combinazione)):
            pos = (pos + segno * self.combinazione[r]) % 40
            segno = -segno

        if self.rotazione == pos:
            return True
        else:
            return False

    def __str__(self):
        #return f"\ncombinazione: {self.combinazione}, rotazione: {self.rotazione}\n"
        return "\ncombinazione: " + str(self.combinazione) + "rotazione: " + " " + str(self.rotazione) + "\n"


