import heapq
import re
import math

from utils.funcs import twoDWhatevers
from utils.printy import print2dArray
from utils.structs import Point2D as P

RE_NUM = r"-?\d+"
MOVES = [P(1,0), P(0,1), P(-1,0), P(0,-1)]

def dijkstra(start, end, walls):
    # Same as Day 16 except turning is free and you can turn 180
    q = [(0, start, 0)]
    seen = set()
    while q:
        cost, pos, dir_idx = heapq.heappop(q)
        if (pos, dir_idx) in seen:
            continue
        if pos == end: 
            return cost

        seen.add((pos,dir_idx))

        next_move = (pos[0]+MOVES[dir_idx].y, pos[1]+MOVES[dir_idx].x)
        if next_move not in walls:
            heapq.heappush(q,(cost+1, next_move, dir_idx))
        heapq.heappush(q,(cost, pos, (dir_idx+1)%4))
        heapq.heappush(q,(cost, pos, (dir_idx-1)%4))
        heapq.heappush(q,(cost, pos, (dir_idx-2)%4))

def part1(instructions, n_to_run, sx, sy):
    walls = instructions[:n_to_run]

    # Easiest way to handle edges is to add a boarder of walls
    for x in range(0, sx):
        walls.append((-1,x))
        walls.append((sy,x))

    for y in range(0, sy):
        walls.append((y,-1))
        walls.append((y,sx))

    steps = dijkstra((0,0), (sy-1,sx-1), walls)

    return steps

def part2(instructions, sx, sy):
    # Just do a binary search until it converges on the last solve-able instruction and the first unsolveable
    l = len(instructions)
    n = int(l/2)
    upper_bound = l
    lower_bound = 0
    while True:
        walls = instructions[:n]
        for x in range(0, sx):
            walls.append((-1,x))
            walls.append((sy,x))

        for y in range(0, sy):
            walls.append((y,-1))
            walls.append((y,sx))

        res = dijkstra((0,0), (sy-1,sx-1), walls)

        if res is None:
            if n < upper_bound:
                upper_bound = n
        else:
            if n > lower_bound:
                lower_bound = n

        if upper_bound == lower_bound+1:
            return instructions[lower_bound]

        n = math.floor((upper_bound + lower_bound)/2)
    

def run(file_name):
    instructions = []
    with open(file_name, 'r') as file:
        for line in file:
            nums = re.findall(RE_NUM, line)
            instructions.append((int(nums[1]), int(nums[0])))

    result1 = part1(instructions, 1024, 71, 71)
    result2 = part2(instructions, 71, 71)
    print(f"Day 18 - Part 1: {result1}")
    print(f"Day 18 - Part 2: {result2} (Make sure to flip these for the answer entry)")
