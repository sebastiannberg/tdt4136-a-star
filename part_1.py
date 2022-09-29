from Map import Map_Obj
from astar import astar, Node
from visualizer import draw_map

def get_int_map(map_obj):
    return map_obj.get_maps()[0]

def update_start_goal(int_map, start_node, goal_node):
    int_map[start_node.x_pos][start_node.y_pos] = -2
    int_map[goal_node.x_pos][goal_node.y_pos] = -3

def update_closed_nodes(int_map, closed_nodes, start_node, goal_node):
    for node in closed_nodes:
        if node.state != start_node.state and node.state != goal_node.state:
            int_map[node.x_pos][node.y_pos] = 0

def update_path_nodes(int_map, current_node):
    while current_node.parent:
        if current_node.parent.parent: # If not start node
            int_map[current_node.parent.x_pos][current_node.parent.y_pos] = -4
        current_node = current_node.parent

# Task 1
map_obj1 = Map_Obj(task=1)
start_node1 = Node(map_obj1.get_start_pos(), map_obj1.get_cell_value(map_obj1.get_start_pos()))
goal_node1 = Node(map_obj1.get_goal_pos(), map_obj1.get_cell_value(map_obj1.get_goal_pos()))

closed, current = astar(start_node1, goal_node1, map_obj1)

int_map = get_int_map(map_obj1)
draw_map(int_map, False, "task1-1.png") # Draw initialized map
update_start_goal(int_map, start_node1, goal_node1)
draw_map(int_map, False, "task1-2.png") # Draw map with start and goal marked
update_closed_nodes(int_map, closed, start_node1, goal_node1)
draw_map(int_map, False, "task1-3.png") # Draw map with closed nodes marked
update_path_nodes(int_map, current)
draw_map(int_map, False, "task1-4.png") # Draw map with path nodes marked

# Task 2
map_obj2 = Map_Obj(task=2)
start_node2 = Node(map_obj2.get_start_pos(), map_obj2.get_cell_value(map_obj2.get_start_pos()))
goal_node2 = Node(map_obj2.get_goal_pos(), map_obj2.get_cell_value(map_obj2.get_goal_pos()))

closed, current = astar(start_node2, goal_node2, map_obj2)

int_map = get_int_map(map_obj2)
draw_map(int_map, False, "task2-1.png") # Draw initialized map
update_start_goal(int_map, start_node2, goal_node2)
draw_map(int_map, False, "task2-2.png") # Draw map with start and goal marked
update_closed_nodes(int_map, closed, start_node2, goal_node2)
draw_map(int_map, False, "task2-3.png") # Draw map with closed nodes marked
update_path_nodes(int_map, current)
draw_map(int_map, False, "task2-4.png") # Draw map with path nodes
