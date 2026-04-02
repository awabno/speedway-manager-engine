import random
from typing import List, Dict
from src.models.rider import Rider

def simulate_detailed_heat(riders: List[Rider], track_modifiers: Dict[str, float]):
    """
    Główny silnik obliczeniowy biegu.
    """
    heat_report = []

    for r in riders:
        # 1. Obliczenia bazowe (Stała klasa zawodnika)
        base_power = r.base_skill * 0.8
        var_pool = r.base_skill * 0.2

        # 2. FAZA: START (Refleks 0.7 + Technika 0.3)
        # Uwzględniamy wagę (lżejszy = bonus) i modyfikator toru
        start_mod = track_modifiers.get("reflex", 1.0) * (1.1 - (r.weight - 1.0))
        start_attr_avg = (r.reflex * 0.7 + r.start_tech * 0.3) / 100
        start_luck = random.uniform(0.95, 1.05)
        start_score = base_power + (var_pool * start_attr_avg * start_mod * start_luck)

        # 3. FAZA: DYSTANS (Jazda 0.7 + Racecraft 0.3)
        dist_mod = track_modifiers.get("track_riding", 1.0)
        dist_attr_avg = (r.track_riding * 0.7 + r.racecraft * 0.3) / 100
        dist_luck = random.uniform(0.92, 1.08)
        dist_score = base_power + (var_pool * dist_attr_avg * dist_mod * dist_luck)

        # 4. WYNIK KOŃCOWY (Wagi faz: Start 40%, Dystans 60%)
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

    # Zwracamy listę posortowaną od najlepszego wyniku
    return sorted(heat_report, key=lambda x: x['total'], reverse=True)