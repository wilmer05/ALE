import universe
import gym
import util
import copy
from Node import Node
from search import graphSearch
import time

#env = gym.make('SpaceInvaders-v0')
env = gym.make('MsPacman-ram-v0')
env.reset()
cnt = 0
actions = []
for _ in range(10):
    act = graphSearch(env, util.Queue())
    actions.append(act)
    obs, rew, done, info = env.step([act]) # take a random action
    print obs
    if done:
        print "FIN DE CICLO, QUE HA PASADO?"
        env.reset()

env.reset()
for act in actions:
    obs, rew, done, info = env.step([act]) # take a random action
    env.render()
    if done:
        print "FIN DE CICLO, QUE HA PASADO?"
        break