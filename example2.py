import universe
import gym
import util
import copy
from Node import Node
from search import graphSearch


# env = gym.make('CartPole-v0')
# env.reset()
# for _ in range(1000):
#     env.render()
#     env.step(env.action_space.sample())


#env = gym.make('SpaceInvaders-v0')
env = gym.make('MsPacman-ram-v0')
#env.configure(remotes=1)
env.reset()
env.render()
cnt = 0
#print type(enf)
#print env.get_keys_to_action()
for _ in range(10):
    cnt+=1
    #act = env.action_space.sample()
    act = graphSearch(env, util.Queue())
    print "################\nAction %s\n###########" % str(act)
    env.render()
    #act = env.step(('KeyEvent', 'Z', True))
    obs, rew, done, info = env.step([act]) # take a random action
    if done:
        print "FIN DE CICLO"
        env.reset()

