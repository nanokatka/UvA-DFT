#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import *
from numpy import *

data = np.genfromtxt('rad_rate_sorted.txt', delimiter=',') 

energy = data[:,0]
print(energy)
rate = data[:,1]
kt = 0.020  #kT=20meV 
homo_energy = data[0,0]
homo_rate = data[0,1]
homo_rates = []
counts = 0

for item in energy:
    if item < (homo_energy + kt):
        homo_rates.append(rate[counts])
        counts = counts +1
    else:
        break

cummulative_rate = 0
for rates in range(len(homo_rates)):
    cummulative_rate = cummulative_rate + rates

final_rate = cummulative_rate/counts
    
np.savetxt('homo_lumo_rate.txt', final_rate)
