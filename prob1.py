import numpy as np
from constants import *
from utils import *

class Clan:
    def __init__(self, x, y, p0):
        self.x = x
        self.y = y
        self._pop = p0
        
    def circle(self):
        return (self.r, self.x, self.y)
    
    def carrying(self):
        return carrying_capacity(t)

    @property
    def pop():
        return self._pop
    
    @property
    def r():
        return self.pop  ppl_supported_per_sq_km 
    
def generate_clan():
    return Clan(numpy.uniform(0, constants.d), 
                numpy.uniform(0, constants.d), 
                numpy.randint(min_start_pop, max_start_pop))
    
    
def discontent(clan):
    return clan.carrying() - clan.pop()


def conflict(clan1, clan2):
    return lambda_(clan1, clan2) * 1.0 / (discontent(clan1) * discontent(clan2))


def lambda_(clan1, clan2, func=intersecting_area):
    return func(clan1, clan2)


def lambda_ij(clans, i, j):
    return lambda_(clans[i], clans[j])