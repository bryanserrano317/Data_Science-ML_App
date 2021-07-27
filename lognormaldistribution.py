import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
from scipy.integrate import quad

# Import the necessary excel spreadsheets
sample_data = pd.read_csv('sample_data.csv')
scatteringfunction = pd.read_csv('lognormalvalues.csv')
workbook = xlrd.open_workbook('sample_data.xlsx')

worksheet = workbook.sheet_by_index(0)

# Read in all q and r values from excel spreadsheet
spreadsheet = [[worksheet.cell_value(i,j) for i in range (1, worksheet.nrows)]
                                          for j in range (0,3)]

# Input Variables
Volume_Fraction = 0.01
R = 55*(10**8)
Rmed = 60*(10**8)
sigma = 0.2
SLD_sphere = (3.262)*(10**8)
SLD_solvent = (3.069)*(10**8)
deltaRho = SLD_sphere - SLD_solvent
bkg = 0

# Output gaussian distribution for a sphere using polydispersity, R, and Rmed
def logNormalDistribution(sigma, R, Rmed):
    fR = (1/((sigma)*R*math.sqrt(2*math.pi)))*math.exp((-1/(2*(sigma**2)))*(np.log(R)-np.log(Rmed))**2)
    print("fR ", fR)
    return fR

# Output scattering amplitude for a sphere using q and R
def scatteringAmplitude(q, R):
    FqR = (3*(math.sin(q*R)-(q*R)*math.cos(q*R)))/((q*R)**3)
    print("fqR ", FqR)
    return FqR

# Output integral equation component from scattering intensity equation
def integrand(q, R):
    return logNormalDistribution(sigma, R, Rmed)*(R**6)*(scatteringAmplitude(q, R))**2

def scatteringFunction(Volume_Fraction, deltaRho, sigma, R, Rmed):
    #gaussian = gaussianDistribution()
    #amplitude = [scatteringAmplitude(spreadsheet, i, R) for i in range (1, worksheet.nrows)]
    
    # Calculate the integral value for each
    for i in range (1, worksheet.nrows):
        for j in range (0,1):
            q = spreadsheet[0][i-1]
            #print(q)
            integral = [quad(integrand, 0, np.inf, args=(q))] 
            #print(integral[0][0])
            qScatteringFunction = ((((4*math.pi)/3)**2)*Volume_Fraction*(deltaRho**2))*(integral[0][0])
            print(qScatteringFunction)

# Plot two sets of miscelle data in a scatterplot
def plotSphericalMicelles(data, data2):
    plt.subplot(111)
    plt.scatter(data2.q, data.Iq, s = 0.9, c = 'red')
    plt.ylim(1*10**-2, 1*10**10)
    plt.xlim(0.002, 0.700)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('q ($Å^{-1}$)', fontsize = 12)
    plt.ylabel('Intensity ($cm^{-1}$)', fontsize = 12)
    plt.grid(True)

scatteringFunction(Volume_Fraction, deltaRho, sigma, R, Rmed)
plotSphericalMicelles(scatteringfunction, sample_data)