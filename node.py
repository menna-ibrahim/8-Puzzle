class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = 0

<<<<<<< HEAD
class Nodestar:
    def __init__(self, node,h):
        self.node = node
        self.h=h
    def __lt__(self, other):
        return self.h < other.h
=======

class Nodestar:
    def __init__(self, node, f):
        self.node = node
        self.f = f

    def __lt__(self, other):
        return self.f < other.f
>>>>>>> dd5e7b5a6f6b0509ba432c821bde44075d976286
