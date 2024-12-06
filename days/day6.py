import numpy as np
import re

from utils.printy import print2dArray
from utils.structs import Point2D

STARTING_RE = r"[\^v<>]"

def get_heading_from_symbol(symbol):
    if symbol == '^':
        return Point2D(0,-1)
    elif symbol == 'v':
        return Point2D(0,1)
    elif symbol == '<':
        return Point2D(-1,0)
    elif symbol == '>':
        return Point2D(1,0)
    
def did_exit(layout, location):
    if location.x < 0 or location.y < 0 or location.x >= len(layout[0]) or location.y >= len(layout):
        return True

    return False

def rotate(symbol):
    if symbol == '^':
        return '>'
    elif symbol == 'v':
        return '<'
    elif symbol == '<':
        return '^'
    elif symbol == '>':
        return 'v'

def move(layout, current_location, symbol):
    done = True
    heading = get_heading_from_symbol(symbol)

    new_loc = Point2D(current_location.x + heading.x, current_location.y + heading.y)
    if not did_exit(layout, new_loc):
        done = False
        if layout[new_loc.y][new_loc.x] == '#':
            symbol = rotate(symbol)
            new_loc = current_location

    return (done, new_loc, symbol)

def part1(input, location, symbol):
    visit_counts = np.zeros((len(input[0]), len(input)), dtype=int)
    visit_counts[location.y,location.x] = 1
    exited = False
    while not exited:
        exited, location, symbol = move(input, location, symbol)
        if not exited:
            visit_counts[location.y,location.x] = 1

    print(visit_counts)
    return visit_counts.sum()

def part2(input):
    return 0


def run(file_name):
    input = []
    starting_location = Point2D
    starting_symbol = ''
    with open(file_name, 'r') as file:
        for idx, line in enumerate(file):
            input.append(line.replace('\n', ''))
            start = re.search(STARTING_RE, line)
            if start:
                starting_location.x = start.start(0)
                starting_location.y = idx
                starting_symbol = line[start.start(0)]


    result1 = part1(input, starting_location, starting_symbol)
    result2 = part2(input)
    print(f"Day 6 - Part 1: {result1}")
    print(f"Day 6 - Part 2: {result2}")
