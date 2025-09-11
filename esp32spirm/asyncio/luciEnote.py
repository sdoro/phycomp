import asyncio

async def accendi_luce_e_aspetta():
    print("Accendo la luce verde.")
    # Immagina che 'hub.light.on("green")' sia una operazione asincrona
    await asyncio.sleep(2) # Pausa di 2 secondi, ma il programma può fare altro
    print("Luce spenta.")

async def fai_suonare_nota_e_aspetta():
    print("Suono una nota.")
    # Immagina che 'hub.speaker.play_note()' sia una operazione asincrona
    await asyncio.sleep(1)
    print("Nota finita.")

async def main():
    # Avvio le due operazioni contemporaneamente
    task1 = asyncio.create_task(accendi_luce_e_aspetta())
    print('type task1: ', type(task1))
    task2 = asyncio.create_task(fai_suonare_nota_e_aspetta())
    
    await task1
    await task2
    print("Finito.")

asyncio.run(main())

