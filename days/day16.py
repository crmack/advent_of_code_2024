import heapq

from utils.printy import print2dArray
from utils.structs import Point2D as P

MOVES = [P(1,0), P(0,1), P(-1,0), P(0,-1)]

def find_start_end_and_walls(grid):
    start = []
    end = []
    walls = []
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == 'S':
                start = (y,x)
            elif col == 'E':
                end = (y,x)
            elif col == '#':
                walls.append((y,x))

    return start, end, walls

def dijkstra(start, end, walls):
    # Disktra's algorithm for shortest path.
    # Didn't use this code, but got the idea from: https://www.datacamp.com/tutorial/dijkstra-algorithm-in-python
    # Needed to cost based on whether or not the next move required a turn

    # heapq is a priority queue algorithm implementation.
    # https://docs.python.org/3/library/heapq.html#
    # With the queue defined below, it will always keep the lowest cost first in the heap.
    # This makes it safe to break as soon as we hit the end, because we know we will have hit the cheapest route

    # the tuple will be cost, position, direction
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
            # straight moves (same dir_idx which don't hit walls) cost 1
            heapq.heappush(q,(cost+1, next_move, dir_idx))
        # Turning 90 degrees (new dir_idx) costs 1000
        heapq.heappush(q,(cost+1000, pos, (dir_idx+1)%4))
        heapq.heappush(q,(cost+1000, pos, (dir_idx-1)%4))


def part1(grid):
    start, end, walls = find_start_end_and_walls(grid)
    cost = dijkstra(start, end, walls)

    return cost

def dijkstra_2(start, end, walls):
    # Same as above except we need to know the unique tiles across ALL optimal paths


    # the tuple will be cost, position, direction, and a list of the best instructions (string with S, R/L for straight or turns)
    # tried counting but it will only give the result for the best single route, so need to keep instruction sets for the best routes
    q = [(0, start, 0, '')]
    # We will store all of the best paths instead of breaking on the first
    paths = []
    best_cost = 1000000000
    # Need to track cost as a given point and heading
    seen = {}
    while q:
        cost, pos, dir_idx, path = heapq.heappop(q)
        if cost > best_cost:
            # heapq ensures we only look at cheapest, so if we ever get a cost that is greater than an already found total cost, we are safe to be done
            break
        if (pos, dir_idx) in seen and seen[(pos,dir_idx)] < cost:
            # If the new cost is less than the previously seen cost, keep going...this is probably applicable to the P1 Dijkstra...
            # but that worked anyway. It is necessary here, however
            continue
        if pos == end:
            paths.append(path)
            best_cost = cost

        seen[(pos,dir_idx)] = cost

        next_moves = (pos[0]+MOVES[dir_idx].y, pos[1]+MOVES[dir_idx].x)
        if next_moves not in walls: 
            # straight moves (same dir_idx which don't hit walls) cost 1
            heapq.heappush(q,(cost+1, next_moves, dir_idx, path+'S'))
        # Turning 90 degrees (new dir_idx) costs 1000
        heapq.heappush(q,(cost+1000, pos, (dir_idx+1)%4, path+'R'))
        heapq.heappush(q,(cost+1000, pos, (dir_idx-1)%4, path+'L'))

    # Now retrace the steps
    # playback each of the optimal paths (strings of S/R/L)
    # Track unique tiles in this playback, total number at the end is the answer
    tiles = set()
    tiles.add(start)
    for p in paths:        
        cur_pos, dir_idx = (start, 0)
        for step in p:
            if step == 'S':
                # Only "straight" moves actually move
                cur_pos = (cur_pos[0] + MOVES[dir_idx].y, cur_pos[1] + MOVES[dir_idx].x)
                tiles.add(cur_pos)
            elif step == 'L': 
                dir_idx = (dir_idx-1)%4
            elif step == 'R': 
                dir_idx = (dir_idx+1)%4

    return len(tiles)

def part2(grid):
    start, end, walls = find_start_end_and_walls(grid)
    cost = dijkstra_2(start, end, walls)

    return cost


def run(file_name):
    grid = []
    with open(file_name, 'r') as file:
        for line in file:
            grid.append(list(line.replace('\n', '')))

    result1 = part1(grid)
    result2 = part2(grid)
    print(f"Day 16 - Part 1: {result1}")
    print(f"Day 16 - Part 2: {result2}")
