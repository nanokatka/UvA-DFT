#call as:
#python ../thermal_rates_allT.py

#import Element
import math
import sys
import numpy as np
import matplotlib.pyplot as plt
import pylab as plb
from scipy.optimize import curve_fit
from scipy import asarray as ar,exp

data = np.genfromtxt('rad_rate_sorted.txt', delimiter=',') 
energy = data[:,0] #in eV
rate = data[:,1] #in 1/s

#thermalised rate is given by <k>={sum[k.exp(-energy/kT)]}/{sum[exp(-energy/kT)]}

nn=0
sum1=0
sum2=0
temp=50
therm_file = []
temp_file = []

for ii in range(27):
    for nn in range(len(energy)):
        kt=0.00008617*temp
        sum1=sum1+rate[nn]*np.exp(-energy[nn]/kt)
        sum2=sum2+np.exp(-energy[nn]/kt)
    therm_rate=sum1/sum2
    print('at T=',temp,' kT=',kt,' [eV] and thermalized rate is ',therm_rate,' [1/s]')
    therm_file.append(therm_rate)
    temp_file.append(temp)
    temp=50+10*ii

temp_rate_all = np.column_stack((temp_file,therm_file))    #temperature and thermalized rate 
np.savetxt('thermalized_rates_allT.txt',temp_rate_all)





