# Analysis for spherical micelles with a spherical Gaussian 
# Distribution

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import scipy.integrate as integrate

# Helper function to plot spherical micelles.
def plotSphericalMicelles(data):
    plt.subplot(111)
    plt.scatter(sample_data.q, sample_data.s, s = 0.1, c = 'red')
    plt.xlim(0.001, 1)
    plt.ylim(0.0000001, 10)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('q($Å^{-1}$)', fontsize = 12)
    plt.ylabel('Intensity', fontsize = 12)
    plt.grid(True)

sample_data = pd.read_csv('sample_data.csv')
workbook = xlrd.open_workbook('sample_data.xlsx')
    
worksheet = workbook.sheet_by_index(0)

# Contains all q,r,s values in individual lists.
twod_list = [[worksheet.cell_value(i,j) for i in range (1, worksheet.nrows)] for j in range (0,3)]

# Prints q,r,s values from excel shees
# for the first array, 0 = q, 1 = r, 2 = s.
print(twod_list[0][0])

plotSphericalMicelles(sample_data)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#def sphericalMicelles():
              
#scatteringFunction(worksheet.cell_value(i,j))

#def scatteringFunction(value):
# modeling functions


# gaussianValue = 0;
#   Normalized Gaussian Distribution
#       f(x) = 1/(std-dev*(sqrt(2*pi)))*exp^(-1/2*((x-mean)/std_dev)^2)

#   form factor 
#       V = 4*pi/3*(R^3) // not needed yet

#   p (polydispersity) page 39/220 // not needed yet
#       (std-dev)/Ravg


#   from 200 page pdf -> Scattering function
#       I(q) = ((4pi/3)^2)*N*(p^2)*(integral(0,inf)*f(R)*R^6*F^2^(qR)dR)


# N = scaling factor
# delta p^2 = difference in scattering length density.
# f(R) = gaussian distribution 
# R = ? (need to find)
# F = scattering amplitude for a sphere


#   read-in inputs from excel sheet 
#   for loop to get each q value 
#   toggles for code blocks for python 

#readSheet(workbook)
#plt.show()




