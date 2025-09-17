import time

def move_robot_step():
    print("Il robot si muove di 1 cm.")
    time.sleep(0.5)  # Simula un'azione che richiede tempo

def check_for_line(current_position):
    print(f"   - Controllo la posizione {current_position}...")
    time.sleep(0.5)  # Simula il tempo necessario per il controllo
    
    # La linea viene trovata solo alla posizione 3
    if current_position == 3:
        print("   - Ho trovato la linea!")
        return True
    else:
        print("   - Linea non trovata.")
        return False

def grab_object():
    print("\nPrendo l'oggetto.")

def sequential_approach():
    current_position = 0
    line_found = False
    
    while not line_found:
        current_position += 1
        move_robot_step()
        line_found = check_for_line(current_position)
    
    grab_object()

if __name__ == "__main__":
    print("--- Inizio approccio sequenziale ---")
    start_time = time.time()
    sequential_approach()
    end_time = time.time()
    print(f"--- Fine. Tempo totale: {end_time - start_time:.2f} secondi ---")
