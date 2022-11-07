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

import os
import os.path
from pathlib import Path
from argparse import ArgumentParser, RawDescriptionHelpFormatter

dt_root = str(Path(__file__).parent.parent)


def validate_args(DTparams):
	"""Summary
	
	Args:
	    DTparams (TYPE): Description
	
	Returns:
	    TYPE: Description
	"""
	return True

def Arguments_Parse_v2():
	"""Summary
	
	Returns:
	    TYPE: Description
	"""
	example_input = os.path.join(dt_root,'example/input/2zta.pdb')

	example_adj_file = os.path.join(dt_root,'example/input/2zta_adjacency.dat')

	example_output_dir = os.path.join(dt_root,'example/output_2zta/')

	# -----------------------------------------
	# Command Line arguments Definitions
	# -----------------------------------------

	# Parse commandline Inputs
	parser_obj = ArgumentParser(description=__doc__, formatter_class=RawDescriptionHelpFormatter)

	parser_obj.add_argument("-i", "--input_pdb", default=example_input, help="Example Input PDB coordinates")

	parser_obj.add_argument("-a", "--dt_ifile", default=example_dt_ifile, help="Example Disctransformation File")

	parser_obj.add_argument("-t", "--run_type", default="single", help="")

	parser_obj.add_argument("-o", "--output_dir", default=example_output_dir, help="Example Output Directory")

	args = parser_obj.parse_args()
	
	input_pdb = os.path.abspath(args.input_pdb)

	adj_file = os.path.abspath(args.adj_file)

	output_dir = os.path.abspath(args.output_dir)
	
	DTparams = {'input_pdb':input_pdb, 'adj_file':adj_file, 'output_dir':output_dir}

	if validate_args(DTparams):
		return DTparams
	else:

		print("Incorrect Input Data")
		sys.exit(1)

	return None

def Arguments_Parse():
	"""Summary
	
	Returns:
	    TYPE: Description
	"""
	example_input = os.path.join(dt_root,'example/input/2zta.pdb')

	example_adj_file = os.path.join(dt_root,'example/input/2zta_adjacency.dat')

	example_output_dir = os.path.join(dt_root,'example/output_2zta/')

	# -----------------------------------------
	# Command Line arguments Definitions
	# -----------------------------------------

	# Parse commandline Inputs
	parser_obj = ArgumentParser(description=__doc__, formatter_class=RawDescriptionHelpFormatter)

	parser_obj.add_argument("-i", "--input_pdb", default=example_input, help="Example Input PDB coordinates")

	parser_obj.add_argument("-a", "--adj_file", default=example_adj_file, help="Example Adjacency matrix for sampling")

	parser_obj.add_argument("-o", "--output_dir", default=example_output_dir, help="Example Output Directory")

	args = parser_obj.parse_args()
	
	input_pdb = os.path.abspath(args.input_pdb)

	adj_file = os.path.abspath(args.adj_file)

	output_dir = os.path.abspath(args.output_dir)
	
	DTparams = {'input_pdb':input_pdb, 'adj_file':adj_file, 'output_dir':output_dir}

	if validate_args(DTparams):
		return DTparams
	else:

		print("Incorrect Input Data")
		sys.exit(1)

	return None

if __name__ == '__main__':
	Arguments_Parse()