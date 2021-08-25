README.txt

The following scripts are used to provide fitting functions for experimental micelle data using gaussian and log normal distributions to estimate parameters. 

The approach to implement the modeling functionality is as follows: 

1.) Import the necessary libraries to implement excel read-ins and the tools to calculate from those values. 

2.) Declare the variables that will be holding the read-in excel data.

3.) Return the parameters for spherical micelles. 

4.) Return the gaussian distribution and scattering amplitude equation.

5.) Return the integrand component of the scattering intensity equation.

6.) Put all the equations together and input the q and R values that will be used to calculate the gaussian / log-normal distribution equation, scattering amplitude equation, the integrand, and remaining parameters. 

7.) The scattering intensity function will return the calculate best fit values. 

8.) The values are then to be implemented in an excel sheet (gaussiandistribution.csv / lognormalvalues.csv) for plotting. 

    Note that the function will return 275 values. Make sure that you replace the FIRST 275 values in the excel sheet. The other values is the experimental data that will need a line of best fit.

9.) Plot functions will plot the line of best fit, experimental data, and R values with a gaussian or log normal distribution. 

------------------------------------------

Improvements to be made: 

The values returned from the scattering intensity function are in an incorrect scale.
They need to range from 10^-3 to 1. 

This could be fixed by possibly implementing more algorithims that can provide more accurate values and clean up data. We don’t know what algorithims we might need, though.

The equations and units were checked rigorously to ensure they were correct and providing the expected values. 

It is highly recommended that machine learning is implemented with Tensorflow libraries to model error section in lower right hand corner and significantly improve modeling functionality. 

Machine learning would allow the script to be able to detect the experimental data line, calculate a value with the scattering intensity equation, and fit the value close to the equation without significantly altering the value. Instead of only calculating values with equations and plotting those values. It would resolve any issues with units or overall noise from experimental data and plot the value based on expectations.

Useful links: 

liulab.csrc.ac.cn:10005/tutorial/

https://www.sciencedirect.com/science/article/pii/S2589004220300900
