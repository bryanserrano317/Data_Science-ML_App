# Gaussian_distribution.py
#
# SAXS data modeling script for spherical micelles. 
#
# This script returns a scattering intensity function as a line of best fit
# for experimental data. It uses a gaussian distribution to estimate values.
#
# Check the readme file or Jupyter Notebook for more information.

# Import libraries handeling excel reads and modeling calculations.

import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
from scipy.integrate import quad
from scipy.stats import norm

# Import the necessary excel spreadsheets.
scatteringfunction = pd.read_csv('gaussianvalues.csv')
workbook = xlrd.open_workbook('sample_data.xlsx')

worksheet = workbook.sheet_by_index(0)

# Read in all q and r values from excel spreadsheet.
spreadsheet = [[worksheet.cell_value(i,j) for i in range (1, worksheet.nrows)]
                                          for j in range (0,3)]

# Declare spherical micelle parameters 
Volume_Fraction = 0.01
Ravg = 60 * (10 ** -8)
polydispersity = 0.2
SLD_sphere = 10.64 * (10 ** 10)
SLD_solvent = 9.42 * (10 ** 10)
deltaRho = SLD_sphere - SLD_solvent
sigma = polydispersity*Ravg
R = norm.rvs(loc = Ravg, scale = sigma, size = 2000, random_state = 3)
bkg = 0.001


# Return estimate for spherical micelle radius using gaussian distribution
# with polydispersity, R, and Ravg as variables.
def gaussianDistribution(R, Ravg, sigma):
    return norm.pdf(R, loc = Ravg, scale = sigma)
    
# Return scattering amplitude for a sphere using q and R.
def scatteringAmplitude(q, R):
    return (3 * (math.sin(q * R)-(q * R) * math.cos(q * R))) / ((q * R) ** 3)
    

# Return integral equation component from scattering intensity equation.
def integrand(q, R):
    return gaussianDistribution(R, Ravg, sigma) * (R ** 6) * (scatteringAmplitude(q, R)) ** 2

# Calculate the integral for each q and R value and multiply constant 
# values to integral value.
def scatteringFunction(Volume_Fraction, deltaRho, sigma, R, Ravg):
    
    for i in range (1, worksheet.nrows):
        for j in range (0, 1):
            q = spreadsheet[0][i - 1] * (10 ** -8)
            integral = [quad(integrand, 0, np.inf, args = (q))] 
            #print(integral)
            qScatteringFunction = ((((4 * math.pi)/3) ** 2) * Volume_Fraction * (deltaRho ** 2)) * (integral[0][0])
            print(qScatteringFunction)
            
    print("\nUpdate gaussianvalues.csv with the new values if needed.\n")

# Plot two sets of miscelle data in a scatterplot. 
def plotSphericalMicellesFit():
    gaussianVals = pd.read_csv('gaussianvaluesfit.csv')
    plt.subplot(111)
    plt.scatter(gaussianVals.x, gaussianVals.y, s = 0.1, c = 'red')
    plt.xlim(0.001, 1)
    plt.ylim(1 * 10 ** -10, 10000)
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True)

# Plot two sets of miscelle data in a histogram. 
def plotGaussianDistribution(R, Ravg, sigma):
    
    # Plot line of best fit for R value distribution.
    x = np.linspace(0.1 * (10 ** -7), (1.1) * (10 ** -6), 500)
    fig, ax = plt.subplots(figsize = (16, 6))
    ax.plot(x, norm.pdf(x, loc = Ravg, scale = sigma), lw = 5)
    
    # Plot histogram to show R value distribution.
    ax.hist(R, bins = 1000, density = True)
    
    plt.show()
    
    # Display parameter values.
    print("Parameters:")
    print("\nmean (Ravg):", norm.mean(Ravg, sigma))
    print("median (Ravg):", norm.median(Ravg, sigma))
    print("var:", norm.var(Ravg, sigma))
    print("std (Sigma):", norm.std(Ravg, sigma))
    print("\n")
        
scatteringFunction(Volume_Fraction, deltaRho, sigma, R, Ravg)

plotSphericalMicellesFit()
plotGaussianDistribution(R, Ravg, sigma)




