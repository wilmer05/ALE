import gym
import util
import copy
from Node import Node
from search import graphSearch
import time
import constants

#env = gym.make('SpaceInvaders-v0')
env = gym.make('MsPacman-ram-v0')
env.reset()
cnt = 0
actions = []
env.frameskip = constants.FRAMESKIP
for i in range(constants.CYCLES):
    acts = graphSearch(env, util.Stack())
    actions += acts
    done = False
    for act in acts:
        obs, rew, done, info = env.step(act)

        if done:
            break
    print "Acciones en el ciclo %s son: %s" % (str(i), str(acts))
    if done:
        print "FIN DE CICLO, QUE HA PASADO?"
        break


env.reset()
print actions
for act in actions:
    obs, rew, done, info = env.step(act)
    env.render()
    time.sleep(2)
    if done:
        print "FIN DE CICLO, QUE HA PASADO?"
        break