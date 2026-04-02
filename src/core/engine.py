import random
from typing import List, Dict

def simulate_advanced_heat(riders_with_gates: List[Dict]):
    """
    riders_with_gates: Lista słowników [{'rider': Rider, 'gate': 1}, ...]
    """
    gate_modifiers = {
        1: {"base": 1.06, "variance": 0.05},
        2: {"base": 0.97, "variance": 0.05},
        3: {"base": 0.94, "variance": 0.05},
        4: {"base": 1.03, "variance": 0.05}
    }

    heat_results = []

    for item in riders_with_gates:
        r = item['rider']
        gate = item['gate']
        
        # --- FAZA 1: START (Moment puszczenia sprzęgła) ---
        # Mechanika Niespodzianki (RNG Pola)
        gate_info = gate_modifiers[gate]
        gate_rng = random.uniform(-gate_info["variance"], gate_info["variance"])
        final_gate_mod = gate_info["base"] + gate_rng
        
        # Obliczenie Startu (Reflex + Tech) * Pole * Luck
        start_attr = (r.reflex * 0.7 + r.start_tech * 0.3)
        start_luck = random.uniform(0.98, 1.02)
        # Wynik startu (czysty potencjał wyjścia spod taśmy)
        start_total = start_attr * final_gate_mod * start_luck

        # --- FAZA 2: DYSTANS (Pogoń / Obrona) ---
        # TrackRiding + Racecraft + Weight (Lżejszy weight = mniejsza kara, np. 1.00 to 1.0)
        weight_impact = 1.05 - (r.weight - 1.0)
        dist_attr = (r.track_riding * 0.7 + r.racecraft * 0.3) * weight_impact
        dist_luck = random.uniform(0.95, 1.05)
        dist_total = dist_attr * dist_luck

        heat_results.append({
            "name": r.name,
            "gate": gate,
            "gate_mod_final": round(final_gate_mod, 3),
            "start_score": round(start_total, 2),
            "dist_score": round(dist_total, 2),
            "total_power": 0 # Obliczymy niżej pozycję
        })

    # Sortujemy po starcie, aby ustalić kto objął prowadzenie
    start_order = sorted(heat_results, key=lambda x: x['start_score'], reverse=True)
    
    # --- LOGIKA WYPRZEDZANIA ---
    # Lider startu ma przewagę. Każdy kolejny musi mieć DIST o 5% wyższy od lidera, by wyprzedzić.
    final_order = []
    lider_startu = start_order[0]
    
    for i, runner in enumerate(start_order):
        # Jeśli nie jesteś liderem, Twój DIST musi pokonać DIST lidera + handicap pozycji
        # (Uproszczona logika na potrzeby testu: silniejszy DIST sumuje się z pozycją startową)
        # Finalna moc to: 40% Start + 60% Dystans
        runner['total_power'] = (runner['start_score'] * 0.4) + (runner['dist_score'] * 0.6)
        final_order.append(runner)

    return sorted(final_order, key=lambda x: x['total_power'], reverse=True)