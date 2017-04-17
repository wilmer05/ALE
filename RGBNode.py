import copy
import time
import constants
import HyperNode
import globales
def aplicable_actions(space):

    return [ [('KeyEvent', 'Z', True)], [('KeyEvent', 'ArrowRight', True)], [('KeyEvent', 'ArrowLeft', True)], [('KeyEvent', 'ArrowUp', True)], [('KeyEvent', 'ArrowDown', True)],  []]

class RGBNode(HyperNode.HyperNode):
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

    def __init__(self, env, state=None, parent=None, action=None, ale_state=None, content=None):
        "Create a search tree Node, derived from a parent by an action."
        HyperNode.HyperNode.__init__(self, env, state, parent, action, ale_state, content)

    def __eq__(self, other):
        return self.process_screen() == other.process_screen()
    
    def __hash__(self):
        return hash(str(self.process_screen()))

    def process_screen(self):
        return self.content

    def set_content(self, rgb):
        features = []
        for x in range(0,len(rgb)):
            for y in range(0, len(rgb[0])):
                features.append((x,y,rgb[x][y][0], rgb[x][y][1], rgb[x][y][2]))
        self.content = features
                
    def get_novelty(self):
        new_features = []
        for feature in self.content:
            if feature not in globales.generated_tuples:
                new_features.append(feature)
        novelty = len(new_features)
        if novelty <= constants.MAX_NOVELTY:
            for feature in new_features:
                globales.generated_tuples.add(feature)
        return novelty
    
    def has_novelty_1(self):
        new_features = []
        for feature in self.content:
            if feature not in globales.generated_tuples:
                return True
        return False

    def add_new_features(self):
        for feature in self.content:
            globales.generated_tuples.add(feature)

    def expand(self):
        "Return a list of nodes reachable from this node. [Fig. 3.8]"
        best_child = None
        for act in range(0,constants.NUMBER_OF_ACTIONS):
            n = RGBNode(self.env, None, self, act, self.ale_state)
            n.env.ale.restoreState(self.ale_state)
            screen, reward, terminal, info = n.env.step(act)
            n.set_content(screen)
            n.ale_state = n.env.ale.cloneState()
            if type(n.reward) is list:
                n.reward += max(n.reward)
            else:
                n.reward += reward

            best_child = n if ((best_child and best_child.reward < n.reward) or (best_child is None)) else best_child

            n.best_reward_below = n.reward
            n.terminal = terminal
            self.children.append(n)
        return best_child
