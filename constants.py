import numpy as np
np.random.seed(1)

d = 100 # size of square in km
s_0 = 0.5 # initial % female (given by problem)
pop_density = 5 # number of people supported by a square kilometer of land (look for source)
total_k = d**2 * pop_density
max_start_pop = 100
min_start_pop = 50
hostility = 3
#hostility = 3.4

natural_death = 0.7
g = 0.85