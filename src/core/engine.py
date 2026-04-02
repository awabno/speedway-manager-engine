import random
from typing import List, Dict

def simulate_detailed_heat(riders: List[Rider], track_modifiers: Dict[str, float]):
    """
    Pełna symulacja biegu z logowaniem każdej fazy.
    track_modifiers: Słownik typu {'reflex': 1.2, 'track_riding': 0.8}
    """
    heat_report = []

    for r in riders:
        # --- OBLICZENIA BAZOWE (70-80% siły) ---
        base_power = r.base_skill * 0.8
        var_pool = r.base_skill * 0.2

        # --- FAZA 1: START (Refleks 0.7 + Tech 0.3) ---
        # Uwzględniamy modyfikator toru i wagę (Lżejszy = lepiej na starcie)
        start_mod = track_modifiers.get("reflex", 1.0) * (1.1 - (r.weight - 1.0))
        start_attr_avg = (r.reflex * 0.7 + r.start_tech * 0.3) / 100
        start_luck = random.uniform(0.95, 1.05)
        start_score = base_power + (var_pool * start_attr_avg * start_mod * start_luck)

        # --- FAZA 2: DYSTANS (Jazda 0.7 + Racecraft 0.3) ---
        dist_mod = track_modifiers.get("track_riding", 1.0)
        dist_attr_avg = (r.track_riding * 0.7 + r.racecraft * 0.3) / 100
        dist_luck = random.uniform(0.92, 1.08) # Na dystansie losowość jest większa (błędy)
        dist_score = base_power + (var_pool * dist_attr_avg * dist_mod * dist_luck)

        # --- WYNIK KOŃCOWY ---
        # Start to 40% sukcesu, Dystans to 60%
        final_performance = (start_score * 0.4) + (dist_score * 0.6)

        heat_report.append({
            "name": r.name,
            "base": round(base_power, 2),
            "start": round(start_score, 2),
            "dist": round(dist_score, 2),
            "total": round(final_performance, 2),
            "luck_start": round(start_luck, 2),
            "luck_dist": round(dist_luck, 2)
        })

    # Sortowanie po wyniku końcowym
    sorted_report = sorted(heat_report, key=lambda x: x['total'], reverse=True)
    
    return sorted_report

# --- PRZYKŁAD WYŚWIETLENIA (W src/main.py) ---

# Symulujemy Tor Twardy (Beton): Bonus do Startu (+20%), Kara do Dystansu (-20%)
modifiers = {"reflex": 1.2, "track_riding": 0.8}
results = simulate_detailed_heat(participants, modifiers)

print(f"{'ZAWODNIK':<20} | {'BAZA':<6} | {'START':<6} | {'DYSTANS':<7} | {'TOTAL':<6}")
print("-" * 60)
for res in results:
    print(f"{res['name']:<20} | {res['base']:<6} | {res['start']:<6} | {res['dist']:<7} | {res['total']:<6}")