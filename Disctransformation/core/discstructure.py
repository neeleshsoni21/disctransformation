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

from math import sqrt
from numpy import mean

class discstructure:

	"""Summary
	"""
	
	def __init__(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		#Coordinates of the discs centre and 12 O'Clock position on the circumference
		self.__p = 0.0
		self.__q = 0.0

		#12 O'Clock position
		self.__r = 0.0
		self.__s = 0.0

		#Direction cosines
		self.__l = 0.0
		self.__m = 0.0

		#Direction of the vector perpendicular to the surface
		self.__dvec = 0

		#Whether the disc is fixed or not
		self.__fixed = 0;
		
		#Transformed Values of Disc and variables to track the state
		self.__theta1 = 0.0
		self.__theta2 = 0.0
		self.__shear = 0.0
		self.__aphase = 0.0

		#Interacting Sites, Eg: Say CA atoms of crosslinks
		self.__InteractingSites = [[],[],[],[None,None]]

		#Similar to the __shear but a list to contains all possible interacting sites
		self.__level = []

		self.__id = -1

		return
	
	
	'''
	* This method initialised the initial disc with coordinates.
	* @param x x position
	* @param y y position
	* @param drad disc radius
	* @param vec disc vector 0/1
	'''
	def initdisc(self,x, y, drad, vec):
		"""Summary
		
		Args:
		    x (TYPE): Description
		    y (TYPE): Description
		    drad (TYPE): Description
		    vec (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		#Describes two pos of the radius vector
		self.__p=x;self.__q=y;self.__r=x;self.__s=y-drad;
		
		return
	
	'''
	* This method initialises all the discs except the first disc. This is because
	* all the disc except the first one should be initialised with respect to the previous disc d.
	* @param d discstructure object
	* @param drad disc radius
	* @param x x position
	* @param y y position
	* @param vec next disc vector
	'''
	def initnxtdisc(self, d,  drad,  dbwd,  x,  y, vec):
		"""Summary
		
		Args:
		    d (TYPE): Description
		    drad (TYPE): Description
		    dbwd (TYPE): Description
		    x (TYPE): Description
		    y (TYPE): Description
		    vec (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		#transform the previous disc properties to get the new disc properties
		disb=dbwd;
		self.__p=d.p() + (2*drad+disb)*d.l();self.__q=d.q() + (2*drad+disb)*d.m();
		self.__r=d.r() + (2*drad+disb)*d.l();self.__s=d.s() + (2*drad+disb)*d.m();
		self.__l=d.l();self.__m=d.m();
		self.__dvec=vec;
		

		if len(d.Get_InteractingSites()[0])==0:
			return

		#Transform the Interacting sites as well if present. This includes x-y-z-center
		self.Set_InteractingSites(d.Get_InteractingSites())

		for k,(x,y) in enumerate(zip(d.Get_InteractingSites()[0],d.Get_InteractingSites()[1])):
			
			self.__InteractingSites[0][k] = x + (2*drad+disb)*d.l() 
			self.__InteractingSites[1][k] = y + (2*drad+disb)*d.m()

		#This update may not be required. Already done! Please check
		self.__InteractingSites[3] = [mean(self.__InteractingSites[0]),mean(self.__InteractingSites[1])]

		return
	
	'''
	* This method initialises the Interacting sites (Such as xlinked CA atoms) 
	* on the discs using coordinates provided for scoring.
	* @param InteractingSites. This contains x-y-z-mean coordinates of the Interacting sites
	'''
	def Set_InteractingSites(self,InteractingSites):
		"""Summary
		
		Args:
		    InteractingSites (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		#Deep copy the InteractingSites variable. NOT using DEEPCOPY
		[Xcoord,Ycoord,Zcoord,center] = InteractingSites[:]
		self.__InteractingSites[0]=Xcoord[:]
		self.__InteractingSites[1]=Ycoord[:]
		self.__InteractingSites[2]=Zcoord[:]
		self.__InteractingSites[3]=center[:]
		
		return self

	def Set_InteractionSitesCENTER(self,center):
		"""Summary
		
		Args:
		    center (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		self.__InteractingSites[3]=center[:]

		return

	'''
	* This method returns the Interacting Sites of the disc object
	'''
	def Get_InteractingSites(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__InteractingSites

	def set_id(self,value):
		"""Summary
		
		Args:
		    value (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		self.__id = value
		return

	def get_id(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__id

	'''
	* This method calculates the direction cosines of the radius vector of the disc
	'''
	def getdc(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		mod = sqrt( (self.__r-self.__p)*(self.__r-self.__p) + (self.__s-self.__q)*(self.__s-self.__q) )
		self.__l=(self.__r-self.__p)/mod;
		self.__m=(self.__s-self.__q)/mod;
		
		return
	
	'''
	* This method defines the shape and length of the disc radius vector as polygon
	* @return the shape of the discs
	'''
	'''public Shape defineshape():
		[] pXs = { () p, () rreturn;
		[] pYs = { () q, () sreturn;
		Shape shape = new Polygon(pXs, pYs, pXs.length);
		return shape;
	return
	'''
	'''
	* This method initialises the disc without giving the relative disc. 
	* It takes the disc position as arguments  
	* @param g2d Graphics object
	* @param d discstructure object
	* @param x x position
	* @param y y position
	* @param drad disc radius
	* @param CLR Colour of the disc
	'''
	def init_new_starting_disc(self, d, x, y, drad):
		"""Summary
		
		Args:
		    d (TYPE): Description
		    x (TYPE): Description
		    y (TYPE): Description
		    drad (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		d.initdisc(x,y,drad,1);
		d.set_dvec(1);
		d.set_aphase(0);
		d.set_shear(0);
		d.getdc();
		d.set_fixed(1);

		#print("Init Disc",self.__InteractingSites[3])

		return
	
	'''
	* This method calculates the distance between each discs and returns the
	* minimum distance
	* @param d discstructure[], array containing all discs
	* @return dist - the minimum distance between all discs.
	'''
	'''Calculate_dist([] d) {
		 dist=100000;
		#loop over all disc disc distances and return the least one
		for ( i=0;i<eger.valueOf(argsg[0]);i++):
			for ( j=i+1;j<eger.valueOf(argsg[0]);j++):
				 dis=distance(d[i],d[j]);
				if (dis < dist):
					dist=dis;
				return
			return
		return
		return dist;
	return'''

	
	
	def theta1(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__theta1
	
	def theta2(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__theta2
		
	def shear(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__shear
	
	def aphase(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__aphase
	
	def p(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__p
	
	def q(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__q
	def r(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__r
	def s(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__s
		
	def l(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__l
	def m(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__m
	
	def dvec(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__dvec
	
		
	
	def set_theta1(self,val):
		"""Summary
		
		Args:
		    val (TYPE): Description
		"""
		self.__theta1=val
	
	def set_theta2(self,val):
		"""Summary
		
		Args:
		    val (TYPE): Description
		"""
		self.__theta2=val
		
	def set_shear(self,val):
		"""Summary
		
		Args:
		    val (TYPE): Description
		"""
		self.__shear=val
	
	def set_aphase(self,val):
		"""Summary
		
		Args:
		    val (TYPE): Description
		"""
		self.__aphase=val
	
	def set_p(self,val):
		"""Summary
		
		Args:
		    val (TYPE): Description
		"""
		self.__p=val
	
	def set_q(self,val):
		"""Summary
		
		Args:
		    val (TYPE): Description
		"""
		self.__q=val
	def set_r(self,val):
		"""Summary
		
		Args:
		    val (TYPE): Description
		"""
		self.__r=val
	def set_s(self,val):
		"""Summary
		
		Args:
		    val (TYPE): Description
		"""
		self.__s=val
		
	def set_l(self,val):
		"""Summary
		
		Args:
		    val (TYPE): Description
		"""
		self.__l=val
	def set_m(self,val):
		"""Summary
		
		Args:
		    val (TYPE): Description
		"""
		self.__m=val
	
	def set_dvec(self,val):
		"""Summary
		
		Args:
		    val (TYPE): Description
		"""
		self.__dvec=val
	def set_dcolor(self,val):
		"""Summary
		
		Args:
		    val (TYPE): Description
		"""
		self.__dcolor=val

	def set_fixed(self,flag):
		"""Summary
		
		Args:
		    flag (TYPE): Description
		"""
		self.__fixed=flag

	def fixed(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__fixed




		
