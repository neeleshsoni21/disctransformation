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


import sys

class Build_Disc_Model:

	"""Summary
	"""
	
	def __init__(self,args):
		"""Summary
		
		Args:
		    args (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		self.__argsg = ""
		
		#Default Initial position of the first disc
		self.__x = 250.0
		self.__y = 350.0

		#Disc radius (Default 20)
		self.__drad = 0
		#Distance between the succeeding disc (distance between the circumference) (Default 2)
		self.__dbwd=0;
		
		#Number of Discs (Default 10)
		self.__nod=0;
		
		self.__mindist=0;
		self.__maxdist=0;
		
		self.__arguments={'@ARG6':[]}
		self.__mode_dict={}

		if int(args[1])==0:
			self.read_arguments_1(args[2])
		else:
			self.read_arguments_2(args[2])
		
		self.__nod=int(self.__arguments['@ARG1']);		
		self.__drad=float(self.__arguments['@ARG2']);
		self.__dbwd=float(self.__arguments['@ARG3']);
		self.__model=self.__arguments['@ARG4'];

		self.__outputfile=self.__arguments['@ARG7'];

		'''ADDED FOR PRINTING'''
		#self.__outputfile='./output/'+self.__outputfile.split('/')[-1]
		
		self.__maxdist=self.__arguments['@ARG8'];
		self.__mindist=self.__arguments['@ARG9'];
		self.__model_id=self.__arguments['@ARG10'];

		self.__discs=[]
		self.__mode_positions=[]
		self.__asa_mesh={}

		self.__x = self.__nod*(self.__drad*2);
		self.__y = self.__nod*(self.__drad*2);

		self.__InteractingSites = [[],[],[],[None,None]]

		
		return

	def get_mindist(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__mindist

	def get_maxdist(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__maxdist

	def get_outfile(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__outputfile

	def get_model(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__model

	def get_dbwd(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__dbwd

	def get_drad(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__drad

	def get_nod(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__nod

	def get_model_id(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__model_id

	def get_arguments(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__arguments

	def get_discs(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__discs

	def get_ARG5(self,sl):
		"""Summary
		
		Args:
		    sl (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		lsplit=sl.split(' ')
		modes=lsplit[1:];
		for m in modes:
			toks=m.split(':');
			self.__mode_dict[toks[0]]=toks[1:]
			self.__arguments[lsplit[0]]=self.__mode_dict
		
		return

	def get_mode_positions(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__mode_positions
	
	def get_ARG_ALL(self,sl):
		"""Summary
		
		Args:
		    sl (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		lsplit=sl.split(' ')
		self.__arguments[lsplit[0]]=lsplit[1];
		
		return

	def read_arguments_1(self,fname):
		"""Summary
		
		Args:
		    fname (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		try:
			inf=open(fname,'r');
			lines=inf.readlines();
			inf.close()
		except IOError:#Catch exception if any
			#fname='./output/'+fname.split('/')[-1]
			print("Error: Following Input file Not Found",fname)
			

		task_dict={'@ARG5':self.get_ARG5, '@ARG1':self.get_ARG_ALL, '@ARG2':self.get_ARG_ALL,
		'@ARG3':self.get_ARG_ALL, '@ARG4':self.get_ARG_ALL, '@ARG6':self.get_ARG_ALL, '@ARG7':self.get_ARG_ALL,
		'@ARG8':self.get_ARG_ALL, '@ARG9':self.get_ARG_ALL, '@ARG10':self.get_ARG_ALL}
		

		flag6=False;
		for l in lines:

			sl=l.strip();
			if len(sl)==0:
				continue;
			if sl[0]=='#':
				continue;
			if sl[0]=='@':
				if sl=='@ARG6':
					flag6=True;
				else:
					flag6=False;
										
					task_dict[sl.split(' ')[0]](sl)
			elif flag6==True:
				self.__arguments['@ARG6'].append( list(sl) )

		#for k,v in self.__arguments.items():
		#	print k,v
		
		return 

	def read_arguments_2(self,file_str):
		"""Summary
		
		Args:
		    file_str (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		lines=file_str.split('\n');

		task_dict={'@ARG5':self.get_ARG5, '@ARG1':self.get_ARG_ALL, '@ARG2':self.get_ARG_ALL,
		'@ARG3':self.get_ARG_ALL, '@ARG4':self.get_ARG_ALL, '@ARG6':self.get_ARG_ALL, '@ARG7':self.get_ARG_ALL,
		'@ARG8':self.get_ARG_ALL, '@ARG9':self.get_ARG_ALL, '@ARG10':self.get_ARG_ALL}
		

		flag6=False;
		for l in lines:
			sl=l.strip();
			if len(sl)==0:
				continue;
			if sl[0]=='#':
				continue;
			if sl[0]=='@':
				if sl=='@ARG6':
					flag6=True;
				else:
					flag6=False;
										
					task_dict[sl.split(' ')[0]](sl)
			elif flag6==True:
				self.__arguments['@ARG6'].append( list(sl) )

		#for k,v in self.__arguments.items():
		#	print k,v
		
		return
	
	def Translate_Interacting_Sites(self,InteractingSites):
		"""Summary
		
		Args:
		    InteractingSites (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		from numpy import sqrt, mean

		[Xcoord,Ycoord,Zcoord,center] = InteractingSites[:]
		
		dist =  sqrt((center[0] - self.__x)**2 + (center[1] - self.__y)**2)

		dcx = ( self.__x - center[0])/dist;
		dcy = ( self.__y - center[1])/dist;

		#self.__InteractingSites = [[],[],Zcoords,None]

		for i,(x,y) in enumerate(zip(Xcoord,Ycoord)):

			self.__InteractingSites[0].append(Xcoord[i]+dcx*dist);
			self.__InteractingSites[1].append(Ycoord[i]+dcy*dist);

		self.__InteractingSites[2] = Zcoord[:]
		self.__InteractingSites[3] = [mean(self.__InteractingSites[0]),mean(self.__InteractingSites[1])]

		return

	def build_disc(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		from core.discstructure import discstructure
		from core.transformation import transformation
		from core.create_graph import Build_Graph_Model
		
		#Initialize discs
		d=[]

		#Get the default disc structure. This is given by discstructure constructor
		for i in range(0,self.__nod):

			discobj = discstructure()

			discobj.set_id(i)
			
			#Set Interacting Sites If present in the model
			discobj = discobj.Set_InteractingSites(self.__InteractingSites)

			d.append(discobj)
		
		
		T= transformation();
		
		#Create starting disc at the position given by x,y
		d[0].init_new_starting_disc(d[0],self.__x,self.__y,self.__drad);
		
		#Create succeeding discs
		connections=self.__arguments['@ARG6']
		
		GM=Build_Graph_Model(connections)
		nodes=GM.get_nodelist()
		
		#for n in nodes:
		#	for n in n.get_connection():
		#		print ("conenctions:",n.get_index(),n.get_visit())
		
		GM.traverse(nodes[0])
		traverse_order=GM.get_traverse_order()

		for pair in traverse_order:
			a1=pair[0]
			a2=pair[1]

			mode=connections[a1][a2]
			
			if mode=='-':
				mode=connections[a2][a1]

			if a2>a1:
				M1=list(map(float,self.__mode_dict[mode]));
				
			else:
				M1=list(map(float,self.__mode_dict[mode]));
				M1=[180-M1[1], 180-M1[0], M1[2],M1[3]]
			
			
			#If input disc number is less than total number of disc then generate the mode else exit
			if((a1<self.__nod) & (a2<self.__nod)):
				T.drawmode(d,a1,a2,self.__x,self.__y,M1,self.__drad,self.__dbwd);
			else:
				print ("Error: Total number Discs in argument 1 is less than the numbers provided in input file!!!");
				sys.exit(0);

		self.__discs=d;

		return d
	
	def write_output_file(self,d, score_obj):
		"""Summary
		
		Args:
		    d (TYPE): Description
		    score_obj (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		line="#Disc Model representation using coordinates. \n"+"#This file gives discs coordinates in tab separated format.\n";
		line+="#First column is the disc number. \n";
		line+="#Second column gives the coordinates of the center of the disc.\n";
		line+="#Third column gives the coordinates of the other point on the disc circumference. \n";
		line+="#Fourth column gives the direction of the discs\n\n"
		for i in range(0,int(self.__nod)):
			vec_c="("+str(round((d[i].p()-self.__x),1))+","+str(round((d[i].q()-self.__y),1))+")";
			vec_r="("+str(round((d[i].r()-self.__x),1))+","+str(round((d[i].s()-self.__y),1))+")"; 
			vec_n=str(i);
			rad_vec=vec_n+"\t"+vec_c+"\t"+vec_r+"\t"+str(d[i].dvec());
			line+=rad_vec+'\n';
		
		try:
			
			#Get score values
			model_id=self.get_model_id()
			model_score=score_obj.model_score()
			tetramer_score=score_obj.tetramer_score()
			clash_score=score_obj.clash_score()
			radial_density=score_obj.radial_density()
			model_mean=score_obj.model_mean()
			max_dist=score_obj.max_dist()

			line+="\nModel ID: "
			line+=str(model_id)
			line+="\nModel Score is: "
			line+=str(model_score)
			line+="\nTetramer Connection Score is: "
			line+=str(tetramer_score)
			line+="\nModel Clash Score is: "
			line+=str(clash_score)
			line+="\nModel radial density: "
			line+=str(" ".join(radial_density))
			line+="\nModel Mean is: "
			line+=str(" ".join(map(str,model_mean)))
			line+="\nModel Max Distance (from mean) is: "
			line+=str(max_dist)
			
			#Open the file for writing
			out=open('./output/Disc_Structure_Coordinates.txt','w');
			out.writelines(line);

			#Close the output stream
			out.close();
			
		except IOError:#Catch exception if any
			print ("Error: ");
		return

	def set_mode_positions(self,probe):
		"""Summary
		
		Args:
		    probe (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		from numpy import cos, sin, array, cross, dot, arctan2
		
		drad=self.get_drad();
		modes=self.get_arguments()['@ARG5']
		d=self.get_discs();
		

		for i in range(0,len(d)):
			a= array([d[0].r()-d[0].p() , d[0].s()-d[0].q()])
			b= array([d[i].r()-d[i].p() , d[i].s()-d[i].q()])
			angle=arctan2( cross(a,b) , dot(a,b))  * 180 / 3.14159 

			pif=-3.1416/180.0
			xcord1=d[i].p();
			ycord1=d[i].q();

			mrad=drad+probe;

			if(d[i].dvec()==1):

				M1 = float(modes['A'][0]); M2 = float(modes['A'][1])
				p1 = [ xcord1+mrad*cos((90-M1-angle)*pif),  ycord1+mrad*sin((90-M1-angle)*pif) ]
				p2 = [ xcord1+mrad*cos((90-(180-M2)-angle)*pif),  ycord1+mrad*sin((90-(180-M2)-angle)*pif) ]
				self.__mode_positions.append(p1)
				self.__mode_positions.append(p2)

				M1 = float(modes['B'][0]); M2 = float(modes['B'][1])
				p1 = [ xcord1+mrad*cos((90-M1-angle)*pif),  ycord1+mrad*sin((90-M1-angle)*pif) ]
				p2 = [ xcord1+mrad*cos((90-(180-M2)-angle)*pif),  ycord1+mrad*sin((90-(180-M2)-angle)*pif) ]
				self.__mode_positions.append(p1)
				self.__mode_positions.append(p2)
			else:
				M1 = float(modes['A'][0]); M2 = float(modes['A'][1])
				p1 = [ xcord1+mrad*cos((90+M1-angle)*pif),  ycord1+mrad*sin((90+M1-angle)*pif) ]
				p2 = [ xcord1+mrad*cos((90+(180-M2)-angle)*pif),  ycord1+mrad*sin((90+(180-M2)-angle)*pif) ]
				self.__mode_positions.append(p1)
				self.__mode_positions.append(p2)

				M1 = float(modes['B'][0]); M2 = float(modes['B'][1])
				p1 = [ xcord1+mrad*cos((90+M1-angle)*pif),  ycord1+mrad*sin((90+M1-angle)*pif) ]
				p2 = [ xcord1+mrad*cos((90+(180-M2)-angle)*pif),  ycord1+mrad*sin((90+(180-M2)-angle)*pif) ]
				self.__mode_positions.append(p1)
				self.__mode_positions.append(p2)

		return

	
	#def argsg(self):
	#	return self.__argsg

