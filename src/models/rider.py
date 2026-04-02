from pydantic import BaseModel, Field
from typing import Dict

class RiderSkills(BaseModel):
    # Techniczne
    reflex: int = Field(..., ge=1, le=100)
    start_tech: int = Field(..., ge=1, le=100)
    track_riding: int = Field(..., ge=1, le=100)
    racecraft: int = Field(..., ge=1, le=100)
    # Fizyczne
    fitness: int = Field(..., ge=1, le=100)
    weight: float = Field(..., ge=1.0, le=1.1)
    # Mentalne
    setup_intel: int = Field(..., ge=1, le=100)
    composure: int = Field(..., ge=1, le=100)
    bravery: int = Field(..., ge=1, le=100)
    consistency: int = Field(..., ge=1, le=100)

class Rider(BaseModel):
    id: str
    name: str
    base_skill: int # Podłoga (np. 1-100)
    skills: RiderSkills
    track_preference: str  # np. "Grit-Lover", "Technical-Master"
    tuner_id: str