import random
from typing import List, Dict

def get_dynamic_skill(base_val: float, consistency: int) -> float:
    """Imitacja rzutu kością: im niższa stabilność, tym większy rozrzut (Variance)."""
    # Zakres błędu: dla Cons 100 -> +/- 2%, dla Cons 70 -> +/- 15%
    variance_range = (100 - consistency) / 200.0 
    multiplier = random.uniform(1.0 - variance_range, 1.0 + variance_range)
    return base_val * multiplier

def simulate_event_based_heat(riders_with_gates: List[Dict], track_difficulty: float = 0.05):
    """
    track_difficulty: Proóg trudności wyprzedzania (0.05 = 5% przewagi wymagane)
    """
    # 1. FAZA: START (PUNKT KONTROLNY 1)
    for item in riders_with_gates:
        r = item['rider']
        gate_mod = 1.06 if item['gate'] == 1 else (0.94 if item['gate'] == 3 else 1.0) # uproszczenie testowe
        
        # Obliczamy start z uwzględnieniem Consistency
        raw_start = (r.reflex * 0.7 + r.start_tech * 0.3) * gate_mod
        item['current_start_score'] = get_dynamic_skill(raw_start, r.consistency)

    # Ustalenie pozycji po 1. łuku
    standings = sorted(riders_with_gates, key=lambda x: x['current_start_score'], reverse=True)
    
    log = [f"START: P1: {standings[0]['rider'].name}, P2: {standings[1]['rider'].name}"]

    # 2. FAZA: OKRĄŻENIA 2-4 (INTERAKCJA I BLOKOWANIE)
    # Symulujemy 3 próby wyprzedzania (po jednej na okrążenie)
    for lap in range(2, 5):
        for i in range(len(standings) - 1, 0, -1): # Idziemy od końca stawki
            attacker = standings[i]['rider']
            defender = standings[i-1]['rider']
            
            # Obliczamy potencjał ataku (Racecraft + Dist) vs obrony (Composure + Dist)
            attack_power = get_dynamic_skill(attacker.track_riding * 0.5 + attacker.racecraft * 0.5, attacker.consistency)
            defense_power = get_dynamic_skill(defender.track_riding * 0.5 + defender.composure * 0.5, defender.consistency)
            
            # Mechanika blokowania: Atakujący musi przebić obronę + próg trudności toru
            success_threshold = defense_power * (1.0 + track_difficulty)
            
            if attack_power > success_threshold:
                log.append(f"OKR {lap}: {attacker.name} WYPRZEDZA {defender.name}!")
                standings[i], standings[i-1] = standings[i-1], standings[i] # Zamiana miejsc
            else:
                log.append(f"OKR {lap}: {attacker.name} atakuje {defender.name} (ZABLOKOWANY)")

    return standings, log