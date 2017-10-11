# Importing libraries and functions
import matplotlib.pyplot as plt
import random as rand
import math
import numpy
from particles_setting import particles_setting
from Maps import Arena_maps
from matplotlib.path import Path
import matplotlib.patches as patches
from Measurement import Measure_Dist


# Initial user settings
Num_Part = input("Enter the number of particles to be used in the localisation:")
Num_Measurement = input("Enter the number of uniformly distributed measurements to be taken:") 
Num_Map = input("Enter the desired arena number (only 1 can be selected atm):")

# Creating the Robot and particles in the arena/ ************************** /
Selected_Map_X,Selected_Map_Y,Selected_Map_vertex,path,patch = Arena_maps(Num_Map)
X_rob,Y_rob,X_dir,Y_dir, Alpha_robot = particles_setting(path,Selected_Map_X,Selected_Map_Y,1)
X_particles, Y_particles, X_par_dir, Y_par_dir, Alpha_particles = particles_setting(path,Selected_Map_X,Selected_Map_Y,Num_Part)
Robot_Distances = Measure_Dist(Alpha_robot,Num_Measurement)


# Taking measurements



# Plots / ************************* /
fig = plt.figure()
ax = fig.add_subplot(111)
ax.add_patch(patch)
plt.plot([X_rob,X_dir],[Y_rob,Y_dir],'r',linewidth=2.0)
plt.plot(X_rob,Y_rob,'ro', markersize=4.0)
plt.plot(X_particles,Y_particles,'bo',markersize=4.0)
plt.plot([X_particles,X_par_dir],[Y_particles,Y_par_dir],'b',linewidth=2.0)
plt.show()
