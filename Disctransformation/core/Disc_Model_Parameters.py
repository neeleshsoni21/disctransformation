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

class Disc_Model_Parameters:

	"""Summary
	"""
	
	def __init__(self,dt_ifile):
		"""Summary
		
		Args:
		    dt_ifile (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		self.__arguments={'@ARG6':[]}
		self.read_arguments_1(dt_ifile)

		self.__nod=int(self.__arguments['@ARG1']);		
		self.__drad=float(self.__arguments['@ARG2']);
		#self.__dbwd=float(self.__arguments['@ARG3']);
		self.__model=self.__arguments['@ARG4'];
		self.__outputfile=self.__arguments['@ARG7'];
		self.__max_disc_overlap_fraction = float(self.__arguments['@ARG11']); 
		self.__rotation_step = float(self.__arguments['@ARG12']);
		self.__translation_step = float(self.__arguments['@ARG13']);

		
		'''ADDED FOR PRINTING'''
		#self.__outputfile='./output/'+self.__outputfile.split('/')[-1]
		
		#self.__maxdist=self.__arguments['@ARG8'];
		#self.__mindist=self.__arguments['@ARG9'];
		#self.__model_id=self.__arguments['@ARG10'];

		#self.__discs=[]
		#self.__mode_positions=[]
		#self.__asa_mesh={}

		#self.__x = self.__nod*(self.__drad*2);
		#self.__y = self.__nod*(self.__drad*2);

		#self.__InteractingSites = [[],[],[],[None,None]]
		return

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

	"""
	def get_dbwd(self):
		return self.__dbwd
	"""

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

	def get_arguments(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__arguments

	def get_max_disc_overlap_fraction(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__max_disc_overlap_fraction

	def get_rotation_step(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__rotation_step

	def get_translation_step(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__translation_step

	"""
	def get_mindist(self):
		return self.__mindist

	def get_maxdist(self):
		return self.__maxdist

	def get_model_id(self):
		return self.__model_id

	def get_discs(self):
		return self.__discs

	def get_ARG5(self,sl):
		lsplit=sl.split(' ')
		modes=lsplit[1:];
		for m in modes:
			toks=m.split(':');
			self.__mode_dict[toks[0]]=toks[1:]
			self.__arguments[lsplit[0]]=self.__mode_dict
		
		return

	def get_mode_positions(self):
		return self.__mode_positions
	
	"""

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
			

		task_dict={'@ARG1':self.get_ARG_ALL, '@ARG2':self.get_ARG_ALL,
		'@ARG3':self.get_ARG_ALL, '@ARG4':self.get_ARG_ALL, 
		'@ARG6':self.get_ARG_ALL, '@ARG7':self.get_ARG_ALL,
		'@ARG11':self.get_ARG_ALL, '@ARG12':self.get_ARG_ALL,
		'@ARG13':self.get_ARG_ALL,'@ARG14':self.get_ARG_ALL,
		'@ARG15':self.get_ARG_ALL,'@ARG16':self.get_ARG_ALL}
		

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
