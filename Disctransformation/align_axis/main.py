""""""
#####################################################################################
#   Copyright (C) 2016 Neelesh Soni <neeleshsoni03@gmail.com>, <neelrocks4@gmail.com>
#   
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#####################################################################################from numpy import log,exp,sqrt,mean,std,pi

from align_axis.parsepdb import parsepdb
from align_axis.getorientation import getorientation
from align_axis.makemove import move
import numpy as np

#N is normal vector passing through P
#let Tg be the vector st (Tg-P) is perpendicular to N
#DC's of (Tg-P) are (Tg-P)/np.sqrt(np.dot(Tg-P,Tg-P))
def get_arbitrary_perpendicular_vector(Ng,P):
	"""Summary
	
	Args:
	    Ng (TYPE): Description
	    P (TYPE): Description
	
	Returns:
	    TYPE: Description
	"""
	#arbitrary point (1,2,z)
	Tg = np.array([100.0,200.0,0.0])
	K=Ng[0]*P[0] + Ng[1]*P[1] + Ng[2]*P[2]
	Tg[2] = (K - Ng[0]*Tg[0] - Ng[1]*Tg[1])/(Ng[2]);
	Tf=Tg-P

	return Tf

def alignx(N, T, B):
	"""Summary
	
	Args:
	    N (TYPE): Description
	    T (TYPE): Description
	    B (TYPE): Description
	
	Returns:
	    TYPE: Description
	"""
	#Align chain on +x axis -ive to +ive
	OM = np.transpose(np.matrix( ( N, T, B) ))
	return OM

def aligny(N, T, B):
	"""Summary
	
	Args:
	    N (TYPE): Description
	    T (TYPE): Description
	    B (TYPE): Description
	
	Returns:
	    TYPE: Description
	"""
	#Align chain on +y axis -ive to +ive
	OM = np.transpose(np.matrix( ( B, N, T) ))
	return OM

def alignz(N, T, B):
	"""Summary
	
	Args:
	    N (TYPE): Description
	    T (TYPE): Description
	    B (TYPE): Description
	
	Returns:
	    TYPE: Description
	"""
	#Align chain on +z axis -ive to +ive
	OM = np.transpose(np.matrix( ( T, B, N) ))
	return OM
   
def align(inputfile, outputfile, alignaxis, chain):
	"""Summary
	
	Args:
	    inputfile (TYPE): Description
	    outputfile (TYPE): Description
	    alignaxis (TYPE): Description
	    chain (TYPE): Description
	
	Returns:
	    TYPE: Description
	"""
	#Parse the pdb file(fname) and returns the coordinates\
	# of CA of Two chains A and B and coordinates of CA atoms of LYS
	#It also returns the instance of pdb_class
	
	#mdl,coord_A,coord_All=parsepdb( inputfile, ['A','B'] );
	mdl,coord_A,coord_A_iter = parsepdb( inputfile, chain );
	
	#Get the axis of rotation of dimers A and B. Axis is \
	#defined by vector pvA/pvB and initial point pA/pB
	pvA,pA=getorientation(coord_A);
	
	axisA=[pvA,pA];
	N=pvA;
	
	T=get_arbitrary_perpendicular_vector(N,pA);

	B=np.cross(T,N);
	
	#Normalize all vectors
	N = N/np.sqrt(np.dot(N,N));
	T = T/np.sqrt(np.dot(T,T));
	B = -1*(B/np.sqrt(np.dot(B,B)));
	
	AlignDict={'x':alignx,'y':aligny,'z':alignz}

	OM = AlignDict[alignaxis](N,T,B)

	#print ("Vector and Position:\n",pvA,pA)
	#print ("Local Orthogonal matrix:\n",OM)
	
	#print("Checking IF the Orthogoal matrix is orthogonal by using dot product")
	#print (np.dot(T,B),np.dot(B,N),np.dot(T,N))
	
	#Convert the local transformation into the actual transformation
	mdl = move(mdl, OM);

	mdl.write(outputfile)

	return mdl, coord_A_iter
	


if __name__ == '__main__':

	import sys

	inputfile, outputfile, alignaxis = sys.argv[1], sys.argv[2], sys.argv[3]
	chain = ['ALL']
	align(inputfile, outputfile, alignaxis, chain)


