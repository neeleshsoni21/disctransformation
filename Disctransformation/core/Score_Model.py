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


from math import floor, exp, sqrt
from random import random
import sys
PI = 3.141592653

class Score_Model:

	"""Summary
	
	Attributes:
	    probe (int): Description
	"""
	
	def __init__(self,bdm,ds,d):
		"""Summary
		
		Args:
		    bdm (TYPE): Description
		    ds (TYPE): Description
		    d (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		self.__discs = d;
		self.__ds=ds;
		self.__shear_steps=5;
		self.__theta1_steps=10;
		self.__theta2_steps=10;
		
		self.__clash_score=None;
		self.__tetramer_score=None;
		self.__model_score=None;
		
		self.__model_mean=[-100000,-100000];
		
		self.__radial_density=[];
		self.__max_dist=None;

		self.__relax_min_dist=None;
		self.__Modes = []

		self.__distance_matrix={}

		self.__disc_clash_counter=[]
		for i in range(0,len(self.__discs)):
			self.__disc_clash_counter.append(0);

		self.__n_accessible_interacting_regions=[]

		self.probe=0

		self.__headtail_domain=[]

		self.__cc_score = {};
		self.__atomclash = {}
		self.__xlinkscore = []

		#self.__mode_positions=bdm.get_mode_positions()

		#THIS will be helpful if you have a constrained moves between the discs
		#self.read_allowed_states(self.__argsg[len(self.__argsg)-3]);
				
		#Use below if you need to find the clash between last disc added with all remaining self.__discs
		#self.__status=self.clash_finding_function_last_vs_all();
		
		#Following gives the compactness and clash scores
		#self.__status=self.compactness_finding_function_first_last_disc();
		#self.__status=self.clash_and_compactness_finding_function_for_last_disc();
		#self.__status=self.compactness_finding_function();

		#self.scoring_function(bdm,ds)

		#Use below if find you need to find the clash between all self.__discs
		#self.clash_finding_function_all_vs_all(bdm);
		#self.radial_dist_function();
		#self.Tetramer_min_dist_function();
		return

	def D3distance(self,coord1,coord2):
		"""Summary
		
		Args:
		    coord1 (TYPE): Description
		    coord2 (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		#calculate the euclidian distance between two self.__discs
		sdis= (coord2[0]-coord1[0])**2 + (coord2[1]-coord1[1])**2 + (coord2[2]-coord1[2])**2
		return sdis;

	def get_xlinkscore(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__xlinkscore
		
	def get_xlink_score(self, mdl, IterIdxs, discs, XlinkIdxs):
		"""Summary
		
		Args:
		    mdl (TYPE): Description
		    IterIdxs (TYPE): Description
		    discs (TYPE): Description
		    XlinkIdxs (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		for i in range(0,len(discs)):
			for j in range(i+1,len(discs)):

				Isites1 = discs[i].Get_InteractingSites()
				Isites2 = discs[j].Get_InteractingSites()

				Coords1 = list(zip(Isites1[0],Isites1[1]))
				Coords2 = list(zip(Isites2[0],Isites2[1]))

				ZCoords1 = Isites1[2]
				ZCoords2 = Isites2[2]

				for xidx in XlinkIdxs:

					p1 = Coords1[xidx]; p2 = Coords2[xidx];

					#dist = sqrt(self.sdistance(p1,p2))
					dist = sqrt(self.D3distance(p1+tuple([ZCoords1[xidx]]),p2+tuple([ZCoords2[xidx]])))

					#Check if xlink formed, else continue the loop
					if ((dist <=9.0) and (dist>=6.0)):
						self.__xlinkscore.append(xidx)
					else:
						continue
				
				#Do not heck for clases of xlink not found
				if self.__xlinkscore==0:
					continue

				for p1idx in range(0,len(Coords1)):
					for p2idx in range(p1idx,len(Coords2)):

						#if abs(ZCoords1[p1idx]-ZCoords2[p2idx]) > 1.0:
						#	continue

						p1 = Coords1[p1idx]; p2 = Coords2[p2idx];
						#dist = sqrt(self.sdistance(p1,p2))
						dist = sqrt(self.D3distance(p1+tuple([ZCoords1[p1idx]]),p2+tuple([ZCoords2[p2idx]])))

						resi1 = IterIdxs[p1idx]; resi2 = IterIdxs[p2idx]

						key1 = mdl.resSeq()[resi1],mdl.resName()[resi1],mdl.chainID()[resi1]
						key2 = mdl.resSeq()[resi2],mdl.resName()[resi2],mdl.chainID()[resi2]
						dist = round(dist,1)

						if dist < 3.0:
							self.__atomclash[tuple([key1,key2])]=dist
							continue
						#No CA-CA distance cutoff for Interaction
						elif (dist > 7):
							continue

						self.__cc_score[tuple([key1,key2])]=dist


		return

	def get_cc_pairing(self, mdl, IterIdxs, discs):
		"""Summary
		
		Args:
		    mdl (TYPE): Description
		    IterIdxs (TYPE): Description
		    discs (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		for i in range(0,len(discs)):
			for j in range(i+1,len(discs)):

				Isites1 = discs[i].Get_InteractingSites()
				Isites2 = discs[j].Get_InteractingSites()

				Coords1 = list(zip(Isites1[0],Isites1[1]))
				Coords2 = list(zip(Isites2[0],Isites2[1]))

				ZCoords1 = Isites1[2]
				ZCoords2 = Isites2[2]

				for p1idx in range(0,len(Coords1)):
					for p2idx in range(p1idx,len(Coords2)):

						#if abs(ZCoords1[p1idx]-ZCoords2[p2idx]) > 1.0:
						#	continue

						p1 = Coords1[p1idx]; p2 = Coords2[p2idx];
						#dist = sqrt(self.sdistance(p1,p2))
						dist = sqrt(self.D3distance(p1+tuple([ZCoords1[p1idx]]),p2+tuple([ZCoords2[p2idx]])))

						#No CA-CA distance cutoff for Interaction
						if (dist > 7):
							continue

						resi1 = IterIdxs[p1idx]; resi2 = IterIdxs[p2idx]

						key1 = mdl.resSeq()[resi1],mdl.resName()[resi1],mdl.chainID()[resi1]
						key2 = mdl.resSeq()[resi2],mdl.resName()[resi2],mdl.chainID()[resi2]
						dist = round(dist,1)

						if dist < 3.0:
							self.__atomclash[tuple([key1,key2])]=dist
							continue


						self.__cc_score[tuple([key1,key2])]=dist

		return

	def get_cc_score(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__cc_score

	def get_atomclash(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__atomclash

	def get_head_positions(self,bdm):
		"""Summary
		
		Args:
		    bdm (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		from numpy import cos, sin, array, cross, dot, arctan2
		
		drad=bdm.get_drad();
		modes=bdm.get_arguments()['@ARG5']
		d=bdm.get_discs();
		probe=18.0
		

		for i in range(0,len(d)):
			
			pif=PI/180.0
			xcord1=d[i].p();
			ycord1=d[i].q();
			#print xcord1
			mrad=drad+probe

			temp_list=[]
			buried_score=[]
			angle_list=[]

			for theta in range(0,360,10):
				angle_list.append(theta);
				p1 = [ xcord1+mrad*cos(theta*pif), ycord1+mrad*sin(theta*pif) ];
				
				#print p1;
				clash_score=0;
				for j in range(0,len(d)):
					xcord2=d[j].p();
					ycord2=d[j].q();

					dissqr=((xcord2-p1[0])*(xcord2-p1[0]) + (ycord2-p1[1])*(ycord2-p1[1]));
					
					if dissqr<mrad*mrad:
						#(dist - mrad)^2=dist^2 + mrad^2 -2*dist*mrad
						clash_score+= (sqrt(dissqr)-mrad)**2;
			
				buried_score.append(round(clash_score,2));

			idx=buried_score.index(min(buried_score));
			ang=angle_list[idx];
			p1 = [ xcord1+mrad*cos(ang*pif),  ycord1+mrad*sin(ang*pif) ];
			#print i,p1
			#Mean point of the head domain
			self.__headtail_domain.append(p1);

			#radius of head/tail domain is 20A by considering globular
			radius_of_head=probe
			headatoms=1858
			tailatoms=1027
			allnccatoms=headatoms+tailatoms
			
			for i in range(0,allnccatoms):
				r1=random()
				position=r1*radius_of_head 
				angle1=random()*2*3.14159
				coord1x=position*cos(angle1)+ p1[0]
				coord1y=position*sin(angle1)+ p1[1]
				self.__headtail_domain.append([coord1x,coord1y])

			"""#radius of head domain extending density
			#radius_of_head=probe
			headatoms=1858
			tailatoms=0
			allnccatoms=headatoms+tailatoms
			allnccdomain_ext=5.0

			for i in range(0,allnccatoms):
				r1=random()
				position=r1*allnccdomain_ext + drad
				angle1=random()*2*3.14159
				coord1x=position*cos(angle1)+ xcord1
				coord1y=position*sin(angle1)+ ycord1
				self.__headtail_domain.append([coord1x,coord1y])
			"""
			
		return

	def get_electronic_density(self,bdm,discs,args):
		"""Summary
		
		Args:
		    bdm (TYPE): Description
		    discs (TYPE): Description
		    args (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		try:

			fname=open(args[3],'r')
			lines=fname.readlines()
			fname.close()
		except:
			print("Provide Electronic Density File!")
			sys.exit()


		mean_coord=map(float,lines[0][1:].strip().split(' '))
		atomic_density=[]
		for l in lines[1:]:
			atomic_density.append( map(float,l.strip().split(' ')) )
			

		#print atomic_density
		MODEL_atomic_density=[]

		for d in discs:
			YA  = d.q() - mean_coord[1]  
			XA  = d.p() - mean_coord[0]
			NA  = sqrt(XA*XA + YA*YA)
			axis = [XA/NA, YA/NA]

			for ad in atomic_density:
				point=self.translatepoint(ad,NA,axis)
				MODEL_atomic_density.append(point)

		
		
		self.get_head_positions(bdm)

		#for p in self.__headtail_domain:
		#	MODEL_atomic_density.append(p);			

		return MODEL_atomic_density, mean_coord
	
	def calculate_accessibility(self,bdm):
		"""Summary
		
		Args:
		    bdm (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		drad = bdm.get_drad();
		probe= (drad/5.0)*4

		self.__probe=probe;

		bdm.set_mode_positions(probe)
		
		mode_positions = bdm.get_mode_positions()
			
		#print len(mode_positions),len(bdm.get_discs())
		for coord in mode_positions:
			
			#print coord
			buried = False
			
			for d in bdm.get_discs():
				r = drad + probe
				dsq = self.sdistance([d.p(),d.q()], coord)

				if dsq + 0.1 < r*r:
					buried = True
					break

			if buried==False:
				self.__n_accessible_interacting_regions.append(coord)

		return;

	#Calculate the minimum distance between tetramers for compactness
	def Tetramer_min_dist_function(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		self.__tetramer_score=1000000
		for i in range(0,4):
			for j in range(len(self.__discs)-4,len(self.__discs)):
				
				distance=self.__distance_matrix[tuple([i,j])]
				if distance < self.__tetramer_score:
					self.__tetramer_score=distance;
		
		self.__tetramer_score=round(self.__tetramer_score)

		return;

	#Calculate the distance of all discs from the model mean. This is used for getting the compactness in the structure
	def radial_dist_function(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		for i in range(0,len(self.__discs)):
			distance= sqrt((self.__model_mean[1]-self.__discs[i].q())*(self.__model_mean[1]-self.__discs[i].q()) + (self.__model_mean[0]-self.__discs[i].p())*(self.__model_mean[0]-self.__discs[i].p()));
			self.__radial_density.append(str(round(distance,1) ));
			if distance > self.__max_dist:
				self.__max_dist=distance;
				
		self.__max_dist=round(self.__max_dist,1)

		return;

	def Disc_clash_counter_function(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		max_clash_with_disc=0
		for num_clash in self.__disc_clash_counter:
			if max_clash_with_disc < num_clash:
				max_clash_with_disc=num_clash;
	
		return max_clash_with_disc

	#This module calculates the clashes between all discs and determines the model mean
	def clash_finding_function_all_vs_all(self,bdm):
		"""Summary
		
		Args:
		    bdm (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		tot_disc=len(self.__discs);
		
		relax_min_dist=float(bdm.get_mindist());
		sum_x=0;
		sum_y=0;
		mclash_score=0
		
		#print "Modeldist:",bdm.get_model_id();

		for i in range(0,tot_disc):
			sum_x+=self.__discs[i].p();
			sum_y+=self.__discs[i].q();

			for j in range(i+1,tot_disc):
				distance= sqrt( (self.__discs[j].q()-self.__discs[i].q())*(self.__discs[j].q()-self.__discs[i].q()) + (self.__discs[j].p()-self.__discs[i].p())*(self.__discs[j].p()-self.__discs[i].p()));
				#temp_list.append(distance)
				self.__distance_matrix[tuple([i,j])]=round(distance,1)
				#print i,j,distance,relax_min_dist,number_of_clashes
				if(distance <relax_min_dist):
					mclash_score+= (relax_min_dist - distance)**4

					#for both clashing disc increment the clash counter
					self.__disc_clash_counter[i]+=1
					self.__disc_clash_counter[j]+=1
			
		
		avg_x=round(sum_x/tot_disc,1);
		avg_y=round(sum_y/tot_disc,1);
		
		self.__model_mean=[avg_x,avg_y]

		#Return no clash (0)
		self.__clash_score=round(mclash_score,1)
		return 
		



	#This model determines the clashes and compactness for the last discs only
	def clash_and_compactness_finding_function_for_last_disc(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		relax_min_dist=float(bdm.get_mindist());
		radius=bdm.get_drad();
		gap=bdm.get_dbwd();
		
		#j is the last disx index
		j=len(self.__discs)-1;
		#dist between first and last disk
		dfl=0;
		Total_dimers=16;
		#Tolerance for compactness which is equal to 1 disc + 1 gap
		tolerance=1*(2*radius+gap);
		for i in range (len(self.__discs)-3,0,-1):
			distance= sqrt((self.__discs[j].q()-self.__discs[i].q())*(self.__discs[j].q()-self.__discs[i].q()) + (self.__discs[j].p()-self.__discs[i].p())*(self.__discs[j].p()-self.__discs[i].p()));
			dfl=distance;
			if(distance <relax_min_dist):
				#Model has clash return zero
				return 0;
		IMD=(Total_dimers-j)*(2*radius+gap);
		if (IMD +tolerance < dfl):
			return 0;
				
		return 1;
	
	#This module determnine the camnpactness for the first and the lasdt discs
	def compactness_finding_function_first_last_disc(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		relax_max_dist=float(bdm.get_maxdist())+20;
		i=0;
		j=len(self.__discs)-1;
		distance= sqrt((self.__discs[j].q()-self.__discs[i].q())*(self.__discs[j].q()-self.__discs[i].q()) + (self.__discs[j].p()-self.__discs[i].p())*(self.__discs[j].p()-self.__discs[i].p()));
		
		if(distance >relaxed_max_distance):
			#Model not compact
			return 0;
		   
		return 1;
	
	#Determine the clash of the last dics vs the all
	def clash_finding_function_last_vs_all(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		relax_min_dist=float(bdm.get_mindist());
		for i in range(0,len(self.__discs)-1):
			j=len(self.__discs)-1;
			distance= sqrt((self.__discs[j].q()-self.__discs[i].q())*(self.__discs[j].q()-self.__discs[i].q()) + (self.__discs[j].p()-self.__discs[i].p())*(self.__discs[j].p()-self.__discs[i].p()));
			if(distance <relax_min_dist):
				return 0;
				   
				
		return 1;
	
		
	#This the scoring fucntion which takes care of the allowed states and then score the model
	def scoring_function(self,bdm,ds):
		"""Summary
		
		Args:
		    bdm (TYPE): Description
		    ds (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		relax_max_dist=float(bdm.get_maxdist());
		relax_min_dist=float(bdm.get_mindist());

		for i in range(0,len(self.__discs)):
			for j in range(i+1,len(self.__discs)):
				
				score1,score2=0,0

				distance= sqrt((self.__discs[j].q()-self.__discs[i].q())*(self.__discs[j].q()-self.__discs[i].q()) + (self.__discs[j].p()-self.__discs[i].p())*(self.__discs[j].p()-self.__discs[i].p()));
					
				if(distance >=relax_min_dist):
					if(distance <= relax_max_dist):
						pass
						
						#disc_state=ds.calculate_state(self.__discs[i],self.__discs[j]);
						#flag=search_allowed_state(disc_state);
						#if (flag==true):
						#	print "satisfy modes\n",i,j,disc_state[0];
					else:
						score1=self.gaussian_distance(self.__discs[i],self.__discs[j],relax_max_dist,3)[1];
							
				else:
					score2=self.gaussian_distance(self.__discs[i],self.__discs[j],relax_min_dist,3)[1];
					status=0;
					print("Clashed Structure");
					#from sys import exit
					#sys.exit(status);
						
				
		#Score
		#abs_phase=gaussian_phase(self.__discs[0],self.__discs[3],200,3)[1];
		
		self.__model_score=score1+score2

		
		return 0;
	
	def translatepoint(self,P,shear,pvX):
		"""Summary
		
		Args:
		    P (TYPE): Description
		    shear (TYPE): Description
		    pvX (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		#initializing coordinates of new point
		P_new=[0,0];
		P_new[0]=P[0]+shear*pvX[0];
		P_new[1]=P[1]+shear*pvX[1];
		#P_new[2]=P[2]+shear*pvX[2];
	
		return P_new;
		
	def roundupto_x(num,x):
		"""Summary
		
		Args:
		    num (TYPE): Description
		    x (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		return floor((num + x/2.0) / x) * x;
		
	def search_allowed_state(disc_state):
		"""Summary
		
		Args:
		    disc_state (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		for value in Modes:
			nshear=roundupto_x(disc_state[0],shear_steps);
			ntheta1=roundupto_x(disc_state[1],theta1_steps);
			ntheta2=roundupto_x(disc_state[2],theta2_steps);
			if (nshear==value[0]):
				if (ntheta1==value[1]):
					if (ntheta2==value[2]):
						return true;
		return false;
		
		
	def harmonic_distance(d1,d2,k,mean):
		"""Summary
		
		Args:
		    d1 (TYPE): Description
		    d2 (TYPE): Description
		    k (TYPE): Description
		    mean (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		x=distance(d1, d2);
		score=0.5*k*(x-mean)*(x-mean);
		values=[x,score];
		return values;
		
	def harmonic_phase(d1,d2,k,mean):
		"""Summary
		
		Args:
		    d1 (TYPE): Description
		    d2 (TYPE): Description
		    k (TYPE): Description
		    mean (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		d1_p=d1.aphase();
		d2_p=d2.aphase();
		rel_p= abs(d1_p-d2_p);
		#Normalize the phase with 360 degrees so that score will not be increased to high values.
		#Mean and relative phase values after normalize will be in range (0,1)
		score=0.5*k*((rel_p-mean)/360)*((rel_p-mean)/360);
		values=[rel_p,score];
		return values;
		
	def gaussian_phase(self,d1,d2,mu,sigma):
		"""Summary
		
		Args:
		    d1 (TYPE): Description
		    d2 (TYPE): Description
		    mu (TYPE): Description
		    sigma (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		d1_p=d1.aphase();
		d2_p=d2.aphase();
		rel_p= abs(d1_p-d2_p);
		#Normalize the phase with 360 degrees so that score will not be increased to high values.
		#Mean and relative phase values after normalize will be in range (0,1)
		#score=0.5*k*((rel_p-mean)/360)*((rel_p-mean)/360);
		rel_p_s=(rel_p-mu)/sigma;
		mag=1/(sigma* sqrt(2 * PI));
		score_g= exp(-rel_p_s*rel_p_s / 2)*mag;
		#Inverting the gaussian curve so as to make score at mean minimum and adding magnitude to make it zero
		score=-1*score_g+mag;
		values=[rel_p,score];
		return values;
		
	def gaussian_distance(self,d1,d2,mu,sigma):
		"""Summary
		
		Args:
		    d1 (TYPE): Description
		    d2 (TYPE): Description
		    mu (TYPE): Description
		    sigma (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		x=self.distance(d1, d2);
		x_s=(x-mu)/sigma;
		mag=1/(sigma* sqrt(2 * PI));
		score_g= exp(-x_s*x_s / 2.0)*mag;
		#Inverting the gaussian curve so as to make score at mean minimum and adding magnitude to make it zero
		score=-1*score_g+mag;
		values=[x,score];
		return values;
		
	
	def distance(self,d1,d2):
		"""Summary
		
		Args:
		    d1 (TYPE): Description
		    d2 (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		#calculate the euclidian distance between two self.__discs
		dis= sqrt((d2.q()-d1.q())*(d2.q()-d1.q()) + (d2.p()-d1.p())*(d2.p()-d1.p()));
		return dis;

	def sdistance(self,coord1,coord2):
		"""Summary
		
		Args:
		    coord1 (TYPE): Description
		    coord2 (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		#calculate the euclidian distance between two self.__discs
		sdis= (coord2[0]-coord1[0])**2 + (coord2[1]-coord1[1])**2
		return sdis;
		
	
	
	def read_allowed_states(self,filename):
		"""Summary
		
		Args:
		    filename (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		tokens = [];#print filename
		try:
			
			line_count=0;
			br=open(filename,'r')
			#Read File Line By Line
			for strLine in br.readlines():
			
				#Skip if line is empty
				if (len(strLine.strip()) != 0):
					#Skip if line starts with '#'
					if (strLine[0]!='#'):
						line_count+=1;
						temp=[]
						#Parse the line with space OR multiple spaces as delimiter
						tokens = strLine.split("\t");
						for i in range(0,len(tokens)):
							#System.out.println(tokens[i]);
							temp.append(float(tokens[i]));
						self.__Modes.append(temp);
															
			#Close the input stream
			br.close();
			
		except IOError:
			print ("Error: ");
		return
		
	def clash_score(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__clash_score

	def model_score(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__model_score

	def disc_clash_counter(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__disc_clash_counter

	def tetramer_score(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__tetramer_score

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

	def distance_matrix(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__distance_matrix

	def get_accessibility(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__n_accessible_interacting_regions

	def get_probe(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__probe

	def get_mode_positions(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__mode_positions

		