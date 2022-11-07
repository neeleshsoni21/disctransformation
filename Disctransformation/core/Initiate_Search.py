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
import os
import copy
import numpy as np
from pathlib import Path
from itertools import product
from core.Disctransformation import DiscTransformation

def validate_paths(dtpath):
	"""Summary
	
	Args:
	    dtpath (TYPE): Description
	
	Returns:
	    TYPE: Description
	"""
	
	dtpath_bool = os.path.exists(dtpath)
	return dtpath_bool

def get_input_fstr(arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9,arg10):
	"""Summary
	
	Args:
	    arg1 (TYPE): Description
	    arg2 (TYPE): Description
	    arg3 (TYPE): Description
	    arg4 (TYPE): Description
	    arg5 (TYPE): Description
	    arg6 (TYPE): Description
	    arg7 (TYPE): Description
	    arg8 (TYPE): Description
	    arg9 (TYPE): Description
	    arg10 (TYPE): Description
	
	Returns:
	    TYPE: Description
	"""
	file_str=""
	file_str+="@ARG1 "+str(arg1)+"\n"
	file_str+="@ARG2 "+str(arg2)+"\n"
	file_str+="@ARG3 "+str(arg3)+"\n"
	file_str+="@ARG4 "+str(arg4)+"\n"
	file_str+="@ARG5 "+str(arg5)+"\n"
	file_str+="@ARG6\n"+str(arg6)+"\n"
	file_str+="@ARG7 "+str(arg7)+"\n"
	file_str+="@ARG8 "+str(arg8)+"\n"
	file_str+="@ARG9 "+str(arg9)+"\n"
	file_str+="@ARG10 "+str(arg10)+"\n"

	return file_str

def get_all_atoms(mdl):
	"""Summary
	
	Args:
	    mdl (TYPE): Description
	
	Returns:
	    TYPE: Description
	"""
	Xmin,Ymin=1000000,1000000
	Xmax,Ymax=-1000000,-1000000

	Xcoord,Ycoord,Zcoords,center,IterIdxs,XlinkIdxs=[],[],[],[],[],[]
	for i in range(0,mdl.iter_length()):

		Xcoord.append(mdl.x()[i])
		Ycoord.append(mdl.y()[i])
		Zcoords.append(mdl.z()[i])
		IterIdxs.append(i)

		if Xmin>mdl.x()[i]:
			Xmin = mdl.x()[i]
		elif Xmax < mdl.x()[i]:
			Xmax = mdl.x()[i]

		if Ymin>mdl.y()[i]:
			Ymin = mdl.y()[i]
		elif Ymax < mdl.y()[i]:
			Ymax = mdl.y()[i]
	
	center = [np.mean(Xcoord),np.mean(Ycoord)]

	return Xcoord,Ycoord,Zcoords, center, [Xmin,Xmax], [Ymin,Ymax], IterIdxs, XlinkIdxs

def get_all_CA_atoms(mdl):
	"""Summary
	
	Args:
	    mdl (TYPE): Description
	
	Returns:
	    TYPE: Description
	"""
	Xmin,Ymin=1000000,1000000
	Xmax,Ymax=-1000000,-1000000

	Xcoord,Ycoord,Zcoords,center,IterIdxs,XlinkIdxs=[],[],[],[],[],[]
	for i in range(0,mdl.iter_length()):

		if ((mdl.resName()[i] == 'DTA') | (mdl.name()[i] != 'CA')):
			continue

		Xcoord.append(mdl.x()[i])
		Ycoord.append(mdl.y()[i])
		Zcoords.append(mdl.z()[i])
		IterIdxs.append(i)

		if Xmin>mdl.x()[i]:
			Xmin = mdl.x()[i]
		elif Xmax < mdl.x()[i]:
			Xmax = mdl.x()[i]

		if Ymin>mdl.y()[i]:
			Ymin = mdl.y()[i]
		elif Ymax < mdl.y()[i]:
			Ymax = mdl.y()[i]

	center = [np.mean(Xcoord),np.mean(Ycoord)]

	return Xcoord,Ycoord,Zcoords, center, [Xmin,Xmax], [Ymin,Ymax], IterIdxs, XlinkIdxs

def get_interacting_atoms(mdl):
	"""Summary
	
	Args:
	    mdl (TYPE): Description
	
	Returns:
	    TYPE: Description
	"""
	Xcoord,Ycoord=[],[]

	Zcoords = []

	IterIdxs = []; XlinkIdxs=[]; idxcounter=-1

	Xmin,Ymin=1000000,1000000
	Xmax,Ymax=-1000000,-1000000

	for i in range(0,mdl.iter_length()):

		#if mdl.resName()[i] != 'DTA':
		#	continue

		#OR BELOW
		
		if ((mdl.resName()[i] == 'DTA') | (mdl.name()[i] != 'CA')):
			continue		
		
		Xcoord.append(mdl.x()[i])
		Ycoord.append(mdl.y()[i])
		Zcoords.append(mdl.z()[i])
		IterIdxs.append(i)
		idxcounter+=1

		if mdl.resSeq()[i] in [42,170,203,264,286]:

			XlinkIdxs.append(idxcounter)

		if Xmin>mdl.x()[i]:
			Xmin = mdl.x()[i]
		elif Xmax < mdl.x()[i]:
			Xmax = mdl.x()[i]

		if Ymin>mdl.y()[i]:
			Ymin = mdl.y()[i]
		elif Ymax < mdl.y()[i]:
			Ymax = mdl.y()[i]
	
	center = [np.mean(Xcoord),np.mean(Ycoord)]

	return Xcoord,Ycoord,Zcoords,center,[Xmin,Xmax],[Ymin,Ymax], IterIdxs, XlinkIdxs

def get_all_interacting_atoms(mdl):
	"""Summary
	
	Args:
	    mdl (TYPE): Description
	
	Returns:
	    TYPE: Description
	"""
	Xcoord,Ycoord=[],[]

	Zcoords = []

	IterIdxs = []; XlinkIdxs=[]; idxcounter=-1

	Xmin,Ymin=1000000,1000000
	Xmax,Ymax=-1000000,-1000000

	for i in range(0,mdl.iter_length()):

		#if mdl.resName()[i] != 'DTA':
		#	continue

		#OR BELOW
		
		if ((mdl.resName()[i] == 'DTA') | (mdl.name()[i] != 'CA')):
			continue		
		
		Xcoord.append(mdl.x()[i])
		Ycoord.append(mdl.y()[i])
		Zcoords.append(mdl.z()[i])
		IterIdxs.append(i)

		if Xmin>mdl.x()[i]:
			Xmin = mdl.x()[i]
		elif Xmax < mdl.x()[i]:
			Xmax = mdl.x()[i]

		if Ymin>mdl.y()[i]:
			Ymin = mdl.y()[i]
		elif Ymax < mdl.y()[i]:
			Ymax = mdl.y()[i]
	
	center = [np.mean(Xcoord),np.mean(Ycoord)]

	return Xcoord,Ycoord,Zcoords,center,[Xmin,Xmax],[Ymin,Ymax], IterIdxs, XlinkIdxs

def get_full_sample_space(Number_of_Modes, theta1_step, overlapRad, dwd_step):
	"""Summary
	
	Args:
	    Number_of_Modes (TYPE): Description
	    theta1_step (TYPE): Description
	    overlapRad (TYPE): Description
	    dwd_step (TYPE): Description
	
	Returns:
	    TYPE: Description
	"""
	THETA=[];
	
	theta1s = np.arange(0,360,theta1_step)

	dwdvals = np.arange(-1*overlapRad,0.000000001,dwd_step)

	THETA = list(product(theta1s, repeat=2*(Number_of_Modes)))

	ALLSAMPLE = np.array(list(product(dwdvals,THETA)),dtype=list)

	return ALLSAMPLE

def generate_model_file(mdl, dtfile, output_dir):
	"""Summary
	
	Args:
	    mdl (TYPE): Description
	    dtfile (TYPE): Description
	    output_dir (TYPE): Description
	
	Returns:
	    TYPE: Description
	"""
	Xcoord,Ycoord,Zcoords,center,[Xmin,Xmax],[Ymin,Ymax], IterIdxs, XlinkIdxs = get_all_atoms(mdl)

	Dmdl1=DiscTransformation()

	#Build Disctransformation model and score
	#FILE content as input

	from numpy import mean

	discs,bdm,score_obj=Dmdl1.main(['',0,dtfile],[Xcoord,Ycoord,Zcoords,[mean(Xcoord),mean(Ycoord)]])

	if not os.path.exists(os.path.dirname(bdm.get_arguments()['@ARG7'])):
		print("Incorrect path for @ARG7")
		sys.exit()
	
	dtoname = os.path.basename(bdm.get_arguments()['@ARG7']).split('.')[0]
	
	for k,d in enumerate(discs):
		
		mdl_new = copy.deepcopy(mdl)

		Isites1 = d.Get_InteractingSites()

		for i in IterIdxs:
			mdl_new.set_x(i, Isites1[0][i] )
			mdl_new.set_y(i, Isites1[1][i] )
			mdl_new.set_z(i, Isites1[2][i] )

		mdl_new.write(os.path.join(output_dir,dtoname+'_disc_'+str(k)+'.pdb'))
		del mdl_new

	Dmdl1.print_model(discs,bdm,score_obj)

	del discs
	del bdm
	del score_obj

	return

def generate_pdb_model(mdl, dtmdl_params, discs, output_dir, counter):
	"""Summary
	
	Args:
	    mdl (TYPE): Description
	    dtmdl_params (TYPE): Description
	    discs (TYPE): Description
	    output_dir (TYPE): Description
	    counter (TYPE): Description
	
	Returns:
	    TYPE: Description
	"""
	#Xcoord,Ycoord,Zcoords,center,[Xmin,Xmax],[Ymin,Ymax], IterIdxs, XlinkIdxs = get_all_atoms(mdl)
	#Xcoord,Ycoord,Zcoords,center,[Xmin,Xmax],[Ymin,Ymax], IterIdxs, XlinkIdxs = get_all_CA_atoms(mdl)
	Xcoord,Ycoord,Zcoords,center,[Xmin,Xmax],[Ymin,Ymax], IterIdxs, XlinkIdxs = get_all_interacting_atoms(mdl)

	if not os.path.exists(os.path.dirname(dtmdl_params.get_arguments()['@ARG7'])):
		print("Incorrect path for @ARG7")
		sys.exit()
	
	dtoname = os.path.basename(dtmdl_params.get_arguments()['@ARG7']).split('.')[0]

	for k,d in enumerate(discs):

		mdl_new = copy.deepcopy(mdl)

		Isites1 = d.Get_InteractingSites()

		for i in IterIdxs:
			mdl_new.set_x(i, Isites1[0][i] )
			mdl_new.set_y(i, Isites1[1][i] )
			mdl_new.set_z(i, Isites1[2][i] )

		#output_file = os.path.join(output_dir,"Disc_Mdl_"+str(counter)+"Disc_"+str(k)+".pdb")
		output_file = os.path.join(output_dir,dtoname+'_'+str(counter)+'_disc_'+str(k)+'.pdb')
		
		
		#Write only CA atoms
		mdl_new.write(output_file)

	return

def generate_pdb_CAmodel(mdl, dtmdl_params, discs, output_dir, counter):
	"""Summary
	
	Args:
	    mdl (TYPE): Description
	    dtmdl_params (TYPE): Description
	    discs (TYPE): Description
	    output_dir (TYPE): Description
	    counter (TYPE): Description
	
	Returns:
	    TYPE: Description
	"""
	#Xcoord,Ycoord,Zcoords,center,[Xmin,Xmax],[Ymin,Ymax], IterIdxs, XlinkIdxs = get_all_atoms(mdl)
	#Xcoord,Ycoord,Zcoords,center,[Xmin,Xmax],[Ymin,Ymax], IterIdxs, XlinkIdxs = get_all_CA_atoms(mdl)
	Xcoord,Ycoord,Zcoords,center,[Xmin,Xmax],[Ymin,Ymax], IterIdxs, XlinkIdxs = get_all_interacting_atoms(mdl)

	if not os.path.exists(os.path.dirname(dtmdl_params.get_arguments()['@ARG7'])):
		print("Incorrect path for @ARG7")
		sys.exit()
	
	dtoname = os.path.basename(dtmdl_params.get_arguments()['@ARG7']).split('.')[0]

	for k,d in enumerate(discs):

		mdl_new = copy.deepcopy(mdl)

		Isites1 = d.Get_InteractingSites()

		for i in IterIdxs:
			mdl_new.set_x(i, Isites1[0][i] )
			mdl_new.set_y(i, Isites1[1][i] )
			mdl_new.set_z(i, Isites1[2][i] )

		#output_file = os.path.join(output_dir,"Disc_Mdl_"+str(counter)+"Disc_"+str(k)+".pdb")
		output_file = os.path.join(output_dir,dtoname+'_'+str(counter)+'_disc_'+str(k)+'.pdb')
		
		#Write only CA atoms
		#mdl_new.write(output_file)
		mdl_new.writeCA(output_file,skip_res='DTA')

	return

def write_dtsampling_input_file(file_str,dtmdl_params, output_dir, counter):
	"""Summary
	
	Args:
	    file_str (TYPE): Description
	    dtmdl_params (TYPE): Description
	    output_dir (TYPE): Description
	    counter (TYPE): Description
	
	Returns:
	    TYPE: Description
	"""
	if not os.path.exists(os.path.dirname(dtmdl_params.get_arguments()['@ARG7'])):
		print("Incorrect path for @ARG7")
		sys.exit()
	
	dtoname = os.path.basename(dtmdl_params.get_arguments()['@ARG7']).split('.')[0]

	#dtifname = os.path.join(output_dir,"Disc_Mdl_"+str(counter)+".dat")
	dtifname = os.path.join(output_dir,dtoname+'_'+str(counter)+'.dat')
	
	inf = open(dtifname,'w')
	inf.writelines(file_str)
	inf.close()

	return

def write_samplespace(Sample_PARAMs, output_dir, swlines):
	"""Summary
	
	Args:
	    Sample_PARAMs (TYPE): Description
	    output_dir (TYPE): Description
	    swlines (TYPE): Description
	
	Returns:
	    TYPE: Description
	"""
	outf = open(os.path.join(output_dir,'SampleSpaceList.txt'),'w')
	outf.writelines(swlines)
	outf.close()
	
	return

def generate_ensemble_inputparams(mdl, dtmdl_params, DiscRad):
	"""Summary
	
	Args:
	    mdl (TYPE): Description
	    dtmdl_params (TYPE): Description
	    DiscRad (TYPE): Description
	
	Returns:
	    TYPE: Description
	"""
	arg1 = int(dtmdl_params.get_arguments()['@ARG1'])

	#Radius of the disc
	arg2 = int(dtmdl_params.get_arguments()['@ARG2'])
	
	if arg2==0:
		arg2 = DiscRad
	
	arg4 = dtmdl_params.get_arguments()['@ARG4']
	
	#Get adjacency matrix
	arg6_temp = dtmdl_params.get_arguments()['@ARG6']
	adj_lines="";
	for row in arg6_temp:
		adj_lines+=''.join(row)+"\n";
	adj_lines.strip()
	arg6 = adj_lines


	DTEnSemParam = {'arg1':arg1,'arg2':arg2,'arg4':arg4,'arg6':arg6}

	return DTEnSemParam

def generate_ensemble(mdl, output_dir, dtmdl_params):
	"""Summary
	
	Args:
	    mdl (TYPE): Description
	    output_dir (TYPE): Description
	    dtmdl_params (TYPE): Description
	
	Returns:
	    TYPE: Description
	"""
	#Get the disc coordinates from the model. And extimate the radius
	#Xcoord,Ycoord,Zcoords,center,[Xmin,Xmax],[Ymin,Ymax], IterIdxs, XlinkIdxs = get_interacting_atoms(mdl)
	
	Xcoord,Ycoord,Zcoords,center,[Xmin,Xmax],[Ymin,Ymax], IterIdxs, XlinkIdxs = get_all_atoms(mdl)

	DiscRad = int((max(Xmax - Xmin, Ymax - Ymin) + 2.0)/2.0 )	

	DTEnSemParam = generate_ensemble_inputparams(mdl, dtmdl_params, DiscRad)

	#Get parameters for sampling; 
	#Maximum overlap between the two connecting discs; Disc radius * overlap fraction
	overlapRad = DTEnSemParam['arg2']*float(dtmdl_params.get_arguments()['@ARG11'])

	theta_step = float(dtmdl_params.get_arguments()['@ARG12'])

	dwd_step = float(dtmdl_params.get_arguments()['@ARG13'])

	#Mode Names
	unique_modes = sorted(list(set([c for c in DTEnSemParam['arg6'] if c.isalpha()])))

	dtoname = os.path.basename(dtmdl_params.get_arguments()['@ARG7']).split('.')[0]

	#Number_of_Discs=int(dtmdl_params.get_arguments()['@ARG1']);
	Number_of_Modes=len(unique_modes);

	#this list can increase but in practical problems this cannot exceed given the sampling times
	ModeName = {i:unique_modes[i] for i in range(0,Number_of_Modes)}

	#Get all the sample that need to be scored
	#Get all theta1 and theta2 in pairs between (0,2pi).
	Sample_PARAMs = get_full_sample_space(Number_of_Modes,theta_step,overlapRad,dwd_step);

	swlines ="\n# Disc Radius:"+str(DTEnSemParam['arg2'])+"\n"
	swlines+="# Starting Overalap Distance:"+str(round(overlapRad,2))+"\n"
	swlines+="# Distance step (till Discs dont overlap):"+str(dwd_step)+"\n"
	swlines+="# Angle Step:"+str(theta_step)+"\n"
	swlines+="# Total Sample Space:"+str(Sample_PARAMs.shape[0])+"\n"
	print(swlines)
	swlines+= "\n\n#Overlap_Dist Theta1   Theta2    Modes->\n"

	###########################
	# Write SampleSpace in File before sampling
	# Iterate over sample. This could be exhaustive or scoring based, say Monte Carlo
	for counter, [dwdisc, (angles)] in enumerate(Sample_PARAMs):
		#generate Input parameters for Exhaustive Enumeration
		Mi=''
		for i in range(0,Number_of_Modes):
			parallel_disc=1; #Set parallel_disc=0 for anti-parallel disc
			ModeVal = ModeName[i]+':'+str(angles[2*i+0])+':'+str(angles[2*i+1])+':'+str(parallel_disc)+':0'
			Mi+= ModeVal.rjust(20)+' '
		
		swlines += str(round(dwdisc,2)).rjust(8)+" "+str(round(angles[0],1)).rjust(8)+" "+str(round(angles[1],1)).rjust(8)+" "
		swlines+=Mi+'\n'
	write_samplespace(Sample_PARAMs, output_dir, swlines)
	############################

	#Start Sampling...
	
	max_cc_score=-1; max_counter=-1; max_mode = "";
	cc_atoms_keys = None
	max_score_fstr = ""

	#Iterate over sample. This could be exhaustive or scoring based, say Monte Carlo
	for counter, [dwdisc, (angles)] in enumerate(Sample_PARAMs):

		#generate Input parameters for Exhaustive Enumeration
		Mi=''
		for i in range(0,Number_of_Modes):

			parallel_disc=1; #Set parallel_disc=0 for anti-parallel disc
			Mi+=ModeName[i]+':'+str(angles[2*i+0])+':'+str(angles[2*i+1])+':'+str(parallel_disc)+':0'+' '

			#print(Mi)

		arg1=DTEnSemParam['arg1']
		arg2=DTEnSemParam['arg2']
		arg3=dwdisc;
		arg5=Mi
		arg4=DTEnSemParam['arg4'];
		arg6=DTEnSemParam['arg6'];
		#arg7 = str(os.path.join(output_dir,"Disc_Mdl_"+str(counter)+".ps"))
		arg7 = str(os.path.join(output_dir,dtoname+'_'+str(counter)+'.ps'))
		arg8=arg2*2; #max distance: Twice the radius when two disc are touching each other
		arg9=arg2*2; #min distance for clash: Twice the radius when two disc are touching each other. Hard clash!
		arg10=counter

		#Get file string
		file_str = get_input_fstr(arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9,arg10)

		print("\nGenerating Mode:",Mi)
		Dmdl=DiscTransformation()
		
		if dtmdl_params.get_arguments()['@ARG15']=='yes':

			discs,bdm,score_obj=Dmdl.main(['',1,file_str],[Xcoord,Ycoord,Zcoords,[np.mean(Xcoord),np.mean(Ycoord)]])
			
			print("Writing pdb model..")
			#generate_pdb_model(mdl, dtmdl_params, discs, output_dir, counter)
			generate_pdb_CAmodel(mdl, dtmdl_params, discs, output_dir, counter)
		
		else:
			discs,bdm,score_obj=Dmdl.main(['',1,file_str],[Xcoord,Ycoord,Zcoords,center])

		
		if dtmdl_params.get_arguments()['@ARG14']=='yes':

			print("Writing DT model..")
			Dmdl.print_model(discs,bdm,score_obj)
		
		
		if dtmdl_params.get_arguments()['@ARG16']=='yes':

			print("Writing DT model input files..")
			write_dtsampling_input_file(file_str, dtmdl_params, output_dir, counter)


		#SCORING FUNCTIONS CAN BE ADDED HERE. SEE SCORE_MODEL CLASS
		#score_obj.get_cc_pairing(mdl, IterIdxs, discs)
		#score_obj.get_xlink_score(mdl, IterIdxs, discs, XlinkIdxs)

		#cc_score = score_obj.get_cc_score()
		#atomclashes =  score_obj.get_atomclash()
		#xlinkscore =  score_obj.get_xlinkscore()
		
		#if xlinkscore!=0:
		#	print("Mode",Mi,"DDist:",dwdisc,"Counter:",counter,len(cc_score.keys()),len(atomclashes.keys()),xlinkscore)

		#if max_cc_score < len(cc_score.keys()):
		#	max_cc_score = len(cc_score.keys())
		#	max_counter = counter
		#	max_mode = Mi
		#	cc_atoms_keys = cc_score
		#	max_score_fstr = file_str

		
		#del Dmdl
		#del bdm
		#del score_obj
		#del discs
		
	#print("Best CC:")
	#print(max_cc_score, max_counter, max_mode)
	#print(cc_atoms_keys)

	#generate_model(mdl,file_str, output_dir)
	

	return

#Called by Example_single_run
def generate_single_configuration(dt_ifile):
	"""Summary
	
	Args:
	    dt_ifile (TYPE): Description
	
	Returns:
	    TYPE: Description
	"""
	if not validate_paths(dt_ifile):
		print("Incorrect Input file!")
		sys.exit()

	Dmdl=DiscTransformation()
		
	#discs,bdm,score_obj=Dmdl.main(['',1,file_str],[Xcoord,Ycoord,Zcoords,center])
	discs,bdm,score_obj=Dmdl.main(['',0,dt_ifile])

	Dmdl.print_model(discs,bdm,score_obj)

	return

#Called by Example_single_run_withpdb
def generate_single_configuration_withpdb(dt_ifile, input_pdb, output_dir):
	"""Summary
	
	Args:
	    dt_ifile (TYPE): Description
	    input_pdb (TYPE): Description
	    output_dir (TYPE): Description
	
	Returns:
	    TYPE: Description
	"""
	if not (validate_paths(dt_ifile) & validate_paths(input_pdb) & validate_paths(output_dir)):
		print("Incorrect Path/Input file!")
		sys.exit()

	inputfname = Path(input_pdb).name
	outputfile = os.path.join(output_dir,inputfname[:-4]+'_z.pdb')
	alignaxis = 'z'
	chain=['ALL']

	from align_axis.main import align
	mdl, __ = align(input_pdb, outputfile, alignaxis, chain)

	from transform.DTransform import GetDiscRepresentation, GetDiscRepresentation_nthCA
	N=1 #Every 4th CA
	mdl = GetDiscRepresentation_nthCA(mdl,N)

	outputfile2 = os.path.join(output_dir,inputfname[:-4]+'_projz.pdb')
	mdl.write(outputfile2)

	generate_model_file(mdl, dt_ifile, output_dir)

	return

#Called by Example_sampling_run
def generate_ensemble_configurations(dt_ifile, input_pdb, output_dir):
	"""Summary
	
	Args:
	    dt_ifile (TYPE): Description
	    input_pdb (TYPE): Description
	    output_dir (TYPE): Description
	
	Returns:
	    TYPE: Description
	"""
	if not (validate_paths(dt_ifile) & validate_paths(input_pdb) & validate_paths(output_dir)):
		print("Incorrect Path/Input file!")
		sys.exit()

	inputfname = Path(input_pdb).name
	outputfile = os.path.join(output_dir,inputfname[:-4]+'_z.pdb')
	alignaxis = 'z'
	chain = ['ALL']

	from align_axis.main import align
	mdl, __ = align(input_pdb, outputfile, alignaxis, chain)

	from transform.DTransform import GetDiscRepresentation, GetDiscRepresentation_nthCA
	N=1 #Every 4th CA
	mdl = GetDiscRepresentation_nthCA(mdl,N)

	outputfile2 = os.path.join(output_dir,inputfname[:-4]+'_projz.pdb')
	mdl.write(outputfile2)

	#TODO: Add all parameters needed for the sampling from this inputfile
	from core.Build_Disc_Model import Build_Disc_Model
	from core.Disc_Model_Parameters import Disc_Model_Parameters
	
	#Read Disc Model parameters
	dtmdl_params = Disc_Model_Parameters(dt_ifile)

	generate_ensemble(mdl, output_dir, dtmdl_params)
	
	return



