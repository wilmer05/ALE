import time
import gym
import constants
from RGBState import RGBState
class MySearchModel(object):
    def __init__(self, searchspace):
        self.searchspace = searchspace
        self.env = gym.make('MsPacman-ram-v0')
        self.env._obs_type = 'image'
        self.env.reset()
        self.env.frameskip = constants.FRAMESKIP
        self.root = self.make_root_node()

    def init(self):
        self.env.reset()
        ale_state = self.env.ale.cloneState()
        screen = self.env._get_obs()

        state = RGBState(ale_state)
        state.set_features(screen)

        return state

    def is_goal(self, node):
        return node.state.reward > constants.GOAL_SCORE

    def get_successor_states(self, state):
        return state.get_successor_states(self.env)

    def make_root_node(self):
        return self.searchspace.make_root_node(self.init())

    def make_node(self, parent, action, state):
        return self.searchspace.make_child_node(parent, action, state)

    def show_env(self):
        self.env.render()
        time.sleep(2)
        self.env.render(close=True)
    
    def simulate_actions(self, actions):
        self.env.reset()
        for act in actions:
            print "\tAction: %s" % str(act)
            self.env.step(act)
            self.show_env()

    def successor_nodes(self, node):
       successors = []
       for action, state in self.get_successor_states(node.state):
           successors.append(self.searchspace.make_child_node(node, action, state))
       return successors

    def get_features(self, node):
        return node.state.features
