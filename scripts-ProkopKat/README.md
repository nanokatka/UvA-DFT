# DFT
DFT scripts

Code written by vast majority by Prokop Hapala for processing DFT cp2k output files (gemoetry .xyz, cp2k output log file .out and molecular orbitals file .MoLog). Scripts require virtual environment qmworks, developed at VU, Amsterdam (https://github.com/SCM-NV/qmflows). It might need to be installed by "pip install git+https://github.com/SCM-NV/qmflows@master#egg=qmflows". Qmworks is mostly used to load properly the wavefunctions coefficients from the MoLog file. 

The processing order is:

******************
	. activate qmworks
	python ../kspace_density_off_GX.py
	python ../kspace_density_off_GL-invert.py
	python ../plot_klinesGX.py
	python ../plot_klinesGL.py
	python ../dipoleTrans_grid_Kat.py
	python ../plotStuff_Kat.py
	x2b relaxed.xyz answer.bas
	python ../bas2bondlength_Kat2.py 0.2
	python ../plot_dos.py -emin -6.0 -emax 2.0
	python ../charge.py cp2k.out 
	source deactivate
*****************

Rest of the scripts are for other types of processing that are not done routinely and hence can be neglected.
