import asyncio
import time

async def cuoci_il_pollo():
    print("Inizio a cuocere il pollo...")
    await asyncio.sleep(3) # Il pollo ha bisogno di 3 secondi
    print("Pollo cotto!")

async def prepara_l_insalata():
    print("Inizio a preparare l'insalata...")
    await asyncio.sleep(1) # L'insalata è veloce
    print("Insalata pronta!")

async def main():
    print(f"Inizio a preparare il pasto alle: {time.strftime('%X')}")

    # Avvia le due operazioni in parallelo
    task1 = asyncio.create_task(cuoci_il_pollo())
    task2 = asyncio.create_task(prepara_l_insalata())

    # Aspetta che entrambe le "task" siano completate
    await task1
    await task2
    
    print(f"Pasto completo alle: {time.strftime('%X')}")

asyncio.run(main())
