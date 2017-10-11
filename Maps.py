# Importing libraries and functions
import math 
import numpy
from matplotlib.path import Path
import matplotlib.patches as patches

def Arena_maps(Num_Map):
	# Map number 1
	if float(Num_Map)==1:
		Selected_Map_X = [0,10,10,7,7,8,5,2,3,3,0,0]
		Selected_Map_Y = [0,0,5,5,7,7,9,7,7,5,5,0]
		Selected_Map_vertex = list(zip(Selected_Map_X,Selected_Map_Y))
		path = Path(Selected_Map_vertex)
		patch = patches.PathPatch(path, facecolor='none', lw=2)

	# Map number x can be added here as above
	
	return Selected_Map_X,Selected_Map_Y,Selected_Map_vertex,path,patch