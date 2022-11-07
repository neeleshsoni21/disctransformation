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

from main import align
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
#from numpy.fft import fft2, ifft2
#from scipy.fft import rfft, rfftfreq, irfft #R ones are faster ffts of scipy. regular ones are also available
from scipy.fft import fft, fftfreq, ifft, fftn, ifftn
from scipy.signal import find_peaks

def avg_zstep_distance(CoordsZ):
	"""Summary
	
	Args:
	    CoordsZ (TYPE): Description
	
	Returns:
	    TYPE: Description
	"""
	Zsteps = np.diff(CoordsZ)
	
	return np.mean(Zsteps),np.std(Zsteps)

def fourier_transform(mdl, coord_A_iter):
	"""Summary
	
	Args:
	    mdl (TYPE): Description
	    coord_A_iter (TYPE): Description
	
	Returns:
	    TYPE: Description
	"""
	CoordsALL=[]
	AtomStep = ['N','C','CA','O']
	AtomStep = ['CA']
	AtomStepSize = len(AtomStep)
	residuecutoff = 1; #Consider the super coiled helix pitch

	for i in coord_A_iter:

		#Get backbone coordinates
		if mdl.name()[i] in AtomStep:
		#if mdl.name()[i] in ['CA']:
			CoordsALL.append([mdl.x()[i], mdl.y()[i], mdl.z()[i]])

	CoordsALL = np.array(CoordsALL)

	iterat=0;print("Shape:",CoordsALL.shape[0]);
	iterstep=CoordsALL.shape[0] #For complete length
	#iterstep = 14 # For sliding window subset
	while iterat < CoordsALL.shape[0]:

		Coords = CoordsALL[iterat:iterat+iterstep,:]
		iterat+=iterstep;
		print(iterat,Coords.shape)

		avgzstep,avgzstepstd = avg_zstep_distance(Coords[:,2])
		print("Average Z step",avgzstep,"+-",avgzstepstd)

		#Coords_dim = 2 #2 is for z, 1 is for y, 0 is for x
		fftvalX = fft(Coords[:,0])
		fftvalY = fft(Coords[:,1])

		#fftval = fftn(Coords[:,1:])
		#fftvalX = fftval[:,0]
		#fftvalY = fftval[:,1]
		print("Shape of coords",Coords[:,0:2].shape)
		

		#power_x = (np.abs(fftvalX)**2)
		power_x = (np.abs(fftvalX)**2)
		sample_freq_x = fftfreq(fftvalX.size)

		power_y = (np.abs(fftvalY)**2)
		sample_freq_y = fftfreq(fftvalY.size)
		
		#fig = plt.figure()
		fig,ax = plt.subplots(2,3)

		#ax = [fig.add_subplot(1, 2, 1, projection='3d')]
		ax[0,0].plot(Coords[:,0],label="x coords")
		ax[0,0].legend()
		ax[1,0].plot(Coords[:,1],label="y coords")
		ax[1,0].legend()
		
		# Find the peak frequency: we can focus on only the positive frequencies
		# Positive axis frequencies
		pos_mask_x = np.where(sample_freq_x > 0)
		freqsX = sample_freq_x[pos_mask_x]
		powerX = power_x[pos_mask_x]
		peaksX, _X = find_peaks(powerX,distance=residuecutoff*AtomStepSize)
		

		ax[0,1].plot(freqsX,np.log(powerX),label="log power (x)")
		ax[0,1].plot(freqsX[peaksX], np.log(powerX[peaksX]), "x",label="peaks")
		ax[0,1].set_xlabel("Frequency (+ive only)")
		ax[0,1].set_ylabel("Log Power: abs(fft_sig)**2")
		ax[0,1].legend()

		# Positive axis frequencies
		pos_mask_y = np.where(sample_freq_y > 0)
		freqsY = sample_freq_y[pos_mask_y]
		powerY = power_y[pos_mask_y]
		peaksY, _Y = find_peaks(powerY,distance=residuecutoff*AtomStepSize)

		#ax[1,1].plot(freqsX,np.log(powerX),label="log power (y)")
		ax[1,1].plot(freqsY,np.log(powerY),label="log power (y)")
		ax[1,1].plot(freqsY[peaksY], np.log(powerY[peaksY]), "x",label="peaks")
		
		ax[1,1].set_xlabel("Frequency (+ive only)")
		ax[1,1].set_ylabel("Log Power: abs(fft_sig)**2")
		ax[1,1].legend()

		n=2
		topnidxX = (-powerX[peaksX]).argsort()[:n]
		peak_freq_x = freqsX[peaksX][topnidxX]
		peak_power_x = powerX[peaksX][topnidxX]

		n=2
		topnidxY = (-powerY[peaksY]).argsort()[:n]
		peak_freq_y = freqsY[peaksY][topnidxY]
		peak_power_y = powerY[peaksY][topnidxY]

		#peak_freq = freqs[power[pos_mask].argmax()]
		print("Peak-power x Freq:",peak_freq_x, np.log(peak_power_x))
		print("Peak-power y Freq:",peak_freq_y, np.log(peak_power_y))

		#print("\nNumber of Turns / atom (data point or CA)", peak_freq_y)
		XPitchRes = (1.0/peak_freq_x)/AtomStepSize
		YPitchRes = (1.0/peak_freq_y)/AtomStepSize
		print("\nNumber of residues / Turn", XPitchRes)
		print("Number of residue / Turn", YPitchRes)

		print("\nDistance / Turn", XPitchRes*avgzstep,"+-",XPitchRes*avgzstepstd)
		print("Distance / Turn", YPitchRes*avgzstep,"+-",YPitchRes*avgzstepstd)

		
		##########################################################
		ax[0,2].plot(Coords[:,0],label="x coords")
		#0th is the highest power. reverse plotting is done so the big frequency is on the top of the plot
		for idx in range(0,len(peak_freq_x)):
			
			freq1_fft = fftvalX.copy()
			freq1_fft[np.abs(sample_freq_x) > peak_freq_x[len(peak_freq_x)-idx-1]] = 0
			filtered_sig_freq1 = ifft(freq1_fft).real #+ np.log(peak_power_x[len(peak_freq_x)-idx-1])
			ax[0,2].plot(filtered_sig_freq1,label="filtered sig freq: power "+str(len(peak_freq_x)-idx-1))
		
		ax[0,2].legend()

		ax[1,2].plot(Coords[:,1],label="y coords")
		for idx in range(0,len(peak_freq_y)):


			freq1_fft = fftvalY.copy()
			freq1_fft[np.abs(sample_freq_y) > peak_freq_y[len(peak_freq_y)-idx-1]] = 0
			filtered_sig_freq1 = ifft(freq1_fft).real

			ax[1,2].plot(filtered_sig_freq1,label="filtered sig freq: power "+str(len(peak_freq_y)-idx-1))
		
		ax[1,2].legend()
		
		plt.show()

	return


if __name__ == '__main__':
	import sys

	inputfile, outputfile, alignaxis = sys.argv[1], sys.argv[2], sys.argv[3]

	chain = ['A']
	chain = ['ALL']
	mdl, coord_A_iter = align(inputfile, outputfile, alignaxis, chain)

	fourier_transform(mdl,coord_A_iter)