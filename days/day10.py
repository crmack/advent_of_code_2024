from utils.funcs import valid_pos
from utils.printy import print2dArray
from utils.structs import Point2DWithVal as PVal

FINISH_VAL = 9
MOVES = [PVal(-1,0,0), PVal(1,0,0), PVal(0,-1,0), PVal(0,1,0)]

def take_steps(grid, startPVal, sx, sy):
    # Check all possible steps from a given location, returning all which are valid
    valid_steps = []

    for move in MOVES:
        x = startPVal.x + move.x
        y = startPVal.y + move.y
        if valid_pos(x,y,sx,sy) and int(grid[y][x]) == startPVal.val+1:
            valid_steps.append(PVal(x,y,startPVal.val+1))

    return valid_steps

def walk(grid, trailhead):
    # From a trailhead, check all possible steps, then repeat with those results until there are no more possible steps
    # or you have reached the FINISH_VAL (end of trail) 
    sy = len(grid)
    sx = len(grid[0])

    steps = [trailhead]
    results = {}
    while len(steps) > 0:
        new_steps = []
        for step in steps:
            tmp_steps = take_steps(grid, step, sx, sy)
            for ns in tmp_steps:
                if ns.val == FINISH_VAL:
                    s = f"{ns.x},{ns.y}"
                    if s not in results:
                        results[s] = 1
                    else:
                        results[s] += 1
            new_steps += tmp_steps
        steps = new_steps

    total = 0
    for v in results.values():
        total += v

    # Return the number of unique trailhead-->top results
    # AND the total number of paths to a top for this trailhead
    return (len(results), total)

def part1(input):
    total = 0

    # Find all zeros
    trailheads = []
    for y in range(0, len(input)):
        for x in range(0, len(input[y])):
            if int(input[y][x]) == 0:
                trailheads.append(PVal(x, y, 0))
    
    # for each zero, walk to all possible 9s
    rating = 0
    for th in trailheads:
        t, v = walk(input, th)
        total += t
        rating += v

    return (total, rating)

def run(file_name):
    input = []
    with open(file_name, 'r') as file:
        for line in file:
            input.append(line.replace('\n', '').replace(' ', ''))

    result1, result2 = part1(input)
    print(f"Day 10 - Part 1: {result1}")
    print(f"Day 10 - Part 2: {result2}")