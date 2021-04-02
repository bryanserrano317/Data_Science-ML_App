# Analysis for spherical micelles with a spherical Gaussian Distribution


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import scipy.integrate as integrate

#def sphericalMicelles():


def plotSphericalMicelles(data):
    plt.subplot(111)
    plt.scatter(sample_data.q,sample_data.r, s = 0.1, c = 'red')
    plt.xlim(0.001, 1)
    plt.ylim(0.0000001, 10)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('q($Å^{-1}$)', fontsize=12)
    plt.ylabel('Intensity', fontsize=12)
    plt.grid(True)

def readSheet(workbook):
    worksheet = workbook.sheet_by_index(0)

    counter = 0
    value = [1,2,3]

    for i in range(1, worksheet.nrows):
        for j in range(0,3):
            value(i).append(j)
            print(value)

    #scatteringFunction(worksheet.cell_value(i,j))

def scatteringFunction(value):
# modeling functions

#   Normalized Gaussian Distribution
#       f(x) = 1/(std-dev*(sqrt(2*pi)))*exp^(-1/2*((x-mean)/std_dev)^2)

#   form factor
#       V = 4*pi/3*(R^3)

#   p (polydispersity) page 39/220
#       (std-dev)/Ravg


#   from 200 page pdf -> Scattering function
#       I(q) = ((4pi/3)^2)*N*(p^2)*(integral(0,inf)*f(R)*R^6*F^2^(qR)dR)


#   read-in inputs from excel sheet
#   for loop to get each q value
#   toggles for close code blocks for python
    print("HELLO WORLD")

sample_data = pd.read_csv('sample_data.csv')
workbook = xlrd.open_workbook('sample_data.xlsx')

plotSphericalMicelles(sample_data)
readSheet(workbook)
plt.show()

            #if(j == 0):
                #print("q: ", worksheet.cell_value(i,j))
            #if(j == 1):
                #print("r: ", worksheet.cell_value(i,j))
            #if(j == 2):
                #print("s: ", worksheet.cell_value(i,j))

        #counter += 1
        #print(counter)

#twod_list = [[worksheet.cell_value(i,j) for i in range(1, worksheet.nrows)] for j in range(0,3)]

#print(twod_list)
