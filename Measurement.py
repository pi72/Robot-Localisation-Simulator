import math
import numpy 
from shapely.geometry import LineString

def Measure_Dist(ang,Measure_Num,Selected_Map_vertex,longest_Dist,X_obj,Y_obj):
	Len_Selected_Map = len(Selected_Map_vertex)
	Ang_step = (2*math.pi)/float(Measure_Num)
	n=1
	Dist_Vector=[]
	X_vect=[]
	Y_vect=[]
	
	while n<=int(Measure_Num):
		X_dir=X_obj+longest_Dist*math.cos(ang)
		Y_dir=Y_obj+longest_Dist*math.sin(ang)
		Dist_perm =10000
		
		for i in range(0,Len_Selected_Map-1):
			Line1 = LineString([Selected_Map_vertex[i],Selected_Map_vertex[i+1]])
			Line2 = LineString([(X_obj,Y_obj),(X_dir,Y_dir)])
			cross = Line1.intersection(Line2)

			if hasattr(cross, 'x'):
				Dist_temp = math.sqrt((X_obj-cross.x)**2 + (Y_obj-cross.y)**2)
				
				if (Dist_temp<Dist_perm):
					Dist_perm=Dist_temp
					temp_X=cross.x
					temp_Y=cross.y					 
		
		X_vect.append(temp_X)
		Y_vect.append(temp_Y)
		Dist_Vector.append(Dist_perm)
		ang=ang+Ang_step
		n+=1	
	return Dist_Vector,X_vect,Y_vect