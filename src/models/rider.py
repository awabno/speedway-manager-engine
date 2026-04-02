from pydantic import BaseModel

class Rider(BaseModel):
    id: str
    name: str
    base_skill: int
    reflex: int
    start_tech: int
    track_riding: int
    racecraft: int
    weight: float
    composure: int