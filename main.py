from sys import exit
from board import *
from node import *
from bfs import bfs
<<<<<<< HEAD
from astar import a_star
from dfs import dfs
=======
from dfs import dfs
from a_star import a_star
>>>>>>> dd5e7b5a6f6b0509ba432c821bde44075d976286


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


if __name__ == '__main__':

    goal = "012345678"
    while True:
        state = input("Initial State : ")
        check = check_input(state)
        check_solv = check_solvable(state)
        if check:
            print("Valid State")
            if check_solv:
                node = Node(state, None, None)
            else:
                print("Unsolvable !!!")
                exit()
        else:
            print("Invalid !!!")
            exit()

        algorithm = input("Select Algorithm :\n1 for BFS\n2 for DFS\n3 for A star.\n")
        cost = 0

        # BFS
        if algorithm == "1":
            path, nodes_expanded, elapsed_time = bfs(node, goal)
        # DFS
        elif algorithm == "2":
            path, nodes_expanded, elapsed_time = dfs(node, goal)
        # A star
        elif algorithm == "3":
            path, nodes_expanded, elapsed_time = a_star(node, goal)
        else:
            print("Invalid Algorithm.")
            exit()

        # solution found
        if path:
            goal_node = path.pop(0)
            for i in range(len(path)):
                step = path.pop()
                print_board(step)
                cost += 1

            print_board(goal_node)
            print(f"Cost = {cost}")
            print(f"Nodes expanded = {nodes_expanded}")
            print(f"Depth = {goal_node.depth}")
            print(f"Running time of BFS = {elapsed_time} seconds.")

        else:
            print("No Solution")
