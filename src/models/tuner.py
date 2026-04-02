class TunerTrajectory(str, Enum):
    STABLE = "stable"
    ASCENDING = "ascending"
    FADING = "fading"
    PEAK = "peak"

class Tuner(BaseModel):
    id: str
    name: str
    base_level: int
    current_trend: float
    momentum: float
    target_trend: float
    specialization: str  # np. "torque", "power"
    max_capacity: int = 30
    current_clients: int = 0