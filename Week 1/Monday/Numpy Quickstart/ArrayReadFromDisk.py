# HDF5: h5py
# FITS: Astropy

import numpy as np

data = np.loadtxt('simple.csv', delimiter=',', skiprows = 1)  # Load a simple CSV file
print(data)