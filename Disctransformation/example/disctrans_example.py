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

from pathlib import Path
dt_root = str(Path(__file__).parent.parent)


def example_single_run(input_dtfile=dt_root+'/example/input/gpcr_dimer.txt'):
	"""Summary
	
	Returns:
	    TYPE: Description
	
	Args:
	    input_dtfile (TYPE): Description
	"""
	from core.Initiate_Search import generate_single_configuration
	generate_single_configuration(input_dtfile)

	return

def example_single_run_withpdb(input_dtfile, input_pdb, output_dir):
	"""Summary
	
	Returns:
	    TYPE: Description
	
	Args:
	    input_dtfile (TYPE): Description
	    input_pdb (TYPE): Description
	    output_dir (TYPE): Description
	"""
	from core.Initiate_Search import generate_single_configuration_withpdb
	generate_single_configuration_withpdb(input_dtfile, input_pdb, output_dir)

	return

def example_sampling_run(input_dtfile, input_pdb, output_dir):
	"""Summary
	
	Args:
	    input_dtfile (TYPE): Description
	    input_pdb (TYPE): Description
	    output_dir (TYPE): Description
	
	Returns:
	    TYPE: Description
	"""
	from core.Initiate_Search import generate_ensemble_configurations
	generate_ensemble_configurations(input_dtfile, input_pdb, output_dir)

	return


