import time

def prepara_caffe():
    print("Accendo la macchinetta del caffè...")
    time.sleep(3)  # Simula l'attesa per il caffè (3 secondi)
    print("Il caffè è pronto!")

def prepara_toast():
    print("Metto il pane nel tostapane...")
    time.sleep(2)  # Simula l'attesa per il toast (2 secondi)
    print("Il toast è pronto!")

def prepara_yogurt():
    print("Inizio a preparare la ciotola di yogurt...")
    time.sleep(1)  # Simula la preparazione dello yogurt (1 secondo)
    print("La ciotola di yogurt è pronta!")

if __name__ == "__main__":
    start_time = time.time()
    
    prepara_caffe()
    prepara_toast()
    prepara_yogurt()
    
    end_time = time.time()
    print(f"\nTempo totale (sequenziale): {end_time - start_time:.2f} secondi")
