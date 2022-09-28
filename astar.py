import numpy as np
from Map import Map_Obj

# Først inspirasjon fra disse, men så insipirert fra vedlegget og boka og ved å studere map_obj sin kildekode
# https://github.com/jrialland/python-astar/blob/master/astar/__init__.py
# https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
# https://github.com/VaibhavSaini19/A_Star-algorithm-in-Python/blob/master/A-Star%20Algorithm


map_obj = Map_Obj(task=1)

# map_obj.show_map()
# int_map, str_map = map_obj.get_maps()
# print(int_map)
# print(str_map)

# start_pos = map_obj.get_start_pos()
# goal_pos = map_obj.get_goal_pos()
# start_val = map_obj.get_cell_value(start_pos)
# goal_val = map_obj.get_cell_value(goal_pos)
# print(start_pos, goal_pos, start_val, goal_val, sep="\n")



# Class to keep track of cells as nodes
class Node:

    def __init__(self, position, value, parent = None, kids = None, g = None, h = None, f = None):
        self.x_pos = position[0]
        self.y_pos = position[1]
        self.state = position
        self.value = value
        self.parent = parent
        self.kids = kids
        self.g = g
        self.h = h
        self.f = f
        self.closed = False


# Generate successors to a given node
# Helper function for astar
def generate_successors(node, map_obj):
    successors = []
    x = node.x_pos
    y = node.y_pos
    if x-1>=0:
        successors.append(Node([x-1,y], map_obj.get_cell_value([x-1,y]), parent=node))
    if x+1<=46:
        successors.append(Node([x+1,y], map_obj.get_cell_value([x+1,y]), parent=node))
    if y-1>=0:
        successors.append(Node([x,y-1], map_obj.get_cell_value([x,y-1]), parent=node))
    if y+1<=38:
        successors.append(Node([x,y+1], map_obj.get_cell_value([x,y+1]), parent=node))
    node.kids = successors

# start_node = Node(map_obj.get_start_pos(), map_obj.get_cell_value(map_obj.get_start_pos()))
# start_node = Node([22,18], map_obj.get_cell_value(map_obj.get_start_pos()))
# generate_successors(start_node, map_obj)
# for node in start_node.kids:
#     print(node.state, node.value, node.parent)

# Manhattan distance
def heuristic(node, goal_node):
    return abs(node.x_pos - goal_node.x_pos) + abs(node.y_pos - goal_node.y_pos)

def astar(start_node, goal_node, map_obj):
    open_nodes = [] # Open nodes contain nodes in ascending f-value
    closed_nodes = []
    start_node.g = 0
    start_node.h = heuristic(start_node, goal_node)
    start_node.f = start_node.g + start_node.h
    open_nodes.append(start_node)
    # Agenda loop
    while True:
        if not len(open_nodes):
            return "Failure" # Returning failure
        current_node = open_nodes.pop(0)
        current_node.closed = True
        closed_nodes.append(current_node)
        if current_node.state == goal_node.state:
            return "Succeed" # Returning succeed
        successors = generate_successors(current_node)
        for node in successors:
            pass # må implementere if else fra pseudo


# astar(Node(start_pos, start_val), Node(goal_pos, goal_val))