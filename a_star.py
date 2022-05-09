from board import *
import heapq as hq
from time import time
from math import sqrt

def heuristic(state, goal, mode):
    distance = 0
    for i in range(9):
        if state[i] == "0" or state[i] == goal[i]:
            continue
        if mode == 1:
            distance += abs(i // 3 - int(state[i]) // 3) + abs(i % 3 - int(state[i]) % 3)
        else:
            distance += sqrt(pow(i // 3 - int(state[i]) // 3, 2) + pow(i % 3 - int(state[i]) % 3,2))
    return distance


def decreaseKey(frontier, frontiers_heap, goal, mode):
    new_f = frontier.depth + heuristic(frontier.state, goal, mode)
    for heap_node in frontiers_heap:
        if heap_node.node.state == frontier.state:
            heap_node.node = frontier
            heap_node.f = min(heap_node.f, new_f)

def a_star(node: Node, goal, mode):
    start_time = time()
    path_stack = []  # stack to backtrack the path to goal
    nodes_expanded = 0
    h = heuristic(node.state, goal, mode)    # f(initial node) = h(initial node) ie: g(initial node) = 0
    node_star = Nodestar(node, h)   # special node for a-star algorithm
    frontiers_heap = [node_star]    # heap data structure to store frontiers
    hq.heapify(frontiers_heap)
    frontiers_set = {node.state}    # set data structure to store frontiers to search in avg O(1)
    explored = {node.state}         # set data structure to store explored nodes to search in avg O(1)

    while frontiers_heap:
        current_node = hq.heappop(frontiers_heap)   # pop node with minimum f
        frontiers_set.remove(current_node.node.state)   # remove it from set also
        nodes_expanded += 1
        explored.add(current_node.node.state)   # add it to explored

        # goal found
        if current_node.node.state == goal:
            path_stack.append(current_node.node)

            # push to the stack the path backwards to pop it correctly
            while current_node.node.parent:
                current_node.node = current_node.node.parent
                path_stack.append(current_node.node)
            end_time = time()
            elapsed_time = end_time - start_time
            return path_stack, nodes_expanded, elapsed_time

        # goal not found
        for frontier in frontiers(current_node.node):
            frontier.depth = current_node.node.depth + 1    # new frontier depth
            f = frontier.depth + heuristic(frontier.state, goal, mode)   # f(x) = h(x) + g(x)
            current_node_star = Nodestar(frontier, f) # special node for a-star algorithm

            # state not in explored nor frontiers --> push it to heap
            if frontier.state not in explored.union(frontiers_set):
                frontiers_set.add(frontier.state)
                hq.heappush(frontiers_heap, current_node_star)

            # state already in frontiers --> re evaluate the f(x)
            elif frontier.state in frontiers_set:
                decreaseKey(frontier, frontiers_heap, goal, mode)

    return None
