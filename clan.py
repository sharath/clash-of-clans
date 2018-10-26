import numpy as np
from constants import *
from utils import *

r = lambda s : -1 * s**3 * np.log(s) # rate of growth


class Clan:
    def __init__(self, x, y, p0, s0):
        self.x = x # x-coordinate
        self.y = y # y-coordinate
        self.p = p0 # initial population
        self.s = s0 # ratio female
        self.K = total_k # carrying capacity of grid / goal for clan
        self.delta = self.K - self.p # discontent
        self.r = np.sqrt(self.p/(np.pi*pop_density))
        
    
    def step(self, dt=0.01):
        dp = (self.r*(self.s)*self.p*(1.0 - (self.p/self.K)))*dt
        
        self.p += dp
        self.delta = self.K - self.p
        self.r = np.sqrt(self.p/(np.pi*pop_density))
        print(self.p)
        self.s = (self.s*self.p + 0.5*dp)/(self.p + dp)
    
    
    def lambda_(self, clan):
        return intersecting_area(self, clan)
    
    
    def conflict(self, clan):
        return self.lambda_(clan) / (self.delta * clan.delta)
    

def generate_clan():
    return Clan(np.random.uniform(0, d), 
                np.random.uniform(0, d), 
                np.random.randint(min_start_pop, max_start_pop), s0=s_0)

