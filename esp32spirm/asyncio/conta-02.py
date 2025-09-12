import asyncio
import time

async def conta_uno():
    print("Inizio conta_uno...")
    await asyncio.sleep(1)
    print("1 secondo passato")

async def conta_due():
    print("Inizio conta_due...")
    await asyncio.sleep(1)
    print("2 secondi passati")

async def conta_tre():
    print("Inizio conta_tre...")
    await asyncio.sleep(1)
    print("3 secondi passati")

async def main():
    print(f"Tempo di inizio: {time.strftime('%X')}")
    print("Inizio a contare...")
    await conta_uno()
    await conta_due()
    await conta_tre()
    print("Finito di contare!")
    print(f"Tempo di fine: {time.strftime('%X')}")

asyncio.run(main())
