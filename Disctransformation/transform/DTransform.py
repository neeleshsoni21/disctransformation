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

from transform.pdbclass import PDB
import numpy as np
from align_axis.main import align

def DTransform(mdl):
	"""
	Takes a model object and performs Linear transformation suitable for Disctransformation
	
	Parameters
	----------
	mdl : pdbclass
		Model object to the file for Disctransform
	
	Returns
	-------
	mdl : pdbclass
		Modified model object after Disctransform
	"""

	ProjZ = np.array([[1,0,0],[0,1,0],[0,0,0]])

	DepZ = np.array([[0,0,0],[0,0,0],[0,0,1]])
	
	for i in range(0,mdl.iter_length()):

		#For identifying atoms at similar level along the z axis
		mdl.set_T(i,mdl.z()[i])

		#Non standard and fast way to get the projections
		mdl.set_z(i,0)

		"""
		#Apply transformation to only CA atoms
		if mdl.name()[i]=='CA' or mdl.name()[i]!='CA':

			#This is standard LA way to get the projection.
			value = np.matmul(ProjZ,np.array([ mdl.x()[i],mdl.y()[i],mdl.z()[i]]))
			mdl.set_x(i,value[0]) 
			mdl.set_y(i,value[1]) 
			mdl.set_z(i,value[2])
			
			#Non standard and fast way to get the projections
			mdl.set_z(i,0)
		"""

	return mdl

def sqrdistance(a1,a2):
	"""Summary
	
	Parameters
	----------
	a1 : TYPE
	    Description
	a2 : TYPE
	    Description
	
	Returns
	-------
	TYPE
	    Description
	"""
	sqrdist = (a1[0]-a2[0])**2 + (a1[1]-a2[1])**2 + (a1[2]-a2[2])**2
	return sqrdist


def GetDiscRepresentation(mdl):
	"""
	Takes a model object and adds a pseudoatom for every CA atom. 
	This atom will be CA atom with Residue DTA. This can be used for 
	the visualization in pdb format
	
	Parameters
	----------
	mdl : pdbclass
		Model object of the file to add pseudoatom
	
	Returns
	-------
	mdl : pdbclass
		Modified model object after pseudoatom addition
	"""
	
	rescounter=-1; DiscAtoms=[]; tempcoords=[]; caca_dist_cutoff = 7.0;
	LastResNum = mdl.resSeq()[-1]

	#Iterate over every CA atom
	for i in range(0,mdl.iter_length()):

		if mdl.name()[i]=='CA':
			
			rescounter+=1
			
			#Skip for first CA atom
			if len(tempcoords)!=0:
				sdist_btx_pre_curr_CA_atom = sqrdistance(tempcoords[len(tempcoords)-1],[mdl.x()[i],mdl.y()[i],mdl.z()[i]])
			else:
				sdist_btx_pre_curr_CA_atom = 0
			
			#Every 4th CA atom
			if ((rescounter+1)%nthCA==0) or (sdist_btx_pre_curr_CA_atom > caca_dist_cutoff**2):

				tempcoords=np.array(tempcoords)
				
				avgcoord = np.mean(tempcoords,axis=0)
				
				DiscAtoms.append(avgcoord)
				
				#Get atom properties
				serial=mdl.iter_length()+len(DiscAtoms);
				name='CA'
				resName='DTA'
				chainID=mdl.chainID()[i]
				resSeq=1000+LastResNum+len(DiscAtoms);
				x=avgcoord[0];y=avgcoord[1];z=avgcoord[2]
				T=mdl.T()[i]
				
				mdl.add_atom_in_model(serial,name,resName,chainID,resSeq,x,y,z,T)

				tempcoords=[];rescounter=-1
				tempcoords.append([mdl.x()[i],mdl.y()[i],mdl.z()[i]])
			else:

				tempcoords.append([mdl.x()[i],mdl.y()[i],mdl.z()[i]])
	
	#Add the last set of coordinates if present
	if len(tempcoords)!=0:
		
		tempcoords=np.array(tempcoords)
					
		avgcoord = np.mean(tempcoords,axis=0)
		DiscAtoms.append(avgcoord)
					
		#Get atom properties
		serial=mdl.iter_length()+len(DiscAtoms);
		name='CA'
		resName='DTA'
		chainID=mdl.chainID()[i]
		resSeq=mdl.aa_length()+len(DiscAtoms);
		x=avgcoord[0];y=avgcoord[1];z=avgcoord[2]
		T=mdl.T()[i]
		mdl.add_atom_in_model(serial,name,resName,chainID,resSeq,x,y,z,T)

	
	mdl.set_iter_length(mdl.iter_length()+len(DiscAtoms))
	
	return mdl

def GetDiscRepresentation_nthCA(mdl, nthCA=4):
	"""
	Takes a model object and adds a pseudoatom for every nth CA atom. 
	This atom will be CA atom with Residue DTA. This can be used for 
	the visualization in pdb format
	
	Parameters
	----------
	mdl : pdbclass
		Model object of the file to add pseudoatom
	nthCA : int, optional
	    Description
	
	Returns
	-------
	mdl : pdbclass
		Modified model object after pseudoatom addition
	"""
	
	rescounter=-1; DiscAtoms=[]; tempcoords=[]; caca_dist_cutoff = 7.0;
	LastResNum = mdl.resSeq()[-1]

	#Iterate over every CA atom
	for i in range(0,mdl.iter_length()):

		if mdl.name()[i]=='CA':
			
			rescounter+=1
			
			#Skip for first CA atom
			if len(tempcoords)!=0:
				sdist_btx_pre_curr_CA_atom = sqrdistance(tempcoords[len(tempcoords)-1],[mdl.x()[i],mdl.y()[i],mdl.z()[i]])
			else:
				sdist_btx_pre_curr_CA_atom = 0
			
			#Every 4th CA atom
			if ((rescounter+1)%nthCA==0) or (sdist_btx_pre_curr_CA_atom > caca_dist_cutoff**2):

				tempcoords.append([mdl.x()[i],mdl.y()[i],mdl.z()[i]])
				tempcoords=np.array(tempcoords)

				avgcoord = np.mean(tempcoords,axis=0)
				
				DiscAtoms.append(avgcoord)
				
				#Get atom properties
				serial=mdl.iter_length()+len(DiscAtoms);
				name='CA'
				resName='DTA'
				chainID=mdl.chainID()[i]
				resSeq=1000+LastResNum+len(DiscAtoms);
				x=avgcoord[0];y=avgcoord[1];z=avgcoord[2]
				T=mdl.T()[i]
				
				mdl.add_atom_in_model(serial,name,resName,chainID,resSeq,x,y,z,T)

				tempcoords=[];rescounter=-1
				
			else:

				tempcoords.append([mdl.x()[i],mdl.y()[i],mdl.z()[i]])
	
	#Add the last set of coordinates if present
	if len(tempcoords)!=0:
		
		tempcoords=np.array(tempcoords)
					
		avgcoord = np.mean(tempcoords,axis=0)
		DiscAtoms.append(avgcoord)
					
		#Get atom properties
		serial=mdl.iter_length()+len(DiscAtoms);
		name='CA'
		resName='DTA'
		chainID=mdl.chainID()[i]
		resSeq=mdl.aa_length()+len(DiscAtoms);
		x=avgcoord[0];y=avgcoord[1];z=avgcoord[2]
		T=mdl.T()[i]
		mdl.add_atom_in_model(serial,name,resName,chainID,resSeq,x,y,z,T)

	
	mdl.set_iter_length(mdl.iter_length()+len(DiscAtoms))
	
	return mdl

if __name__ == '__main__':
	
	import sys
	inputfile = sys.argv[1]
	outputfile = sys.argv[1][:-4]+'_z.pdb'
	alignaxis = 'z'
	chain=['ALL']

	mdl, __ = align(inputfile, outputfile, alignaxis, chain)
	
	
	#Get radius at each CA/every 7th residue. generate a pseudo atom at this for visualization
	#Get the center of every nth residue and get some radius around it to have a disc
	N=7 #Every 4th CA
	mdl = GetDiscRepresentation_nthCA(mdl,N)

	mdl = DTransform(mdl)
	
	mdl.write(sys.argv[1][:-4]+'_projz.pdb')

__author__ = "Neelesh Soni"