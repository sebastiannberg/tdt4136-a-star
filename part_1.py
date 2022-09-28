from Map import Map_Obj
from astar import astar, Node

map_obj1 = Map_Obj(task=1)
start_node1 = Node(map_obj1.get_start_pos(), map_obj1.get_cell_value(map_obj1.get_start_pos()))
goal_node1 = Node(map_obj1.get_goal_pos(), map_obj1.get_cell_value(map_obj1.get_goal_pos()))

closed, current = astar(start_node1, goal_node1, map_obj1)
print(closed, current, sep="\n")