import util
import copy
from Node import Node
import constants
import sys
import RGBNode
def graphSearch(root_env, fringe, lookahead_size = constants.LOOKAHEAD_SIZE, max_depth = constants.MAX_DEPTH_SIZE, mode = "ram"):
    """Search through the successors of a problem to find a goal.
    The argument fringe should be an empty queue. [Fig. 3.18]"""
   
    if mode == "ram": 
        rootNode = Node(root_env, ale_state=root_env.ale.cloneState())
    else: 
        rootNode = RGBNode(root_env, ale_state=root_env.ale.cloneState())
    rootNode.env.frameskip = constants.FRAMESKIP
    fringe.push(rootNode)
    #try:
    #    rootNode.__hash__()
    #    visited = set()
    #except:
    #    visited = list()
    visited = set()
    total_expanded = 0
    best_node = None
    while not fringe.isEmpty() and total_expanded < lookahead_size:
        node = fringe.pop()
        #print node
        if node.isTerminal() or node.depth == max_depth:
            continue

        n = node.expand()
        visited.add(n)
        best_node = n if ((best_node and n and best_node.reward <= n.reward) or (best_node is None)) else best_node

        total_expanded += 1
        
        for nextnode in node.children:
            #nextnode.back_propagate_reward()
            if nextnode not in visited:
                fringe.push(nextnode)

    return best_node.path()
