import asyncio
import time

async def conta(numero_secondi):
    print(f"Inizio a contare per {numero_secondi} secondi.")
    await asyncio.sleep(numero_secondi)
    print(f"{numero_secondi} secondi passati!")
    return f"Finito di contare per {numero_secondi} secondi."

async def main():
    print(f"Tempo di inizio: {time.strftime('%X')}")
    
    # Crea le tre coroutine (non partono ancora)
    coroutine1 = conta(3)
    coroutine2 = conta(1)
    coroutine3 = conta(2)

    # Eseguile in parallelo e aspetta che tutte finiscano
    risultati = await asyncio.gather(coroutine1, coroutine2, coroutine3)
    
    print("Finito di contare!")
    print(f"Risultati: {risultati}")
    print(f"Tempo di fine: {time.strftime('%X')}")

asyncio.run(main())
