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


'''
 * @author Neelesh Soni
 * This is the main class for DISC TRANSFORMATION.
 * 
 '''
class DiscTransformation:

	"""Summary
	"""
	
	def __init__(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		self.__clash_score=0;
		self.__model_score=0;
		self.__model_mean=[]
		self.__radial_density=[]
		self.__max_dist=0

		return
	
	def main(self,args,InteractingSites=[[],[],[],[None,None]]):
		"""Summary
		
		Args:
		    args (TYPE): Description
		    InteractingSites (list, optional): Description
		
		Returns:
		    TYPE: Description
		"""
		from core.Build_Disc_Model import Build_Disc_Model
		from core.disc_state import disc_state
		from core.Score_Model import Score_Model
		from core.cluster import cluster_models
		
			
		#Setup Disc model environment variables through constructor
		bdm=Build_Disc_Model(args);

		if len(InteractingSites[0])!=0:
			bdm.Translate_Interacting_Sites(InteractingSites)
		
		#Build disc models
		discs=bdm.build_disc();
		
		#Get the disc state object
		ds=disc_state(bdm,discs);

		#Score the models
		score_obj=Score_Model(bdm,ds,discs);

		#Clash finding function
		#score_obj.clash_finding_function_all_vs_all(bdm);

		"""
		#To use this option provide electronic density file
		MODEL_atomic_density,mean_coord=score_obj.get_electronic_density(bdm,discs,args);
		
		print("@",score_obj.model_mean()[0],score_obj.model_mean()[1])
		for ad in MODEL_atomic_density:
			print(ad[0],ad[1])
		"""	
		

		#score_obj.calculate_accessibility(bdm)

		#print args[2].split('/')[-1], len(score_obj.get_accessibility())
		#print len(score_obj.get_accessibility())

		#print score_obj.get_accessibility()

		
		'''ADDED FOR PRINTING'''
		#Score the models
		#score_obj=Score_Model(bdm,ds,discs);
		
		#Write the text output file of the model  
		#bdm.write_output_file(discs,score_obj);
		
		#if score_obj.clash_score()!=0:
		#if score_obj.clash_score()>3:
		#	return discs,bdm

		#if score_obj.tetramer_score()>130:
		#	return discs,bdm
			
		#if score_obj.max_dist() >130:
		#	return discs,bdm
			
		#Check whether to print the model graphically or not
		#if bdm.get_model()=='yes':
		#	self.print_model(discs,bdm);

		'''ADDED FOR PRINTING'''
		#self.print_model(discs,bdm,score_obj);

		'''ADDED FOR PRINTING'''
		return discs,bdm,score_obj

	def print_model(self,discs,bdm,score_obj):
		"""Summary
		
		Args:
		    discs (TYPE): Description
		    bdm (TYPE): Description
		    score_obj (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		from core.Print_Disc_Model import Print_Disc_Model

		#Setup environment variables for graphics frame through constructor
		pdm=Print_Disc_Model(discs,bdm);
		
		#Write ps output
		pdm.printdata(discs,bdm.get_outfile(),score_obj);
		return

	def clash_score(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__clash_score;

	def model_score(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__model_score;

	def model_mean(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__model_mean

	def radial_density(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__radial_density

	def max_dist(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__max_dist


if __name__ == '__main__':
	
	'''ADDED FOR PRINTING'''
	import sys
	mdl=DiscTransformation()
	mdl.main(sys.argv)

	#OR
	#mdl.main(['',0,'./input/sample_input_2.txt'])



