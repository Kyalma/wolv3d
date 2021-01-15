from typing import NamedTuple

class Position(NamedTuple):
    x: int
    y: int

    def __repr__(self) -> str:
        return f'({x}, {y})'

    def __eq__(self, other: Position) -> bool:
        return self.x == other.x and self.y == other.y
