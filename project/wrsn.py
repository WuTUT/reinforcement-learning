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


def calculate_transprob(sensor_node,selected,switch=None):
    if selected==True:
        #BH
        if (switch!=0 and switch!=1):
            raise Exception("Invalid switch",switch)
        if switch==0:
            B[sensor_node]=min(B[sensor_node]+funEh(H[sensor_node]),battle_level)
        else:
            if funPh(H[sensor_node])<B[sensor_node]:
                B[sensor_node]=B[sensor_node]-funPh(H[sensor_node])
                D[sensor_node]=max(D[sensor_node]-1,0)
            D[sensor_node]=D[sensor_node]+1 if data_prob[sensor_node]>np.random.uniform(0,1) else D[sensor_node]
            if D[sensor_node]>queue_len:
                D[sensor_node]=queue_len
                data_overflow=-1
            else:
                data_overflow=0
   
    else:
        D[sensor_node]=D[sensor_node]+1 if data_prob[sensor_node]>np.random.uniform(0,1) else D[sensor_node]
        if D[sensor_node]>queue_len:
            D[sensor_node]=queue_len
            data_overflow=-1
        else:
            data_overflow=0

    return data_overflow




#Sensor Node select Env
class nsEnv(gym.Env):
    def __init__(self,sensor_node):
        self.action_space = spaces.Discrete(sensor_node)

        self.lowstate=np.array([0,0,0])
        self.highstate=np.array([battle_level-1,queue_len-1,distance_level-1])

        self.observation_space = spaces.Box(low=self.lowstate,high=self.highstate,shape=(sensor_node,3))
        

    def step(self,action):
        done=False
        reward=0.0
        #TO DO
        for i in range(sensor_node):
            if i != action:
                reward += calculate_transprob(i,False)
        for i in range(sensor_node):
            if B[i]==0:
                done = True
                break
        


    
        return self._get_obs(),reward,done,{}
    def _get_obs(self):
        return 
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







        