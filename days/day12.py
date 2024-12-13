from functools import cache
from utils.funcs import valid_pos
from utils.printy import print2dArray
from utils.structs import Point2D as P

COUNTED_VAL = '.'
MOVES = [P(-1,0), P(1,0), P(0,-1), P(0,1)]

def take_steps(grid, startPoint, val, sx, sy):
    # Check all possible steps from a given location, returning all which are valid
    valid_steps = []

    for move in MOVES:
        x = startPoint.x + move.x
        y = startPoint.y + move.y
        if valid_pos(x,y,sx,sy) and grid[y][x] == val:
            valid_steps.append(P(x,y))

    return valid_steps

def perimeter_from_set(index_list):
    p = 0
    for spot in index_list:
        for move in MOVES:
            new_spot = [spot[0] + move.x, spot[1] + move.y]
            if new_spot not in index_list:
                p += 1

    return p

def all_dir_same(list, point, dir):
    for l in list:
        if l[dir] != point[dir]:
            return False
        
    return True

def check_diagonals(group, point, neighbors):
    minx = point[0]
    miny = point[1]
    maxx = point[0]
    maxy = point[1]
    for n in neighbors:
        minx = min(minx, n[0])
        maxx = max(maxx, n[0])
        miny = min(miny, n[1])
        maxy = max(maxy, n[1])

    corners = 0
    tl = [minx, miny]
    if tl not in neighbors and tl not in group:
        corners += 1
    tr = [maxx, miny]
    if tr not in neighbors and tr not in group:
        corners += 1
    bl = [minx, maxy]
    if bl not in neighbors and bl not in group:
        corners += 1
    br = [maxx, maxy]
    if br not in neighbors and br not in group:
        corners += 1

    return corners


def count_corners(point, points):
    neighbors = []
    for move in MOVES:
        new_spot = [point[0] + move.x, point[1] + move.y]
        if new_spot in points:
            neighbors.append(new_spot)
    
    n = len(neighbors)
    if n == 0:
        return 4
    if n == 1:
        return 2
    if n == 2:
        if all_dir_same(neighbors, point, 0) or all_dir_same(neighbors, point, 1):
            return 0      
        return 1 + check_diagonals(points, point, neighbors)
    if n == 3:
        # maybe 2, but check both diagonals created by the neighbors
        return check_diagonals(points, point, neighbors)
    if n == 4:
        # 0-4, potentially
        return check_diagonals(points, point, neighbors)

    return 0

def perimeter_part_2(index_list):
    sides = 0
    for spot in index_list:
        s = count_corners(spot, index_list)
        sides += s
        

    return sides

def grow_area(grid, point, use_perimeter_sides=False):
    sy = len(grid)
    sx = len(grid[0])
    val = grid[point.y][point.x]

    unique_spots = [[point.x,point.y]]
    steps = [point]
    while len(steps) > 0:
        new_steps = []
        for step in steps:
            tmp_steps = take_steps(grid, step, val, sx, sy)
            for ns in tmp_steps:
                grid[ns.y] = grid[ns.y][:ns.x] + COUNTED_VAL + grid[ns.y][ns.x + 1:]
                t = [ns.x, ns.y]
                if t not in unique_spots:
                    unique_spots.append(t)
            new_steps += tmp_steps
        steps = new_steps

    if use_perimeter_sides:
        return (perimeter_part_2(unique_spots), len(unique_spots))
    
    return (perimeter_from_set(unique_spots), len(unique_spots))

def part1(grid):
    count = 0

    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x] != COUNTED_VAL:
                p, a = grow_area(grid, P(x,y))
                count += (p * a)

    return count

def part2(grid):
    count = 0

    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x] != COUNTED_VAL:
                p, a = grow_area(grid, P(x,y), True)
                count += (p * a)


    return count

def run(file_name):
    input = []
    input2 = []
    with open(file_name, 'r') as file:
        for line in file:
          input.append(line.replace('\n', '') )
          input2.append(line.replace('\n', '') )

    result1 = part1(input)
    result2 = part2(input2)
    print(f"Day 12 - Part 1: {result1}")
    print(f"Day 12 - Part 2: {result2}")