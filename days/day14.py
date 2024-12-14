import math
import re

from utils.funcs import twoDZeros as td
from utils.printy import print2dArray
from utils.structs import Guard as G

RE_NUM = r"-?\d+"

def move_guard(guard, maxx, maxy):
    newx = guard.x + guard.vx
    newy = guard.y + guard.vy

    if newx < 0:
        newx = newx + maxx + 1
    if newx > maxx:
        newx = newx - maxx - 1
    if newy < 0:
        newy = newy + maxy + 1
    if newy > maxy:
        newy = newy - maxy - 1

    return G(newx, newy, guard.vx, guard.vy)

def find_quadrant(guard, midx, midy):
    if guard.x < midx and guard.y < midy:
        return 0 #TL
    if guard.x > midx and guard.y < midy:
        return 1 #TR
    if guard.x < midx and guard.y > midy:
        return 2 #BL
    if guard.x > midx and guard.y > midy:
        return 3 #BR
    
    return -1


def calculate_quadrants(guards, maxx, maxy):
    midx = int(maxx / 2)
    midy = int(maxy / 2)

    #TL, TR, BL, BR
    quads = [0,0,0,0]
    for guard in guards:
        idx = find_quadrant(guard, midx, midy)
        if idx >= 0:
            quads[idx] += 1

    return quads

def print_grid(guards, maxx, maxy, n):
    grid = td(maxx, maxy)

    for g in guards:
        grid[g.y][g.x] += 1

    # Looking at each frame for a few minutes, I found that every 101st frame was aligning way differently than the others,
    # viewing only those frames led me to the answer pretty quickly
    if n > 1000 and (n - 1003) % 101 == 0:
    # if n == 7568: # this was my answer, just wanted to verify
        print2dArray(grid)
        print("***********")
        print("***********")
        print("***********")
        print("***********")
        print("***********")
        print(f"That was the {n}th second")
        input("Press Enter to continue...")


def part1(guards, maxx, maxy, n_turns, do_print=False):

    for n in range(0, n_turns):
        for idx, guard in enumerate(guards):
            guards[idx] = move_guard(guard, maxx, maxy)
        if do_print:
            print_grid(guards, maxx, maxy, n)

    quads = calculate_quadrants(guards, maxx, maxy)

    return math.prod(quads)

def run(file_name):
    guards = []
    maxx = 0
    maxy = 0

    with open(file_name, 'r') as file:
        for line in file:
            nums = re.findall(RE_NUM, line.replace('\n', ''))
            guards.append(G(int(nums[0]), int(nums[1]), int(nums[2]), int(nums[3])))
            if int(nums[0]) > maxx:
                maxx = int(nums[0])
            if int(nums[1]) > maxy:
                maxy = int(nums[1])

    print(f"maxx: {maxx}, maxy: {maxy}")
    # result1 = part1(guards, maxx, maxy, 100)
    result2 = part1(guards, maxx, maxy, 10000, True)
    print(f"Day 14 - Part 1: {result1}")
    print(f"Day 14 - Part 2: {result2}")
