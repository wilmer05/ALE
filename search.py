import util
import copy
from Node import Node
def graphSearch(root_env, fringe, lookahead_size = 10, max_depth = 10):
    """Search through the successors of a problem to find a goal.
    The argument fringe should be an empty queue. [Fig. 3.18]"""

    rootNode = Node(copy.deepcopy(root_env))
    fringe.push(rootNode)
    try:
        rootNode.__hash__()
        visited = set()
    except:
        visited = list()

    total_expanded = 0
    while not fringe.isEmpty() and total_expanded < lookahead_size:
        node = fringe.pop()
        if node.isTerminal() or node.depth == max_depth:
            continue

        node.expand()

        total_expanded += 1
        
        for nextnode in node.children:
            nextnode.back_propagate_reward()
            fringe.push(nextnode)

    best_action = None
    for n in rootNode.children:
        if n.best_reward_below == rootNode.best_reward_below:
            best_action = n.action

    return best_action