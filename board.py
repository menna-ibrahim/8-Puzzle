from node import *


size = 9


# check whether the input is a valid state for the 8 puzzle
def check_input(state):
    if len(state) != size:
        return False
    present = [False for i in range(size)]
    for ch in state:
        # ascii comparison
        if ord('0') <= ord(ch) <= ord('8'):
            digit = int(ch)
            if present[digit]:
                return False
            else:
                present[digit] = True
        else:
            return False
    return True


def check_solvable(state):
    inv_count = 0
    for i in range(9):
        for j in range(i + 1, 9):
            if state[i] != "0" and state[j] != "0" and state[i] > state[j]:
                inv_count += 1
    return inv_count % 2 == 0


# print the state as a board style in console
def print_board(node: Node):
    if node.action:
        print(node.action)
    for i in range(size):
        if i % 3 == 0 and i != 0:
            print("")
        print(node.state[i], end="")
    print("\n")


# find the index of the zero
def find_zero(state):
    for i in range(size):
        if state[i] == '0':
            return i


# swap the zero with the desired index
def swap(state, i, j):
    new_state = list(state)
    new_state[i], new_state[j] = new_state[j], new_state[i]
    return ''.join(new_state)


# swap up if possible
def up(node: Node):
    zero = find_zero(node.state)
    if zero > 2:
        new_state = swap(node.state, zero, zero-3)
        frontier = Node(new_state, node, "Up")
        return frontier
    return None


# swap down if possible
def down(node: Node):
    zero = find_zero(node.state)
    if zero < 6:
        new_state = swap(node.state, zero, zero+3)
        frontier = Node(new_state, node, "Down")
        return frontier
    return None


# swap left if possible
def left(node: Node):
    zero = find_zero(node.state)
    if zero not in [0, 3, 6]:
        new_state = swap(node.state, zero, zero-1)
        frontier = Node(new_state, node, "Left")
        return frontier
    return None


# swap right if possible
def right(node: Node):
    zero = find_zero(node.state)
    if zero not in [2, 5, 8]:
        new_state = swap(node.state, zero, zero+1)
        frontier = Node(new_state, node, "Right")
        return frontier
    return None


# return all possible frontiers of a state node
def frontiers(node: Node):
    frontier_list = []
    frontier_up = up(node)
    frontier_left = left(node)
    frontier_down = down(node)
    frontier_right = right(node)

    parent = node.parent

    if frontier_up:
        if parent:
            if frontier_up.state != parent.state:
                frontier_list.append(up(node))
        else:   # root node has no parent
            frontier_list.append(up(node))
    if frontier_left:
        if parent:
            if frontier_left.state != parent.state:
                frontier_list.append(left(node))
        else:   # root node has no parent
            frontier_list.append(left(node))

    if frontier_down:
        if parent:
            if frontier_down.state != parent.state:
                frontier_list.append(down(node))
        else:   # root node has no parent
            frontier_list.append(down(node))

    if frontier_right:
        if parent:
            if frontier_right.state != parent.state:
                frontier_list.append(right(node))
        else:   # root node has no parent
            frontier_list.append(right(node))

    return frontier_list



