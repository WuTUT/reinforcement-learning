import numpy as np
import gym
from gym import spaces

#define constant value
dtheta=0.5
k1=0.2
k2=3
modulation_level=5
queue_len=6
battle_level=5
packet_payload=256
ber_requirement=0.0005
T_len=5
data_arrival_p=
def calculate_reward():
    return reward
def calculate_modulationK():
    return modulationK
def calculate_incbattery(modulationK)
def calculate_trans_P(idnode,modulationK,):
    return 

class WrsnEnv(gym.Env):
    def __init__(self,sensor_node=40):
        self.action_space = spaces.Discrete(sensor_node)
        self.observation_space = spaces.Tuple((((spaces.Discrete(battle_level),spaces.Discrete(queue_len+1)),)*sensor_node))
    def step(self,action):
        done=False
        reward=0.0
        #TO DO

        return 
    def _get_obs(self):

    def reset():

        return self._get_obs()



        