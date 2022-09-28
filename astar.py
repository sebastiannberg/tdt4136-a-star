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

start_pos = map_obj.get_start_pos()
goal_pos = map_obj.get_goal_pos()
start_val = map_obj.get_cell_value(start_pos)
goal_val = map_obj.get_cell_value(goal_pos)
# print(start_pos, goal_pos, start_val, goal_val, sep="\n")



# Class to keep track of nodes when searching
# Nodes are created from cells in the map of samfundet provided by tdt4136 via Map.py and csv files
class Node:

    def __init__(self, position, value, parent = None, kids = [], g = None, h = None, f = None):
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
def generate_successors(node, map_obj):
    successors = []
    x = node.x_pos
    y = node.y_pos
    if x-1>=0 and map_obj.get_cell_value([x-1,y]) > 0:
        successors.append(Node([x-1,y], map_obj.get_cell_value([x-1,y])))
    if x+1<=46 and map_obj.get_cell_value([x+1,y]) > 0:
        successors.append(Node([x+1,y], map_obj.get_cell_value([x+1,y])))
    if y-1>=0 and map_obj.get_cell_value([x,y-1]) > 0:
        successors.append(Node([x,y-1], map_obj.get_cell_value([x,y-1])))
    if y+1<=38 and map_obj.get_cell_value([x,y+1]) > 0:
        successors.append(Node([x,y+1], map_obj.get_cell_value([x,y+1])))
    return successors

# Updating parent and computing f value
def attach_and_eval(child, parent, goal_node):
    child.parent = parent
    child.g = parent.g + child.value
    child.h = heuristic(child, goal_node)
    child.f = child.g + child.h

# Ensure all nodes in search graph always aware of the current best parent and g value
def propagate_path_improvements(parent):
    for child in parent.kids:
        if parent.g + child.value < child.g:
            child.parent = parent
            child.g = parent.g + child.value
            child.f = child.g + child.h
            propagate_path_improvements(child)

# Manhattan distance used as admissable heuristic
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
            return (closed_nodes, current_node) # Succeed
        successors = generate_successors(current_node, map_obj)
        for node in successors:
            # Check if state already exists, then set node to already created node
            for closed_node in closed_nodes:
                if node.state == closed_node.state:
                    node = closed_node
            for open_node in open_nodes:
                if node.state == open_node.state:
                    node = open_node
            current_node.kids.append(node)
            if node not in open_nodes and node not in closed_nodes:
                attach_and_eval(node, current_node, goal_node)
                open_nodes.append(node)
                if len(open_nodes) > 0:
                    open_nodes.sort(key=lambda a: a.f) # Sort open_nodes by ascending f
            elif current_node.g + node.value < node.g: # Found cheaper path to node via current_node
                attach_and_eval(node, current_node, goal_node)
                if node in closed_nodes:
                    propagate_path_improvements(node)


closed, current = astar(Node(start_pos, start_val), Node(goal_pos, goal_val), map_obj)