from src.utils.loaders import load_riders
from src.core.engine import simulate_advanced_heat

def run_test_heat():
    all_riders = load_riders("data/riders.json")
    
    # Mapujemy zawodników na konkretne pola startowe wg Twojego schematu
    mapping = {
        "GP-001": 3, # Zmarzlik - Pole 3 (0.94)
        "GP-002": 4, # Madsen - Pole 4 (1.03)
        "GP-003": 2, # Fricke - Pole 2 (0.97)
        "JUN-001": 1 # Przyjemski - Pole 1 (1.06)
    }

    riders_with_gates = []
    for r in all_riders:
        if r.id in mapping:
            riders_with_gates.append({'rider': r, 'gate': mapping[r.id]})

    results = simulate_advanced_heat(riders_with_gates)

    print(f"{'ZAWODNIK':<18} | {'POLE':<4} | {'MOD':<5} | {'START':<7} | {'DIST':<7} | {'TOTAL'}")
    print("-" * 65)
    for res in results:
        print(f"{res['name']:<18} | {res['gate']:<4} | {res['gate_mod_final']:<5} | {res['start_score']:<7} | {res['dist_score']:<7} | {res['total_power']:<7}")

if __name__ == "__main__":
    run_test_heat()