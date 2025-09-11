import asyncio
import time

async def conta_fino_a_tre():
    print("Inizio a contare...")
    await asyncio.sleep(1) # Simula un'operazione che richiede tempo
    print("1 secondo passato")
    await asyncio.sleep(1)
    print("2 secondi passati")
    await asyncio.sleep(1)
    print("3 secondi passati")
    print("Finito di contare!")

async def main():
    print(f"Tempo di inizio: {time.strftime('%X')}")
    await conta_fino_a_tre()
    print(f"Tempo di fine: {time.strftime('%X')}")

asyncio.run(main())
