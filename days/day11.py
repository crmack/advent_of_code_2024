from functools import cache

from utils.funcs import count_nodes, split_ll_in_half
from utils.printy import printWalkedNodes
from utils.structs import Node

N_BLINKS = 75

def blink(stone):
    if stone is None:
        return None
    
    v = stone.val
    s = str(v)

    if v == 0:
        return [1]
    if len(s) % 2 == 0:
        half = int(len(s)/2)
        r = []
        r.append(int(s[0:half]))
        r.append(int(s[half:]))
        return r

    return [v*2024]

def blink_ll(head_node):
    new_vals = blink(head_node)
    if new_vals:
        head_node.val = new_vals[0]
        if len(new_vals) == 1:
            next_node = head_node.next
        else:
            n = Node(new_vals[1], head_node.next)
            head_node.next = n
            next_node = n.next
        
        head_node = blink_ll(next_node)

    return head_node

def run_n_blinks(head, n_blinks):
    for i in range(0, n_blinks):
        blink_ll(head)

    return head

def split_and_run_n_blinks(head, n_blinks):
    h1, h2 = split_ll_in_half(head)
    h1 = run_n_blinks(h1, n_blinks)
    h2 = run_n_blinks(h2, n_blinks)

    return (h1, h2)

def part1(input):
    total = 0

    head = None
    for i in reversed(input):
        temp = Node(int(i), head)
        head = temp

    all = [head]
    for i in range(0, N_BLINKS):
        tmp = []
        for h in all:
            h1, h2 = split_and_run_n_blinks(h, 1)
            if h1 is not None:
                tmp.append(h1)
            if h2 is not None:
                tmp.append(h2)
        all = tmp

    for a in all:
        total += count_nodes(a)

    return total


@cache
def blink_2(str_val, blink_count=0):
    if blink_count == N_BLINKS:
        return 1
    
    if str_val == '0':
        return blink_2('1', blink_count + 1)
    
    if len(str_val) % 2 == 0:
        left = str_val[:int(len(str_val)/2)]
        right = str(int(str_val[int(len(str_val)/2):])) #str(int())kills leading zeros
        return blink_2(left, blink_count+1) + blink_2(right, blink_count+1)
    
    return blink_2(str(int(str_val)*2024), blink_count + 1)


def part2(input):
    count = 0
    for i in input:
        count += blink_2(i)

    return count

def run(file_name):
    with open(file_name, 'r') as file:
        input = file.read().replace('\n', '').split(' ')

    # result1 = part1(input)
    result2 = part2(input)
    # print(f"Day 11 - Part 1: {result1}")
    print(f"Day 11 - Part 2: {result2}")
