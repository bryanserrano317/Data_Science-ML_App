# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 16:54:34 2022

@author: BSO8
"""

import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import sklearn
from scipy.integrate import quad
from scipy.stats import norm
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

workbook = xlrd.open_workbook('lognormal.xls')

worksheet = workbook.sheet_by_index(0)

spreadsheet = [[worksheet.cell_value(i,j) for i in range (1, worksheet.nrows)]
                                          for j in range (0,3)]

xCoordinates = []
yCoordinates = []

# Considering dataset of 275 points, manually adjust range as seen fit
# first segmented regression analysis
for i in range (1, worksheet.nrows):
    xCoordinates.append([spreadsheet[0][i - 1]])
    yCoordinates.append([spreadsheet[1][i - 1]])


x1 = np.array(xCoordinates[:50])
y1 = np.array(yCoordinates[:50])

x2 = np.array(xCoordinates[50:100])
y2 = np.array(yCoordinates[50:100])

x3 = np.array(xCoordinates[100:200])
y3 = np.array(yCoordinates[100:200])

x4 = np.array(xCoordinates[200:275])
y4 = np.array(yCoordinates[200:275])


def polynomialRegression(x, y, degreeNum):
    poly_features  =  PolynomialFeatures(degree = degreeNum, include_bias = False)
    X_poly  =  poly_features.fit_transform(x.reshape(-1,1))
    poly_reg_model = LinearRegression()
    poly_reg_model.fit(X_poly, y)
    y = poly_reg_model.predict(X_poly)
    return y

y1 = polynomialRegression(x1, y1, 5)
y2 = polynomialRegression(x2, y2, 5)
y3 = polynomialRegression(x3, y3, 9)
y4 = polynomialRegression(x4, y4, 2)


fullFit = []
fullFit.extend(y1)
fullFit.extend(y2)
fullFit.extend(y3)
fullFit.extend(y4)


def plotSegmentedSphericalMicellesFit():
    s = pd.read_csv('sample_data.csv')
    plt.subplot(111)
    plt.scatter(s.q, s.r, s = 0.1, c = 'chartreuse')
    plt.scatter(spreadsheet[0][:50], y1, s = 0.1, c = 'blue')
    plt.scatter(spreadsheet[0][50:100], y2, s = 0.1, c = 'black')
    plt.scatter(spreadsheet[0][100:200], y3, s = 0.1, c = 'red')
    plt.scatter(spreadsheet[0][200:275], y4, s = 0.1, c = 'magenta')
    plt.xlim(1* 10 **-3,1)
    plt.ylim(1* 10 **-5,3 * 10 **1)
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True)
    
def plotFullSphericalMicellesFit():
    s = pd.read_csv('sample_data.csv')
    plt.subplot(111)
    plt.scatter(s.q, s.r, s = 0.1, c = 'chartreuse')
    plt.scatter(spreadsheet[0], fullFit, s = 0.1, c = 'blue')
    plt.xlim(1* 10 **-3,1)
    plt.ylim(1* 10 **-5,3 * 10 **1)
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True)
    
plotSegmentedSphericalMicellesFit()
#plotFullSphericalMicellesFit()