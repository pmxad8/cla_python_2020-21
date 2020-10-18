#### script to complete the newton method part of the coursework ####

###############################################################################
########################### import libraries ##################################
###############################################################################

import numpy as np;
import matplotlib.pyplot as plt


###############################################################################
###############################################################################
####################### homebrew functions ####################################
###############################################################################
###############################################################################

def get_f(x):
	# returns f(x) for the given f at point x
	f = x**2 - 2
	return f
	
def get_dfdx(x):
	# returns dfdx for given f at point x
	dfdx = 2*x
	return dfdx
	

def newton_func(f,dfdx,p0,TOL,Nmax):
	# computes the zero of f using newtons method
	p_vec = np.zeros(Nmax) #preallocate solution vector
	p_vec[0] = p0; #store the initial value
	
	for k in range(1,Nmax):
		x = p_vec[k - 1]
		p_vec[k] = x - f(x)/dfdx(x) #update the approx using newton method
		
		#if consecutive approximations haven't changed, have converged. Break.
		if abs(p_vec[k] - x) < TOL:
			print('Method has converged.')
			break
	
	return p_vec[0:k+1] #return the values that have been used
	
		
	
###############################################################################
########################### Driver ############################################
###############################################################################	

p0 = 0.5;
Nmax = 50;
TOL = 1e-6;
p_vec = newton_func(get_f,get_dfdx,p0,TOL,Nmax)
print(p_vec)
