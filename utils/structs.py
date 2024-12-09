from dataclasses import dataclass

@dataclass
class Point2D:
    x: int
    y: int


@dataclass
class Rule:
    first: int
    second: int

@dataclass
class FileStorage:
    id: int
    length: int
    freespace: int