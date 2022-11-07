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

'''
This function parse the PDB file and return the coordinates of all atoms

'''

import sys
from align_axis.pdbclass import PDB

def parsepdb(fname,chains):
	"""Summary
	
	Args:
	    fname (TYPE): Description
	    chains (TYPE): Description
	
	Returns:
	    TYPE: Description
	"""
	#calling the PDB module to parse the "fname" and load it in memory
	mdl = PDB(fname)

	#Error checking
	if mdl == None:
		print('ERROR: no such file:', fname)
		sys.exit()
	
	#Allocating variables for coordinates atoms of chain A and All
	coord_A = [ ]
	coord_A_iter = []
	#coord_All = [ ]
	
	#Extracting the coordinates of C alpha atoms where chainID is A & B
	
	if chains[0]=='ALL':
		#Add coordinates of all chains
		for i in range(0,mdl.iter_length()):
			#coord_All.append([mdl.x()[i], mdl.y()[i], mdl.z()[i]]);
			coord_A.append([mdl.x()[i], mdl.y()[i], mdl.z()[i]]);
			coord_A_iter.append(i)

	else:

		for i in range(0,mdl.iter_length()):
			#Add coordinates of all chains
			#coord_All.append([mdl.x()[i], mdl.y()[i], mdl.z()[i]]);
			
			#Add coordinates of given chains chains
			if (mdl.chainID()[i] in chains):
				coord_A.append([mdl.x()[i], mdl.y()[i], mdl.z()[i]]);
				coord_A_iter.append(i)

	#return (mdl,coord_A,coord_All)
	return (mdl,coord_A, coord_A_iter)
	
	
	
