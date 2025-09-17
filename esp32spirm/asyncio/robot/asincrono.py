import asyncio
import time

# Variabile per tracciare la posizione, come nell'esempio sequenziale
position_counter = 0
line_to_find = 3

async def move_robot():
    global position_counter
    print("Il robot si muove...")
    
    while position_counter < line_to_find:
        await asyncio.sleep(0.5) # Simula il movimento
        position_counter += 1
        
    print("\nIl robot si è mosso abbastanza lontano per trovare la linea.")

async def check_for_line_async():
    global position_counter
    print("Il sensore cerca la linea...")
    
    while position_counter < line_to_find:
        await asyncio.sleep(0.5) # Simula la ricerca continua
        
    print("Il sensore ha trovato la linea!")
    return True

async def asynchronous_approach():
    move_task = asyncio.create_task(move_robot())
    check_task = asyncio.create_task(check_for_line_async())
    
    # Aspettiamo che il sensore trovi la linea
    await asyncio.gather(move_task, check_task)
    
    print("\nPrendo l'oggetto.")

if __name__ == "__main__":
    print("--- Inizio approccio asincrono ---")
    start_time = time.time()
    asyncio.run(asynchronous_approach())
    end_time = time.time()
    print(f"--- Fine. Tempo totale: {end_time - start_time:.2f} secondi ---")
