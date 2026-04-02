def run_enhanced_simulation():
    participants = load_riders("data/riders.json")
    
    # Definicja pól wg Twoich wytycznych (Gorzów)
    # Mapowanie: Pole 1: Przyjemski, Pole 2: Fricke, Pole 3: Zmarzlik, Pole 4: Madsen
    gates = {
        "JUN-001": 1.05,  # Pole 1 (Handicap dla Juniora)
        "GP-003": 0.98,   # Pole 2
        "GP-001": 0.95,   # Pole 3 (Najgorsze dla Mistrza)
        "GP-002": 1.03    # Pole 4
    }

    track_mods = {"reflex": 1.2, "track_riding": 0.8}
    results = []

    for r in participants:
        gate_val = gates.get(r.id, 1.0)
        perf = calculate_rider_performance(r, gate_val, track_mods)
        results.append({**perf, "name": r.name, "gate": gate_val})

    # Sortowanie wyników
    sorted_results = sorted(results, key=lambda x: x['total'], reverse=True)

    print(f"{'POZ':<3} | {'ZAWODNIK':<18} | {'GATE':<5} | {'START':<7} | {'DIST':<7} | {'LUCK':<6} | {'TOTAL'}")
    print("-" * 75)
    for i, res in enumerate(sorted_results, 1):
        print(f"{i:<3} | {res['name']:<18} | {res['gate']:<5} | {res['start']:<7} | {res['dist']:<7} | {res['luck']:<6} | {res['total']}")

if __name__ == "__main__":
    run_enhanced_simulation()