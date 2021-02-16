import numpy as np
from . import atomicUtils as au

# use:    python print_all_bonds.py ./SiQD.xyz

#fin          =     sys.argv[1]
fin = 'SiQD.xyz'
atoms  = np.genfromtxt  ( fin , skip_header=1 )
bonds,bondVecs = au.findAllBonds( atoms, Rcut=3.0, RvdwCut=0.8 )
