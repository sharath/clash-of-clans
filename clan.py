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
        p = self.last('m') + self.last('f')
        K = self.last('K')
        W = self.last('W')
        
        dm = (0.5*r(s)*p*(1-(p/K)) - g*np.sum(W))*dt
        df = (0.5*r(s)*p*(1-(p/K)) - (1-g)*np.sum(W))*dt
            
        if self.m <= 0:
            self.m = 0
            dm = 0
            df = -1*(1-g)*np.sum(W)*dt
            
        if self.f <= 0:
            self.f = 0
            df = 0
            
        if self.f <= 0 and self.s <= 0:
            self.dead = True
            
        if self.dead:
            df = 0
            dm = 0
    
        self.m += dm
        self.f += df
        
        self.delta = K - p
        self.radius = np.sqrt(p/(np.pi*pop_density))
        
        self.W = np.sum([self.alpha_(w) for w in self.world])
        
        if self.p > 1e-15:
            self.s = self.f / self.p
        else:
            self.s = 0
    
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
__seed = 0
def generate_clan():
    global __seed
    np.random.seed(__seed)
    __seed += 1
    c = Clan(np.random.uniform(0, d),
             np.random.uniform(0, d),
             np.random.randint(min_start_pop, max_start_pop), list(__world), s0=s_0)
    
    for j in __world:
        j.world.append(c)
    __world.append(c)
    return c

