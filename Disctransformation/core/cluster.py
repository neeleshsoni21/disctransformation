""""""
################################################################################
#   Copyright (C) 2016 Neelesh Soni <neeleshsoni03@gmail.com>, 
#   <neelesh.soni@alumni.iiserpune.ac.in>
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
################################################################################


def cluster_models(MODELS):
	"""Summary
	
	Args:
	    MODELS (TYPE): Description
	
	Returns:
	    TYPE: Description
	"""
	Similar_models=[];
	removed_indxs=[]

	for idx1 in range(0,len(MODELS)):

		for idx2 in range(idx1+1,len(MODELS)):

			discs1=MODELS[idx1][1]
			discs2=MODELS[idx2][1]

			#print len(discs1),len(discs2)

			#get_best_rmsd_tetramer(discs1[0:4],discs2[0:4])

			dist1=MODELS[idx1][3].distance_matrix()
			dist2=MODELS[idx2][3].distance_matrix()

			#self.clash_finding_function_all_vs_all(bdm);

			#for i in range(0,4):
			#	for j in range(i,4):
			#		print discs1[i].p(),discs2[j].p()
			sumdist1=get_sum_dist(dist1)
			sumdist2=get_sum_dist(dist2)

			if (sumdist1==sumdist2):
				removed_indxs.append(idx2)

	for idx in range(0,len(MODELS)):
		if idx not in removed_indxs:
			Similar_models.append(idx);

	#print len(Similar_models)
	
	return Similar_models

def get_sum_dist(distX):
	"""Summary
	
	Args:
	    distX (TYPE): Description
	
	Returns:
	    TYPE: Description
	"""
	sumXs=0;
	for k,v in distX.items():
		sumXs+=v
	
	return sumXs