from dataclasses import dataclass

@dataclass
class Point2D:
    x: int
    y: int

@dataclass
class Rule:
    first: int
    second: int