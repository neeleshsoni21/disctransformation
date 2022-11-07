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

from math import sqrt, acos

class disc_state:

	"""Summary
	"""
	
	def __init__(self,bdm,discs):
		"""Summary
		
		Args:
		    bdm (TYPE): Description
		    discs (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		self.__discs = discs
		self.__bdm_c = bdm
		#length of keratin dimer 450
		self.__dimer_length=360;
		self.__gap_length=0;
		return
	

	def calculate_state(self,d1,d2):
		"""Summary
		
		Args:
		    d1 (TYPE): Description
		    d2 (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		pi = 3.141592653

		coord1=[d1.r(),d1.s()];
		coord2=[d1.p(),d1.q()];
		coord3=[d2.p(),d2.q()];

		theta1=self.calculate_angle(coord1,coord2,coord3);
		
		flag1=self.crossProductdirection(coord1,coord2,coord3);
		
		coord4=[d1.p(),d1.q()];
		coord5=[d2.p(),d2.q()];
		coord6=[d2.r(),d2.s()];
		theta2=self.calculate_angle(coord4,coord5,coord6);
		
		flag2=self.crossProductdirection(coord4,coord5,coord6);
		
		theta1=theta1*180/pi;
		theta2=theta2*180/pi;
		
		theta1=round(theta1,6);
		theta2=round(theta2,6);
		
		theta2=180-theta2;
				
		if(flag1<0):
			theta1=360-theta1;
		
		if(flag2<0):
			theta2=360-theta2;
		
				
		if(d1.dvec==0):
			theta1=360-theta1;
			theta2=360-theta2;
		
		
		#double distance=Math.sqrt((d2.q-d1.q)*(d2.q-d1.q) + (d2.p-d1.p)*(d2.p-d1.p));
		vshear=0;
		if (d1.dvec==1):
			vshear=d1.shear()-d2.shear();
		else:
			vshear=d2.shear()-d1.shear();
		
		
		quot=int( (vshear/self.__dimer_length));
		
		
		shear=0;
		
		shear=(vshear-quot*self.__gap_length)%self.__dimer_length;
				
		#state={shear,theta1,theta2,distance;
		state=[shear,theta1,theta2];
		return state;
	
	
	
	def calculate_angle(self,c1,c2,c3):
		"""Summary
		
		Args:
		    c1 (TYPE): Description
		    c2 (TYPE): Description
		    c3 (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		s1=self.Distbd(c1,c2);
		s2=self.Distbd(c2,c3);
		s3=self.Distbd(c1,c3);
		#0.00000001 is addeded to remove error caused by rounding of
		value=acos( ( ( (s1*s1)+(s2*s2) ) - (s3*s3) ) / (2*s1*s2+0.000000001) );
		return value
				
	
	
	def Distbd(self,c1,c2):
		"""Summary
		
		Args:
		    c1 (TYPE): Description
		    c2 (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		value=(c2[1]-c1[1])**2 + (c2[0]-c1[0])**2
		return sqrt(value);
		
		
	
	
	def crossProductdirection(self,c1,c2,c3):
		"""Summary
		
		Args:
		    c1 (TYPE): Description
		    c2 (TYPE): Description
		    c3 (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		c21_x = c1[0] - c2[0];
		c21_y = c1[1] - c2[1];
		
		c23_x = c3[0] - c2[0];
		c23_y = c3[1] - c2[1];
		
		dot = c21_x*c23_y - c23_x*c21_y;
		return dot;

	
	
	


