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

class Build_Graph_Model:

	"""Summary
	"""
	
	def __init__(self,adj_matrix):
		"""Summary
		
		Args:
		    adj_matrix (TYPE): Description
		"""
		self.__tot_discs=len(adj_matrix[0])

		self.__node_list=[]

		self.__traverse_order=[]

		for a1 in range(0,self.__tot_discs):
			n1=node()
			n1.set_index(a1);

			self.__node_list.append( n1 )

		for a1 in range(0,self.__tot_discs):
			n1=self.__node_list[a1]
			for a2 in range(a1+1,self.__tot_discs):
				n2=self.__node_list[a2]
				
				if adj_matrix[a1][a2]!='-':
					n1.set_connection(n2);
					n2.set_connection(n1);


	def get_nodelist(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__node_list

	def get_traverse_order(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__traverse_order

	def traverse(self,node):
		"""Summary
		
		Args:
		    node (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		if ((len(node.get_connection())==0) | (node.get_visit()==True)):
			return

		node.set_visit(True)

		connections=node.get_connection();
		for node2 in connections:
			if node2.get_visit()==False:
				#print "connection: ", node.get_index(),node2.get_index()
				self.__traverse_order.append([node.get_index(),node2.get_index()])
				self.traverse(node2);



		return

class node:

	"""Summary
	"""
	
	def __init__(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		self.__index=0
		self.__connections=[]
		self.__visit=False
		return

	def get_visit(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__visit

	def set_visit(self,value):
		"""Summary
		
		Args:
		    value (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		self.__visit=value
		return

	def set_connection(self,value):
		"""Summary
		
		Args:
		    value (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		self.__connections.append(value)
		return
	
	def set_index(self,value):
		"""Summary
		
		Args:
		    value (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		self.__index=value
		return

	def get_connection(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__connections

	def get_index(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__index
		

