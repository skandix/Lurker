from dataclasses import dataclass, asdict

@dataclass(repr=True)
class RHendrix:
    Indentation: str
    Age: int
    Height: float