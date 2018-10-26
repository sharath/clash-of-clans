import numpy as np
np.random.seed(1)

d = 100 # size of square in km
n = 2 # number of clans
s_0 = 17.0/18.0 # initial % female
pop_density = 10 # number of people supported by a square kilometer of land (look for source)
total_k = d**2 * pop_density
max_start_pop = total_k/50
min_start_pop = total_k/1000
hostility = 3
g = 0.5