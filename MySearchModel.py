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

    def init(self):
        self.env.reset()
        ale_state = self.env.ale.cloneState()
        screen = self.env._get_obs()

        state = RGBState(ale_state)
        state.set_features(screen)

        return state

    def is_goal(self, state):
        return state.reward > 70

    def successors(self, state):
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
