import numpy as np
np.random.seed(1)

d = 100 # size of square in km
max_start_pop = 10000
min_start_pop = 500
n = 2 # number of clans
s_0 = 17.0/18.0 # initial % female
pop_density = np.random.randint(50, 200) # number of people supported by a square kilometer of land (look for source)
total_k = d**2 * pop_density
hostility = 3
g = 0.8