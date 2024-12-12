from utils.structs import Node

def print2dArray(array):
    for row in array:
        print(row)

def printWalkedNodes(node):
    if node is not None:
        print(node.val)
        printWalkedNodes(node.next)