import gym
import constants
import RGBState
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
        return state.reward > 5

    def successors(self, state):
        return state.get_successor_states(self.env)

    def make_root_node(self):
        return self.searchspace.make_root_node(self.init())

    def make_node(self, parent, action, state):
        return self.searchspace.make_child_node(parent, action, state)

