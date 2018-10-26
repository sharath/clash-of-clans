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
        self._history = defaultdict(lambda : [])
        self._world = world
        self.dead = False
        self.W = 0
        
    
    def step(self, dt=0.01):
        self.__monitor()
        if self.p <= 0:
            self.dead = True
            self.p = 0
            self.radius = 0
            self.s = 0
            
            
        if not self.dead:
            dp = (r(self.s)*self.p*(1.0 - (self.p/self.K)) - self.W**3)*dt 
        
            self.p = max(self._history['p'][-1] + dp, 0)
            self.delta = self._history['K'][-1] - self._history['p'][-1]
            self.radius = np.sqrt(self._history['p'][-1]/(np.pi*pop_density))
            self.s = max(min((self._history['s'][-1]*self._history['p'][-1] + 0.5*dp)/(self._history['p'][-1] + dp), 1), 0)
            
            self.W = np.sum([self.alpha_(w) for w in self.world])
    
    def __monitor(self):
        for k, v in vars(self).items():
            if '_' != k:
                self._history[k].append(v)

    @property
    def history(self):
        return self._history
    
    @property
    def world(self):
        return self._world
    
    def lambda_(self, clan):
        return intersecting_area(self, clan)
    
    def alpha_(self, clan):
        return (self.lambda_(clan)*(self.delta))/(clan.delta)
    

__world = []
def generate_clan():
    c = Clan(np.random.uniform(0, d),
             np.random.uniform(0, d),
             np.random.randint(min_start_pop, max_start_pop), list(__world), s0=s_0)
    
    for j in __world:
        j.world.append(c)
    __world.append(c)
    return c

