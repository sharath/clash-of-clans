import numpy as np
from collections import defaultdict
from constants import *
from utils import *

r = lambda s : -1 * s**3 * np.log(s) # rate of growth


class Clan:
    def __init__(self, x, y, p0, world, s0):
        self.x = x # x-coordinate
        self.y = y # y-coordinate
        self.p = p0 # initial population
        self.s = s0 # ratio female
        self.K = total_k # carrying capacity of grid / goal for clan
        self.delta = self.K - self.p # discontent
        self.radius = np.sqrt(self.p/(np.pi*pop_density))
        self.history = defaultdict(lambda : [])
        self.world = world
        
    
    def step(self, dt=0.01):
        self.__monitor()
        dp = (r(self.s)*self.p*(1.0 - (self.p/self.K)))*dt
        
        self.p += dp
        self.delta = self.K - self.p
        self.radius = np.sqrt(self.p/(np.pi*pop_density))
        self.s = (self.s*self.p + 0.5*dp)/(self.p + dp)
    
    def __monitor(self):
        for k, v in vars(self).items():
            if k != 'history':
                self.history[k].append(v)
    
    
    def lambda_(self, clan):
        return intersecting_area(self, clan)
    

world = []

def generate_clan():
    c = Clan(np.random.uniform(0, d),
             np.random.uniform(0, d),
             np.random.randint(min_start_pop, max_start_pop), world, s0=s_0)
    for j in world:
        j.world.append(c)
    return c

