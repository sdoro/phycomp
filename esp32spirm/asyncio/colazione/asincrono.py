import asyncio
import time

async def prepara_caffe():
    print("Accendo la macchinetta del caffè...")
    await asyncio.sleep(3)  # Simula l'attesa in modo non bloccante
    print("Il caffè è pronto!")

async def prepara_toast():
    print("Metto il pane nel tostapane...")
    await asyncio.sleep(2)  # Simula l'attesa in modo non bloccante
    print("Il toast è pronto!")

async def prepara_yogurt():
    print("Inizio a preparare la ciotola di yogurt...")
    await asyncio.sleep(1)  # Simula l'attesa in modo non bloccante
    print("La ciotola di yogurt è pronta!")

async def prepara_colazione():
    # Avvia le tre operazioni contemporaneamente
    await asyncio.gather(
        prepara_caffe(),
        prepara_toast(),
        prepara_yogurt()
    )

if __name__ == "__main__":
    start_time = time.time()
    
    asyncio.run(prepara_colazione())
    
    end_time = time.time()
    print(f"\nTempo totale (asincrono): {end_time - start_time:.2f} secondi")
