from board import *
from time import time

<<<<<<< HEAD
def dfs(node: Node, goal):
    start_time = time()
    stack = [node] #frontiers stack
    explored_set={node.state} #explored nodes set
    frontier_set={node.state}
    path_stack=[] #path of the solution
    expanded_nodes=0 #number of expanded nodes

    while stack:
        current_node=stack.pop(-1) #pop one from the stack
        expanded_nodes+=1
        explored_set.add(current_node.state) #add state to explored state
        if current_node.state==goal: #if the goal is reached, prepare path
            path_stack.append(current_node)
            while current_node.parent:
                current_node=current_node.parent
                path_stack.append(current_node)
            end_time=time()
            elapsed_time=end_time-start_time
            return path_stack, expanded_nodes, elapsed_time
        else: #add children nodes to frontier stack
            for f in frontiers(current_node):
                if f.state not in explored_set.union(frontier_set):
                    f.depth=current_node.depth+1
                    frontier_set.add(f.state)
                    stack.append(f)

    return None
=======

def dfs(node: Node, goal):
    start_time = time()
    stack = [node]  # frontiers stack
    explored_set = {node.state}     # explored nodes set
    frontier_set = {node.state}
    path_stack = []  # path of the solution
    expanded_nodes = 0  # number of expanded nodes

    while stack:
        current_node = stack.pop(-1)  # pop one from the stack
        frontier_set.remove(current_node.state)
        expanded_nodes += 1
        explored_set.add(current_node.state)  # add state to explored state
        if current_node.state == goal:  # if the goal is reached, prepare path
            path_stack.append(current_node)
            while current_node.parent:
                current_node = current_node.parent
                path_stack.append(current_node)
            end_time = time()
            elapsed_time = end_time-start_time
            return path_stack, expanded_nodes, elapsed_time
        else:
            # add children nodes to frontier stack
            for f in frontiers(current_node):
                if f.state not in explored_set.union(frontier_set):
                    f.depth = current_node.depth + 1
                    frontier_set.add(f.state)
                    stack.append(f)

    return None
>>>>>>> dd5e7b5a6f6b0509ba432c821bde44075d976286
