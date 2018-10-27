import numpy as np
np.random.seed(1)

d = 100 # size of square in km
s_0 = 0.5 # initial % female
pop_density = 1 # number of people supported by a square kilometer of land (look for source)
total_k = d**2 * pop_density
max_start_pop = 250
min_start_pop = 50
hostility = 10

natural_death = 0.1
g = 0.9