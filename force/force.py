from dataclasses import dataclass


@dataclass
class Force:
    size: float
    direction: float
    poe: tuple[float, float] = 0, 0

    def __post_init__(self):
        if self.size < 0:
            raise ValueError('Size should not be negative')

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def __str__(self):
        return f'Force of size {self.size} and at {self.direction} degrees angle'


def add_force(a: Force, b: Force) -> Force:
    raise NotImplementedError
