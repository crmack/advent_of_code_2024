from dataclasses import dataclass

@dataclass
class Point2D:
    x: int
    y: int

@dataclass
class Point2DWithVal:
    x: int
    y: int
    val: int

@dataclass
class Point2DWithStrVal:
    x: int
    y: int
    val: str

@dataclass
class Rule:
    first: int
    second: int

@dataclass
class FileStorage:
    id: int
    length: int
    freespace: int

@dataclass
class Node:
    val: int
    next: None