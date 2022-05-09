from node import *
from board import *
from time import time


def bfs(node: Node, goal):

    start_time = time()
    queue = [node]  # frontiers queue
    frontier_set = {node.state}
    explored = {node.state}  # visited nodes
    path_stack = []  # stack to backtrack the path to goal
    nodes_expanded = 0

    while queue:
        current_node = queue.pop(0)
        nodes_expanded += 1
        explored.add(current_node.state)
        frontier_set.remove(current_node.state)     # remove from frontiers set also
        # goal is the current node --> stop
        if current_node.state == goal:
            path_stack.append(current_node)
            # push to the stack the path backwards to pop it correctly
            while current_node.parent:
                current_node = current_node.parent
                path_stack.append(current_node)
            end_time = time()
            elapsed_time = end_time - start_time
            return path_stack, nodes_expanded, elapsed_time
        # enqueue unvisited frontiers in queue to explore them later
        for frontier in frontiers(current_node):
            if frontier.state not in explored.union(frontier_set):
                frontier.depth = current_node.depth + 1
                frontier_set.add(frontier.state)
                queue.append(frontier)

    return None
