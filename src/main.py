from src.utils.loaders import load_riders
from src.core.engine import simulate_detailed_heat

def run_simulation():
    # 1. Ładowanie danych
    # (Załóżmy, że plik riders.json zawiera naszą czwórkę: Zmarzlik, Madsen, Fricke, Przyjemski)
    try:
        participants = load_riders("data/riders.json")
    except FileNotFoundError:
        print("Błąd: Nie znaleziono pliku data/riders.json!")
        return

    # 2. Definicja warunków (Tor: Gorzów - Twardy/Techniczny)
    # Zgodnie z Twoją tabelą: Refleks 1.2x, Dystans 0.8x
    track_conditions = {
        "name": "Gorzów (Hard/Technical)",
        "modifiers": {"reflex": 1.2, "track_riding": 0.8}
    }

    print(f"SYMULACJA BIEGU NA TORZE: {track_conditions['name']}\n")

    # 3. Uruchomienie silnika
    results = simulate_detailed_heat(participants, track_conditions["modifiers"])

    # 4. Raportowanie (Wyświetlenie wszystkich składowych)
    header = f"{'ZAWODNIK':<20} | {'BASE':<6} | {'START':<7} | {'DIST':<7} | {'TOTAL':<7} | {'LUCK S/D'}"
    print(header)
    print("-" * len(header))

    for res in results:
        luck_str = f"{res['luck_start']}/{res['luck_dist']}"
        print(f"{res['name']:<20} | {res['base']:<6} | {res['start']:<7} | {res['dist']:<7} | {res['total']:<7} | {luck_str}")

if __name__ == "__main__":
    run_simulation()