#call as:
#python ../thermalrates.py 300

#import Element
import math
import sys
import numpy as np
import matplotlib.pyplot as plt
import pylab as plb
from scipy.optimize import curve_fit
from scipy import asarray as ar,exp

temperature=  float(sys.argv[1])		# temperature for thermalisation
data = np.genfromtxt('rad_rate_sorted.txt', delimiter=',') 
energy = data[:,0] #in eV
rate = data[:,1] #in 1/s

#thermalised rate is given by <k>={sum[k.exp(-energy/kT)]}/{sum[exp(-energy/kT)]}

kt=0.00008617*temperature #in eVs
nn=0
sum1=0
sum2=0

for nn in range(len(energy)):
    sum1=sum1+rate[nn]*np.exp(-energy[nn]/kt)
    sum2=sum2+np.exp(-energy[nn]/kt)
     
thermalized_rate=sum1/sum2
print('at T=',temperature,' kT=',kt,' [eV] and thermalized rate is ',thermalized_rate,' [1/s]')






