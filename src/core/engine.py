import random
from typing import List, Dict

def calculate_rider_performance(rider, gate_mod: float, track_mods: Dict[str, float]):
    """
    Nowy model: Spłaszczone różnice + RNG uzależnione od Consistency.
    """
    # 1. Spłaszczanie bazy (Normalizacja)
    # Zamiast 98 vs 78, robimy różnicę rzędu kilku punktów wokół średniej 80.
    flattened_base = 80 + (rider.base_skill - 85) * 0.3 
    
    # 2. Obliczanie potencjału faz (Start i Dystans)
    start_attr = (rider.reflex * 0.7 + rider.start_tech * 0.3) / 100
    dist_attr = (rider.track_riding * 0.7 + rider.racecraft * 0.3) / 100

    # 3. Dynamiczne RNG oparte na Consistency
    # Im wyższe consistency, tym mniejszy rozrzut (Zmarzlik: +/- 2, Przyjemski: +/- 8)
    rng_range = (100 - rider.consistency) * 0.4
    luck_factor = random.uniform(-rng_range, rng_range)

    # 4. Wpływ Pola Startowego i Toru
    # Pole startowe modyfikuje głównie fazę startu
    start_score = (flattened_base * start_attr * gate_mod * track_mods.get("reflex", 1.0))
    dist_score = (flattened_base * dist_attr * track_mods.get("track_riding", 1.0))

    # Wynik końcowy z dodanym pechem/szczęściem
    final_total = (start_score * 0.4 + dist_score * 0.6) + luck_factor

    return {
        "start": round(start_score, 2),
        "dist": round(dist_score, 2),
        "luck": round(luck_factor, 2),
        "total": round(final_total, 2)
    }