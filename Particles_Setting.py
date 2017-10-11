# Importing libraries and functions
import random as rand
import math
import numpy
from matplotlib.path import Path
import matplotlib.patches as patches

# This function returns x,y coordinates of particles as well as their orientation angle and another set of x,y points inorder to illustrate their orientations in plotting
def particles_setting(path,Selected_Map_X,Selected_Map_Y,Num_Part):
	Num_Part =int(Num_Part)
	X_particles = []
	Y_particles = []
	Alpha_particles=[]
	D_par_dir = 0.2 
	X_par_dir = []
	Y_par_dir = []
	x=0

	while x <Num_Part: 
		i = rand.uniform(min(Selected_Map_X),max(Selected_Map_X))
		j = rand.uniform(min(Selected_Map_Y),max(Selected_Map_Y))
		ang = rand.uniform(0,1)*2*math.pi
		inside = path.contains_points([(i,j)])
		if inside[0]==True:	
			X_particles.append(i)
			Y_particles.append(j)
			Alpha_particles.append(ang)
			X_par_dir.append(i + D_par_dir*math.cos(ang))
			Y_par_dir.append(j + D_par_dir*math.sin(ang))
			x +=1
	return X_particles, Y_particles, X_par_dir, Y_par_dir, Alpha_particles