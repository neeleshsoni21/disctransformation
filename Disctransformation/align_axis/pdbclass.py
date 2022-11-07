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

from os import system

#dictionary for converting three letter code to one letter code
THREEONE={'LEU':'L','PHE':'F','TRP':'W','TYR':'Y','ASN':'N','ASP':'D','HIS':'H','VAL':'V','ILE':'I',
'PRO':'P','THR':'T','GLY':'G','ALA':'A','SER':'S','CYS':'C','GLN':'Q','GLU':'E','MET':'M','LYS':'K','ARG':'R'}

AMINOACID=['LEU','PHE','TRP','TYR','ASN','ASP','HIS','VAL','ILE',
'PRO','THR','GLY','ALA','SER','CYS','GLN','GLU','MET','LYS','ARG',
'SOL']


#Class definition
class PDB:

	"""Summary
	"""
	
	#init function for parsing the pdb format file
	def __init__(self,filename):
		"""Summary
		
		Args:
		    filename (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		#open the file for reading
		pdbfile = open(filename,'r')
		pdblines = pdbfile.readlines()
		pdbfile.close();

		#declaring variables as list for storing values of each column in the pdb file
		self.__serial = []
		self.__name = []
		self.__altLoc = []
		self.__resName = []
		self.__chainID = []
		self.__resSeq  = []
		self.__iCode = []
		self.__x = []
		self.__y = []
		self.__z = []
		self.__T = []

		#Ierating over lines in the pdb file
		for line in pdblines:				
			atom = line[0:6]

			#Skip all HETATM/ANISOU etc
			if ((atom.strip() != 'ATOM')&(atom.strip() != 'HETATM')):
			#if atom.strip() != 'ATOM':
				continue
			
			#Skip all Hydrogens
			element = line[76:78]
			if element.strip() == "H":
				continue

			#Skip all iCodes
			iCode = line[26:27]
			if iCode.strip() != "":
				continue

			#Skip all alternate locations
			altLoc = line[16:17]
			if (altLoc.strip() != "") and (altLoc != "A") and (altLoc != 1):
				continue

			#Skip all non standard amino acids
			if line[17:20].strip() not in AMINOACID:
				continue

			#Initialize class variables with values from the pdbline
			self.__serial.append(int(float(line[6:11])))
			self.__name.append(line[12:16].strip())
			self.__altLoc.append(altLoc.strip())
			self.__resName.append(line[17:20].strip())
			self.__chainID.append(line[21:22].strip())
			self.__resSeq.append(int(line[22:26]))
			self.__iCode.append(line[26:27].strip())
			self.__x.append(float(line[30:38]))
			self.__y.append(float(line[38:46]))
			self.__z.append(float(line[46:54]))
			self.__T.append(float(line[60:66]))
		
		#get the total number of amino acids
		self.__aa_length = len(set(self.__resSeq))
		#Get the total length of the pdbfile
		self.__iter_length = len(self.__x)
		return
	
	#Return all atoms or iteration length
	def iter_length(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__iter_length

	def set_iter_length(self,value):
		"""Summary
		
		Args:
		    value (TYPE): Description
		"""
		self.__iter_length=value
	
	#return amino acid length
	def aa_length(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__aa_length
	
	#return serial if column if the pdb file
	def serial(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__serial
	
	#return the name of the atom
	def name(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__name

	#return altLoc
	def altLoc(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__altLoc
	
	#return the residue name
	def resName(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__resName

	#return the sequence extracted from the structure
	def sequence(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		seq = ""
		#iterate over the total iteration length
		for i in range(self.__iter_length):
			#check if the atom is CA, then add one leter code in the seq variable
			if self.__name[i] == 'CA':
				seq = seq + THREEONE[self.__resName[i]]
		return seq

	#return the sequence map that consists of start and end of the iter variable for every residue
	def sequence_map(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		seq = ''
		seq_map = []
		
		#Get the iter index for the first residue
		cres=0;
		if self.__name[cres] == 'N':
			seq = seq + THREEONE[self.__resName[cres]]
			seq_map.append([cres]);

		#get the iter index for following residues
		for i in range(1,self.__iter_length):
			if self.__name[i] == 'N':
				seq = seq + THREEONE[self.__resName[i]]
				#append the previous residue iter in the previous residue map
				seq_map[-1].append(i-1);
				#append the current residue
				seq_map.append([i]); 

		seq_map[-1].append(self.__iter_length-1);
			
		return seq, seq_map
	
	#return the chain ID
	def chainID(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__chainID

	#return residue number
	def resSeq(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__resSeq

	#return x coordinate
	def x(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__x
	
	#return y coordinate
	def y(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__y
	
	#return z coordinate
	def z(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__z

	#set x coordinate
	def set_x(self,i,value):
		"""Summary
		
		Args:
		    i (TYPE): Description
		    value (TYPE): Description
		"""
		self.__x[i] = value
	
	#set y coordinate
	def set_y(self,i,value):
		"""Summary
		
		Args:
		    i (TYPE): Description
		    value (TYPE): Description
		"""
		self.__y[i] = value
	
	#set z coordinate
	def set_z(self,i,value):
		"""Summary
		
		Args:
		    i (TYPE): Description
		    value (TYPE): Description
		"""
		self.__z[i] = value

	#return temperature factor values
	def T(self):
		"""Summary
		
		Returns:
		    TYPE: Description
		"""
		return self.__T

	#set temperature factor values
	def set_T(self,i,value):
		"""Summary
		
		Args:
		    i (TYPE): Description
		    value (TYPE): Description
		"""
		self.__T[i]=value

	def add_atom_in_model(self,serial,name,resName,chainID,resSeq,x,y,z,T):
		"""Summary
		
		Args:
		    serial (TYPE): Description
		    name (TYPE): Description
		    resName (TYPE): Description
		    chainID (TYPE): Description
		    resSeq (TYPE): Description
		    x (TYPE): Description
		    y (TYPE): Description
		    z (TYPE): Description
		    T (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		self.__serial.append(serial)
		self.__name.append(name)
		self.__resName.append(resName)
		self.__chainID.append(chainID)
		self.__resSeq.append(resSeq)
		self.__x.append(x)
		self.__y.append(y)
		self.__z.append(z)
		self.__T.append(T)

		return

	#write pdb file from class object
	def write(self, outfilename):
		"""Summary
		
		Args:
		    outfilename (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		fout = open(outfilename,'w')
		for i in range(self.iter_length()):
			serial = str(self.__serial[i])
			name = self.__name[i]
			resName = self.__resName[i]
			chainID = self.__chainID[i]
			resSeq  = str(self.__resSeq[i])
			x = str("%.3f" % self.__x[i])
			y = str("%.3f" % self.__y[i])
			z = str("%.3f" % self.__z[i])
			T = str("%.3f" % self.__T[i])
			fout.writelines(pdb_line(serial, name, resName, chainID, resSeq, x, y, z, T=T))
		fout.close()
		return

	#write pdb file from class object
	def writeCA(self, outfilename,skip_res='DTA'):
		"""Summary
		
		Args:
		    outfilename (TYPE): Description
		    skip_res (str, optional): Description
		
		Returns:
		    TYPE: Description
		"""
		fout = open(outfilename,'w')
		for i in range(self.iter_length()):
			serial = str(self.__serial[i])
			name = self.__name[i]
			resName = self.__resName[i]
			if ((name != 'CA') or (resName==skip_res)):
				continue
			chainID = self.__chainID[i]
			resSeq  = str(self.__resSeq[i])
			x = str("%.3f" % self.__x[i])
			y = str("%.3f" % self.__y[i])
			z = str("%.3f" % self.__z[i])
			T = str("%.3f" % self.__T[i])
			fout.writelines(pdb_line(serial, name, resName, chainID, resSeq, x, y, z, T=T))
		fout.close()
		return

	#write pdb file from class object for selected atoms
	def write_selection(self, outfilename, selection):
		"""Summary
		
		Args:
		    outfilename (TYPE): Description
		    selection (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		fout = open(outfilename,'w')
		for i in selection:
			serial = str(self.__serial[i])
			name = self.__name[i]
			resName = self.__resName[i]
			chainID = self.__chainID[i]
			resSeq  = str(self.__resSeq[i])
			x = str("%.3f" % self.__x[i])
			y = str("%.3f" % self.__y[i])
			z = str("%.3f" % self.__z[i])
			fout.writelines(pdb_line(serial, name, resName, chainID, resSeq, x, y, z))
		fout.close()
		return

	#write pdb file from class object in multiple models
	def write_selection_multimdl(self, outfilename, selection, modelid):
		"""Summary
		
		Args:
		    outfilename (TYPE): Description
		    selection (TYPE): Description
		    modelid (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		fout = open(outfilename,'a')
		fout.writelines('MODEL        '+modelid+'\n')
		for i in selection:
			serial = str(self.__serial[i])
			name = self.__name[i]
			resName = self.__resName[i]
			chainID = self.__chainID[i]
			resSeq  = str(self.__resSeq[i])
			x = str("%.3f" % self.__x[i])
			y = str("%.3f" % self.__y[i])
			z = str("%.3f" % self.__z[i])
			fout.writelines(pdb_line(serial, name, resName, chainID, resSeq, x, y, z))
		fout.writelines('ENDMDL'+'\n')
		fout.close()
		return
	
	#write pdb file from class object for different chains
	def write_all_chains(self, outfilename):
		"""Summary
		
		Args:
		    outfilename (TYPE): Description
		
		Returns:
		    TYPE: Description
		"""
		fout = open(outfilename,'a')
		for i in range(self.iter_length()):
			serial = str(self.__serial[i])
			name = self.__name[i]
			resName = self.__resName[i]
			chainID = self.__chainID[i]
			resSeq  = str(self.__resSeq[i])
			x = str("%.3f" % self.__x[i])
			y = str("%.3f" % self.__y[i])
			z = str("%.3f" % self.__z[i])
			fout.writelines(pdb_line(serial, name, resName, chainID, resSeq, x, y, z))
		fout.close()
		return

#write pdb line in a file according to pdb format
def pdb_line(serial = "", name = "", resName = "", chainID = "", resSeq  = "", x = "", y = "", z = "", occupancy = "", T = "", element = "", charge = "", altLoc = "", iCode = ""):
	'''serial, name, resName, resSeq , x, y, z, occupancy, T, element, charge, altLoc, chainID, iCode
	
	Args:
	    serial (str, optional): Description
	    name (str, optional): Description
	    resName (str, optional): Description
	    chainID (str, optional): Description
	    resSeq (str, optional): Description
	    x (str, optional): Description
	    y (str, optional): Description
	    z (str, optional): Description
	    occupancy (str, optional): Description
	    T (str, optional): Description
	    element (str, optional): Description
	    charge (str, optional): Description
	    altLoc (str, optional): Description
	    iCode (str, optional): Description
	
	Returns:
	    TYPE: Description
	'''

	serial = str(serial)
	resSeq = str(resSeq)
	x = str(x)
	y = str(y)
	z = str(z)
	occupancy = str(occupancy)
	T = str(T)
	charge = str(charge)

	atom = 'ATOM  '
	serial = serial.rjust(len(range( 6,11)))
	name = name.ljust(len(range(12,15)))
	altLoc = altLoc.ljust(len(range(16,17)))
	resName = resName.ljust(len(range(17,20)))
	chainID = chainID.ljust(len(range(21,22)))
	resSeq = resSeq .rjust(len(range(22,26)))
	iCode = iCode.ljust(len(range(26,27)))
	x = x.rjust(len(range(30,38)))
	y = y.rjust(len(range(38,46)))
	z = z.rjust(len(range(46,54)))
	occupancy = occupancy.rjust(len(range(54,60)))
	T = T.rjust(len(range(60,66)))
	element = element.ljust(len(range(76,78)))
	charge = charge.rjust(len(range(78,80)))

	line = atom + serial + '  ' + name + altLoc + resName + ' ' + chainID + resSeq + iCode + ' '*3 + x + y + z + occupancy + T + ' '*11 + element + charge
	line = line[:80].strip() + '\n'

	return line
