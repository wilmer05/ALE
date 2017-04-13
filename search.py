import util
import copy
from Node import Node
import constants
import sys
from RGBNode import RGBNode


def graphSearch(root_env, fringe, lookahead_size = constants.LOOKAHEAD_SIZE, max_depth = constants.MAX_DEPTH_SIZE, mode = "ram"):
    """Search through the successors of a problem to find a goal.
    The argument fringe should be an empty queue. [Fig. 3.18]"""
   
    state = root_env._get_obs()
    if mode == "ram": 
        rootNode = Node(root_env, ale_state=root_env.ale.cloneState())
    else: 
        rootNode = RGBNode(root_env, ale_state=root_env.ale.cloneState())

    rootNode.env.frameskip = constants.FRAMESKIP
    rootNode.set_content(state)
    rootNode.add_new_features()

    visited = set()
    total_expanded = 0
    best_node = None
    fringe.push(rootNode)

    while not fringe.isEmpty() and total_expanded < lookahead_size:
        node = fringe.pop()
        if node.isTerminal() or node.depth == max_depth:
            continue
        n = node.expand()
        visited.add(node)
        best_node = n if ((best_node and n and best_node.reward <= n.reward) or (best_node is None)) else best_node

        total_expanded += 1
        for nextnode in node.children:
            novelty = nextnode.get_novelty()
            print novelty
            if nextnode not in visited and novelty <= constants.MAX_NOVELTY:
                fringe.push(nextnode)

    return best_node.path()
