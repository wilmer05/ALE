import copy
import time
import constants
import HyperNode
import globales

class RGBState():
    def __init__(self, ale_state=None, features=None):
        self.ale_state = ale_state
        self.features = features
        self.best_reward_below = float("-inf")
        self.reward = 0
        self.terminal = False

    def __eq__(self, other):
        return self.features == other.features
    
    def __hash__(self):
        return hash(str(self.process_screen()))

    def process_screen(self):
        return self.features

    def set_features(self, rgb):
        features = []
        for x in range(0,len(rgb)):
            for y in range(0, len(rgb[0])):
                features.append((x,y,rgb[x][y][0], rgb[x][y][1], rgb[x][y][2]))
        self.features = features

    def get_successor_states(self, env):
        "Return a list of nodes reachable from this node. [Fig. 3.8]"
        nexts = []
        for act in range(0, constants.NUMBER_OF_ACTIONS):
            n = RGBState()
            env.ale.restoreState(self.ale_state)
            screen, reward, terminal, info = env.step(act)
            n.set_features(screen)
            n.ale_state = env.ale.cloneState()
            n.reward = self.reward + reward
            if type(n.reward) is list:
                n.reward += max(n.reward)
            else:
                n.reward += reward
            n.best_reward_below = n.reward
            n.terminal = terminal
            nexts.append((act, n))
        return nexts
