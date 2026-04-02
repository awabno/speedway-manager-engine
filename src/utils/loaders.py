import json
from src.models.rider import Rider

def load_riders(file_path: str) -> list[Rider]:
    """Wczytuje zawodników z pliku JSON do obiektów klasy Rider."""
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return [Rider(**r) for r in data]

def load_track(file_path: str, track_id: str):
    """Wczytuje dane konkretnego toru."""
    with open(file_path, 'r', encoding='utf-8') as f:
        tracks = json.load(f)
        return tracks.get(track_id)