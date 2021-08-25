# Log-normal_distribution.py
#
# SAXS data modeling script for spherical micelles. 
#
# This script returns a scattering intensity function as a line of best fit
# for experimental data. It uses a log-normal distribution to estimate values.
#
# Check the readme file or Jupyter Notebook for more information.

# Import libraries handeling excel reads and modeling calculations.

import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
from scipy.integrate import quad
from scipy.stats import lognorm

# Import the necessary excel spreadsheets
scatteringfunction = pd.read_csv('lognormalvalues.csv')
workbook = xlrd.open_workbook('sample_data.xlsx')

worksheet = workbook.sheet_by_index(0)

# Read in all q and r values from excel spreadsheet
spreadsheet = [[worksheet.cell_value(i,j) for i in range (1, worksheet.nrows)]
                                          for j in range (0,3)]

# Declare spherical micelle parameters 
Volume_Fraction = 0.01
Rmed = 60 * (10 ** -8)
polydispersity = 0.2
SLD_sphere = 10.64 * (10 ** 10)
SLD_solvent = 9.42 * (10 ** 10)
deltaRho = SLD_sphere - SLD_solvent
sigma = polydispersity * Rmed
R = lognorm.rvs(s = sigma, loc = Rmed, scale = math.exp(np.log(Rmed)), size = 2000, random_state = 3 )
bkg = 0.001

# Return estimate for spherical micelle radius using gaussian distribution
# with polydispersity, R, and Ravg as variables.
def logNormalDistribution(sigma, R, Rmed):
    return (1 / ((sigma) * R * math.sqrt(2 * math.pi))) * math.exp((-1 / (2 * (sigma ** 2))) * (np.log(R) - np.log(Rmed)) ** 2)

# Return scattering amplitude for a sphere using q and R.
def scatteringAmplitude(q, R):
    return (3 * (math.sin(q * R)-(q * R) * math.cos(q * R))) / ((q * R) ** 3)

# Return integral equation component from scattering intensity equation.
def integrand(q, R):
    return logNormalDistribution(sigma, R, Rmed) * (R ** 6) * (scatteringAmplitude(q, R)) ** 2

# Calculate the integral for each q and R value and multiply constant 
# values to integral value.
def scatteringFunction(Volume_Fraction, deltaRho, sigma, R, Rmed):

    for i in range (1, worksheet.nrows):
        for j in range (0,1):
            q = spreadsheet[0][i - 1] * (10 ** -8)
            #print(q)
            integral = [quad(integrand, 0, np.inf, args = (q))] 
            #print(integral[0][0])
            qScatteringFunction = ((((4 * math.pi) / 3) ** 2) * Volume_Fraction * (deltaRho ** 2)) * (integral[0][0])
            print(qScatteringFunction)
            
    print("\nUpdate lognormalvalues.csv with the new values if needed.\n")


# Plot two sets of miscelle data in a scatterplot. 
def plotSphericalMicelles():
    logNormVals = pd.read_csv('logNormalValues.csv')
    plt.subplot(111)
    plt.scatter(logNormVals.x, logNormVals.y, s = 0.9, c = 'red')
    plt.xlim(0.001, 10)
    plt.ylim(1 * 10 ** -10, 1)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('q ($Å^{-1}$)', fontsize = 12)
    plt.ylabel('Intensity ($cm^{-1}$)', fontsize = 12)
    plt.grid(True)

# Plot two sets of miscelle data in a histogram. 
def plotLogNormalDistribution(R, sigma):
    
    # Plot line of best fit for R value distribution.
    x = np.linspace(lognorm.ppf(0.01, sigma), lognorm.ppf(0.99, sigma), 1000)
    fig, ax = plt.subplots(figsize = (16, 6))
    rv = lognorm(sigma)
    ax.plot(x, rv.pdf(x))
    
    # Plot histogram to show R value distribution.
    r = lognorm.rvs(sigma, size = 1000)
    ax.hist(r, bins = 275, density = True)

    plt.show()
    
    # Display parameter values.
    print("Parameters:")
    print("\nmean (Ravg):", lognorm.mean(Rmed, sigma))
    print("median (Ravg):", lognorm.median(Rmed, sigma))
    print("var:", lognorm.var(Rmed, sigma))
    print("std (Sigma):", lognorm.std(Rmed, sigma))

scatteringFunction(Volume_Fraction, deltaRho, sigma, R, Rmed)

plotSphericalMicelles()
plotLogNormalDistribution(R, sigma)
