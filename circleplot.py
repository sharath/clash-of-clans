import numpy as np
from clan import Clan, generate_clan
from constants import *
import seaborn as sns
import matplotlib.pyplot as plt

n = 5 # Number of clans
color_list = ['blue', 'green', 'red', 'royalblue','honeydew','yellow','brown','maroon','aqua','indigo']
clans = [generate_clan() for i in range(n)]
x_cor = []
y_cor = []
rad = []

for c in clans:
	x_cor.append(c.x)
	y_cor.append(c.y)
	rad.append(c.radius)

#for i in range(0,n):
	#circles = [plt.Circle((x_cor[i], y_cor[i]), rad[i], clip_on=False)]

steps = 7000
dt = 700/steps
x = np.linspace(0, 700, steps)

for t in range(0,steps):
	rad = []
	circles = []
	for c in clans:
		c.step(dt)

	for c in clans:
		rad.append(c.radius)

	for j in range(0,n):
		circle_add = plt.Circle((x_cor[j], y_cor[j]), rad[j],color=color_list[j])
		circles.append(circle_add)

	plt.style.use('seaborn-white')
	plt.gcf().set_size_inches(15, 10)
	sns.despine()
	plt.ion()
	plt.xlabel('x coordinate')
	plt.ylabel('y coordinate')
	plt.plot(x_cor, y_cor,'ro')

	for j in range(0,n):
		plt.subplot().add_artist(circles[j])
	#plt.delaxes()
	plt.legend()
	plt.pause(0.000000001)
	for i in range(0,n):
		print('radius ', i, ' = ' , rad[i])
	plt.delaxes()

plt.show()