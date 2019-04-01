import numpy as np
import gym
from gym import spaces

#define constant value

queue_len=20
battle_level=40

distance_level=5
sensor_node=10
B=np.random.randint(1,battle_level,sensor_node)
D=np.random.randint(0,10,sensor_node)
H=np.random.randint(0,5,sensor_node)
data_prob=np.ones(sensor_node)*0.1
def funEh(distance):
    Eh=[5,5,4,4,3]
    return Eh[distance]

def funPh(distance):
    Ph=[1,1,2,2,3]
    return Ph[distance]    

def calculate_reward():
    return reward

def calculate_incbattery()
def calculate_trans_P():
    return 

#Sensor Node select Env
class nsEnv(gym.Env):
    def __init__(self,sensor_node):
        self.action_space = spaces.Discrete(sensor_node)
        self.observation_space = spaces.Tuple((((spaces.Discrete(battle_level+1),spaces.Discrete(queue_len+1)),)*sensor_node))
        

    def step(self,action):
        done=False
        reward=0.0
        #TO DO
    
        return 
    def _get_obs(self):

    def reset():

        return self._get_obs()

#switch EH or DT Env
class chEnv(gym.Env):
    def __init__(self):
        self.action_space = spaces.Discrete(2)
        self.observation_space=spaces.Tuple((spaces.Discrete(battle_level+1),spaces.Discrete(queue_len+1),spaces.Discrete(distance_level+1)))

    def step(self,action):
        done=False
        reward=0.0







        