import gym
import util
import copy
from Node import Node
from search import graphSearch
import time
import constants
import sys
import globales

param = 'image'
#env = gym.make('SpaceInvaders-v0')
env = gym.make('MsPacman-ram-v0')
env._obs_type = param
env.reset()
cnt = 0
actions = []
env.frameskip = constants.FRAMESKIP
first_state = env.ale.cloneState()
for i in range(constants.CYCLES):
    globales.init()
    partialState = env.ale.cloneState()
    acts = graphSearch(env, util.Queue(), mode=param)
    env.ale.restoreState(partialState)
    actions += acts
    done = False
    tmp = False
    for act in acts:
        obs, rew, done, info = env.step(act)
        if done:
            break
    print "Acciones en el ciclo %s son: %s" % (str(i), str(acts))
    if done:
        print "FIN DE CICLO, QUE HA PASADO?"
        break


env.reset()
env.ale.restoreState(first_state)
env.frameskip = constants.FRAMESKIP
print actions
for act in actions:
    obs, rew, done, info = env.step(act)
    env.render()
    time.sleep(2)
    if done:
        print "FIN DE CICLO, QUE HA PASADO?"
        break
