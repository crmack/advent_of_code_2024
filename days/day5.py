import math
import re
from functools import cmp_to_key
from utils.structs import Rule

RULES_RE = r"[0-9]+"

def check_rules(first, second, rules):
    for rule in rules:
        if rule.first == second and rule.second == first:
            return False
        
    return True

def check_needs_swap(first, second, rules):
    for rule in rules:
        if rule.first == first and rule.second == second:
            return -1
        
    return 0

def check_order(order, rules, idx=0):
    for i in range(idx, len(order)-1):
        if not check_rules(order[i], order[i+1], rules):
            return 0
        return check_order(order, rules, idx+1)

    return int(order[math.floor(len(order)/2.0)])

def reorder(order, rules):
    cmp = cmp_to_key(lambda first, second: check_needs_swap(first, second, rules))
    order = sorted(order, key=cmp)

    return int(order[math.floor(len(order)/2.0)])

def part1(rules, orders):
    count = 0

    for order in orders:
        count += check_order(order, rules)

    return count

def part2(rules, orders):
    count = 0

    incorrect = []
    for order in orders:
        if not check_order(order, rules):
            incorrect.append(order)

    for order in incorrect:
        count += reorder(order, rules)

    return count

def run(file_name):
    rules = []
    orders = []
    with open(file_name, 'r') as file:
        for line in file:
            if '|' in line:
                vals = re.findall(RULES_RE, line.replace('\n', ''))
                rules.append(Rule(vals[0], vals[1]))
            elif ',' in line:
                orders.append(line.replace('\n', '').split(','))

    result1 = part1(rules, orders)
    result2 = part2(rules, orders)
    print(f"Day 5 - Part 1: {result1}")
    print(f"Day 5 - Part 2: {result2}")