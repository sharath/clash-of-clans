import numpy as np
from collections import defaultdict
from constants import *
from utils import *

r = lambda s : -1 * s**3 * np.log(s) # rate of growth


class Clan:
    def __init__(self, x, y, p0, world, s0):
        self.x = x
        self.y = y
        self.s = s0
        self.m = (1-s0) * p0
        self.f = s0 * p0
        self.K = total_k
        
        self.delta = self.K - self.p
        
        self.radius = np.sqrt(self.p / (np.pi*pop_density))
        self._history = defaultdict(lambda : [])
        self._world = world
        self.dead = False
        self.W = 0
        
        self.__keys = ['x', 'y', 'radius', 'm', 'f', 'dead', 'W', 's', 'K']
        
    
    def step(self, dt=0.01):
        self.__monitor()
        
        # values for the last time step
        s = self.last('s')
        p = self.last('m')+self.last('f')
        K = self.last('K')
        W = self.last('W')
        
        self.m += 0.5*r(s)*p*(1-(p/K)) - g*np.sum(W)
        self.f += 0.5*r(s)*p*(1-(p/K)) - (1-g)*np.sum(W)
        
        self.delta = K - p
        self.radius = np.sqrt(p/(np.pi*pop_density))
        
        self.W = np.sum([self.alpha_(w) for w in self.world])
        
        self.s = min(max(self.f / self.p, 0), 1)
    
    def __monitor(self):
        for k in self.__keys:
            self._history[k].append(vars(self)[k])

    @property
    def p(self):
        return self.m + self.f
                
    @property
    def history(self):
        return self._history
    
    @property
    def world(self):
        return self._world
    
    def last(self, key):
        return self._history[key][-1]
    
    def lambda_(self, clan):
        return intersecting_area(self, clan)
    
    def alpha_(self, clan):
        return (self.lambda_(clan)/np.log(clan.delta * self.delta))**hostility
    

__world = []
def generate_clan():
    c = Clan(np.random.uniform(0, d),
             np.random.uniform(0, d),
             np.random.randint(min_start_pop, max_start_pop), list(__world), s0=s_0)
    
    for j in __world:
        j.world.append(c)
    __world.append(c)
    return c

