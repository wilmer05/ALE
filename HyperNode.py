import copy
import time
import constants

def aplicable_actions(space):

    return [ [('KeyEvent', 'Z', True)], [('KeyEvent', 'ArrowRight', True)], [('KeyEvent', 'ArrowLeft', True)], [('KeyEvent', 'ArrowUp', True)], [('KeyEvent', 'ArrowDown', True)],  []]

class HyperNode:
    """AIMA: A node in a search tree. Contains a pointer
    to the parent (the node that this is a successor of)
    and to the actual state for this node. Note that if
    a state is arrived at by two paths, then there are
    two nodes with the same state.  Also includes the
    action that got us to this state, and the total
    path_cost (also known as g) to reach the node.
    Other functions may add an f and h value; see
    best_first_graph_search and astar_search for an
    explanation of how the f and h values are handled.
    You will not need to subclass this class."""

    def __init__(self, env, state=None, parent=None, action=None, ale_state=None, content = None):
        "Create a search tree Node, derived from a parent by an action."
        self.env = env
        self.state = state
        self.parent = parent
        self.children = []
        self.action = action
        self.terminal = False
        self.best_reward_below = float("-inf")
        self.best_action = None
        self.ale_state = ale_state
        self.content = content

        if parent:
            self.depth = parent.depth + 1
            self.size_subtree = 0
            self.reward = parent.reward
            #self.accumulated_reward = parent.accumulated_reward + reward
        else:
            self.depth = 0
            self.size_subtree = 0
            self.reward = 0
            #self.accumulated_reward = reward


    def __repr__(self):
        return "<Node %s>" % (self.env,)

    def isTerminal(self):
        return self.terminal

    def nodePath(self):
        "Create a list of nodes from the root to this node."
        x, result = self, [self]
        while x.parent:
            result.append(x.parent)
            x = x.parent
        result.reverse()
        return result

    def path(self):
      """
      Create a path of actions from the start to the current state
      """
      actions = []
      currnode = self
      while currnode.parent:
        actions.append(currnode.action)
        currnode = currnode.parent
      actions.reverse()
      return actions

    def back_propagate_reward(self):
        n = self
        while n.parent is not None:
            if n.parent.best_reward_below < n.reward:
                n.parent.best_reward_below = n.reward
                n.parent.best_action = n.action
            n = n.parent
            n.size_subtree += 1

    def expand(self):
        raise NotImplementedError
