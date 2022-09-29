from Map import Map_Obj
from astar import astar, Node
from visualizer import draw_map

def get_int_map(map_obj):
    """Generates integer map of a given map object

    Parameters
    ----------
    map_obj : Map_Obj
        The map object that contains description of
        the map

    Returns
    -------
    [[int]]
        An integer map describing the map
    """

    return map_obj.get_maps()[0]

def update_start_goal(int_map, start_node, goal_node):
    """Updates and integer map with start and goal node

    Parameters
    ----------
    int_map : [[int]]
        The integer map
    start_node : Node
        The start node
    goal_node : Node
        The goal node
    """

    int_map[start_node.x_pos][start_node.y_pos] = -2 # Values used by visualizer
    int_map[goal_node.x_pos][goal_node.y_pos] = -3

def update_closed_nodes(int_map, closed_nodes, start_node, goal_node):
    """Updates and integer map with closed nodes

    Parameters
    ----------
    int_map : [[int]]
        The integer map
    closed_nodes : [Node]
        A list of all the closed nodes after searching with astar
    start_node : Node
        The start node
    goal_node : Node
        The goal node
    """

    for node in closed_nodes:
        if node.state != start_node.state and node.state != goal_node.state:
            int_map[node.x_pos][node.y_pos] = 0

def update_path_nodes(int_map, current_node):
    """Updates and integer map with the path from start to goal

    Parameters
    ----------
    int_map : [[int]]
        The integer map
    current_node : Node
        The current node when a solution is found by astar
    """

    while current_node.parent:
        if current_node.parent.parent: # If not start node
            int_map[current_node.parent.x_pos][current_node.parent.y_pos] = -4 # Value used by visualizer
        current_node = current_node.parent

def execute_task(task_number, saved = False):
    """Executes one of the tasks in the assignment by TDT4136@NTNU

    Parameters
    ----------
    task_number : int
        The task number to be executed
    save : boolean, optional
        Set this to True if you want to save .png files of the visualizing
        for the path finding. Files are saved in the same directory as this file
    """

    map_obj = Map_Obj(task=task_number)
    start_node = Node(map_obj.get_start_pos(), map_obj.get_cell_value(map_obj.get_start_pos()))
    goal_node = Node(map_obj.get_goal_pos(), map_obj.get_cell_value(map_obj.get_goal_pos()))

    closed, current = astar(start_node, goal_node, map_obj)

    int_map = get_int_map(map_obj)
    draw_map(int_map, saved, f"task{task_number}-1.png") # Draw initial map
    update_start_goal(int_map, start_node, goal_node)
    draw_map(int_map, saved, f"task{task_number}-2.png") # Draw map with start and goal marked
    update_closed_nodes(int_map, closed, start_node, goal_node)
    draw_map(int_map, saved, f"task{task_number}-3.png") # Draw map with closed nodes marked
    update_path_nodes(int_map, current)
    draw_map(int_map, saved, f"task{task_number}-4.png") # Draw map with path nodes marked

execute_task(1)
execute_task(2)
execute_task(3)
execute_task(4)
