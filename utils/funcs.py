import math
from utils.structs import Node

def valid_pos(x, y, size_x, size_y):
    if x >= 0 and y >= 0 and x < size_x and y < size_y:
        return True
    
    return False

def count_nodes(head):
    count = 0

    while head is not None:
        count += 1
        head = head.next

    return count

def split_ll_in_half(head):
    if head is None or head.next is None:
        return (head, None)
    
    half = int(math.floor(count_nodes(head)/2))

    h2 = head
    for i in range(0, half):
        temp = h2.next
        if i == half - 1:
            h2.next = None

        h2 = temp

    return (head, h2)

def twoDZeros(x, y):
    return [ [0]*(x+1) for _ in range(y+1) ]

def twoDWhatevers(x, y, whatever):
    return [ [whatever]*(x) for _ in range(y) ]