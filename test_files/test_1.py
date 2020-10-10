################### code to plot some Gaussians ####################################

#### import libraries ####
import math
import numpy as np #import numerical library
import matplotlib.pyplot as plt #allow plotting

n = 101 # number of points
xx = np.linspace(-10,10,n) #vector of linearly spaced points
s = 0.5,1,1.5,2,5 # vector of sigma values
g = np.zeros(n) # making vector of n zeros

## reoding stupid python syntax. This syntax is clunky and I hate it...
PI = math.pi
EXP = np.exp
SQRT= math.sqrt

## loop over all sigma values
for sig in s: #this is apparently how loops work in python?
	g = 1/(sig*SQRT(2*PI)) * EXP(-xx**2/(2*sig**2)) # formula of Gaussian curve
	plt.plot(xx,g,linestyle = '--') # update python plot

plt.show() # actually show the figure
