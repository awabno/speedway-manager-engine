from src.utils.loaders import load_riders
from src.core.engine import simulate_detailed_heat

def run_enhanced_simulation():
    # Ścieżka relatywna do miejsca, z którego wywołujesz skrypt (root projektu)
    participants = load_riders("data/riders.json")
    
    # Tor Twardy (Modyfikatory zgodnie z Twoją tabelą)
    track_conditions = {"reflex": 1.2, "track_riding": 0.8}

    results = simulate_detailed_heat(participants, track_conditions)

    print(f"{'ZAWODNIK':<20} | {'BASE':<6} | {'START':<7} | {'DIST':<7} | {'TOTAL':<7}")
    print("-" * 60)
    for res in results:
        print(f"{res['name']:<20} | {res['base']:<6} | {res['start']:<7} | {res['dist']:<7} | {res['total']:<7}")

if __name__ == "__main__":
    run_enhanced_simulation()