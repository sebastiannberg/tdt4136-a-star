class Node:
    """Nodes are created from cells in the map provided by tdt4136 via Map.py and csv files."""

    def __init__(self, position, value, parent = None, kids = [], g = None, h = None, f = None):
        """
        Parameters
        ----------
        position : (int, int)
            A tuple describing the node's position
        value : int
            The value (cost) of traversing this node
        parent : Node, optional
            The parent-node of this node
        kids: [Node], optional
            A list containing the kids to this node in the search tree
        g: int, optional
            This node's g value
        h: int, optional
            This node's h value
        f: int, optional
            This node's f value
        """

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


def generate_successors(node, map_obj):
    """Generates successor-nodes to a given node

    Parameters
    ----------
    node : Node
        The node to generate successor-nodes from
    map_obj : Map_Obj
        An object that is used to find the values
        of specific positions on a map

    Returns
    -------
    list
        A list of all the successor-nodes
    """

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

def attach_and_eval(child, parent, goal_node):
    """Helper function for astar, updating parent and computing f value

    Parameters
    ----------
    child : Node
        The child node that is being attached to parent
    parent : Node
        The node that is being set as parent node to child
    goal_node: Node
        The node that is set as goal_node in current
        iteration of astar
    """

    child.parent = parent
    child.g = parent.g + child.value
    child.h = heuristic(child, goal_node)
    child.f = child.g + child.h

def propagate_path_improvements(parent):
    """Helper function for astar, ensure all nodes in search graph always aware of the
    current best parent and g value

    Parameters
    ----------
    parent : Node
        The node that is being propagated
    """

    for child in parent.kids:
        if parent.g + child.value < child.g:
            child.parent = parent
            child.g = parent.g + child.value
            child.f = child.g + child.h
            propagate_path_improvements(child)

def heuristic(node, goal_node):
    """Heuristic function (manhattan distance + admissable)

    Parameters
    ----------
    node : Node
        The node that is computing h value
    goal_node : Node
        The goal node in current iteration of astar
    """

    return abs(node.x_pos - goal_node.x_pos) + abs(node.y_pos - goal_node.y_pos)

def astar(start_node, goal_node, map_obj):
    """Implementation of A* algorithm

    Parameters
    ----------
    start_node : Node
        The starting node
    goal_node: Node
        The goal node
    map_obj : Map_Obj
        An object that is used to find the values
        of specific positions on a map

    Returns
    -------
    string
        A string if the algorithm fails at finding a solution
    ([Node], Node)
        A tuple consisting of a list of all closed nodes and the
        current node when finding a solution
    """

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
