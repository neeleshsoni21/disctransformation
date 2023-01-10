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


#Load the Disctransformation object
import Disctransformation as DT

DT.example_single_run()


DT.example_single_run(
	input_dtfile = './Disctransformation/example/input/gpcr_dimer.txt')


DT.example_single_run(
	input_dtfile = './Disctransformation/example/input/gpcr_trimer.txt')

DT.example_single_run_withpdb(
	input_dtfile = './Disctransformation/example/input/gpcr_dimer.txt', 
	input_pdb = './Disctransformation/example/input/GPCR_Helices.pdb',
	output_dir = './Disctransformation/example/output_gpcr/')

DT.example_single_run_withpdb(
	input_dtfile = './Disctransformation/example/input/gpcr_trimer.txt', 
	input_pdb = './Disctransformation/example/input/GPCR_Helices.pdb',
	output_dir = './Disctransformation/example/output_gpcr/')


DT.example_sampling_run(
	input_dtfile = './Disctransformation/example/input/gpcr_trimer_sample_1mode.txt', 
	input_pdb = './Disctransformation/example/input/GPCR_Helices.pdb',
	output_dir = './Disctransformation/example/output_gpcr_ensemble_1mode/')


DT.example_sampling_run(
	input_dtfile = './Disctransformation/example/input/gpcr_trimer_sample_2mode.txt', 
	input_pdb = './Disctransformation/example/input/GPCR_Helices.pdb',
	output_dir = './Disctransformation/example/output_gpcr_ensemble_2mode/')

DT.example_single_run_withpdb(
	input_dtfile = './Disctransformation/example/input/gpcr_dimer.txt', 
	input_pdb = './Disctransformation/example/input/GPCR_Helices.pdb',
	output_dir = './Disctransformation/example/output_gpcr/',
	align_flag = False)

DT.example_sampling_run(
	input_dtfile = './Disctransformation/example/input/gpcr_trimer_sample_1mode.txt', 
	input_pdb = './Disctransformation/example/input/GPCR_Helices.pdb',
	output_dir = './Disctransformation/example/output_gpcr_ensemble_1mode/',
	align_flag = False)

