#!/usr/bin/env python


"""--- Day 18: Snailfish ---"""



import sys
import math
import copy

class Node:
    left = None
    right = None
    value = None
    parent = None

    def __init__(self, left, right, parent=None, value=None):
        self.left = left
        self.right = right
        self.value = value
        self.parent = parent

    def __str__(self):
        return "[Node {}]".format(self.value)


def print_tree(node):
    while node.parent:
        node = node.parent
    print_node(node)
    print("")


def print_node(node):
    if node is None:
        print("None", end="")
    elif node.value is not None:
        print(node.value, end="")
    else:
        print("[", end="")
        print_node(node.left)
        print(", ", end="")
        print_node(node.right)
        print("]", end="")
  

def parse_number(input):
    stack = []
    number = []
    for symbol in input:
        if symbol == "[":
            stack.append(symbol)
        elif symbol == "]":
            right = stack.pop()
            left = stack.pop()
            assert("[" == stack.pop())
            node = Node(left, right)
            left.parent = node
            right.parent = node
            stack.append(node)
        elif symbol.isnumeric():
            stack.append(Node(None, None, value=int(symbol)))
        elif symbol == ",":
            pass
        else:
            raise("unknown symbol")
    return stack.pop()


def read_input(fin):
    numbers = [parse_number(line.strip()) for line in fin.readlines()]
    return numbers


def add(a, b):
    node = Node(copy.deepcopy(a), copy.deepcopy(b))
    node.left.parent = node
    node.right.parent = node
    reduce(node)
    return node


def left_neighbor(node):
    n = node
    while n is not None:
        if n.parent and n.parent.left is not n:
            n = n.parent.left
            break
        n = n.parent
    if n is None:
        return None
    while n.value is None:
        n = n.right
    return n


def right_neighbor(node):
    n = node
    while n is not None:
        if n.parent and n.parent.right is not n:
            n = n.parent.right
            break
        n = n.parent
    if n is None:
        return None
    while n.value is None:
        n = n.left
    return n


def replace(parent, old_child, new_child):
    if parent.left is old_child:
        parent.left = new_child
    elif parent.right is old_child:
        parent.right = new_child
    else:
        raise("Could not find old node in children")


def explode(node):
    left = left_neighbor(node)
    if left is not None:
        left.value += node.left.value
    right = right_neighbor(node)
    if right is not None:
        right.value += node.right.value
    replace(node.parent, node, Node(None, None, value=0, parent=node.parent))


def split(node):
    assert(node.value is not None)
    assert(node.parent is not None)
    node.left = Node(None, None, value=math.floor(node.value/2), parent=node)
    node.right = Node(None, None, value=math.ceil(node.value/2), parent=node)
    node.value = None


def reduce_action(root, action):
    stack = [(root, 0)]
    while not len(stack) == 0:
        node, depth = stack.pop()
        if action == "explode" and depth == 4 and node.value is None:
            explode(node)
            return True
        if action == "split" and node.value and node.value >= 10:
            split(node)
            return True
        if node.right:
            stack.append((node.right, depth+1))
        if node.left:
            stack.append((node.left, depth+1))
    return False


def reduce(node):
    while True:
        if reduce_action(node, "explode"):
            continue
        if reduce_action(node, "split"):
            continue
        break

def magnitude(node):
    if node.value is not None:
        return node.value
    else:
        return 3*magnitude(node.left) + 2*magnitude(node.right)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day18_snailfish_part2.py <input file>")
        sys.exit(-1)

    with open(sys.argv[1], 'r') as fin:
        numbers = read_input(fin)
    max_magnitude = 0
    for number1 in range(len(numbers)):
        for number2 in range(len(numbers)):
            print("add", number1, number2)
            print_tree(numbers[number1])
            print("+")
            print_tree(numbers[number2])
            print("=")
            result = add(numbers[number1], numbers[number2])
            print_tree(result)
            result_magnitude = magnitude(result)
            max_magnitude = max(max_magnitude, result_magnitude)
    print(max_magnitude)