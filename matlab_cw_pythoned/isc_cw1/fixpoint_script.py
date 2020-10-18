#### script to perform the fixed point method part of the coursework ####

#################################################################################
########################### library imports #####################################
#################################################################################

import numpy as np;
import matplotlib.pyplot as plt;


#################################################################################
#################################################################################
########################## funcitons written by ALD #############################
#################################################################################
#################################################################################

def get_f(x):
	#function computes f(x) at a given x
	f = x**3 + x**2 - 2*x - 2;
	return f


def fpiter_func(f,c,p0,Nmax):
	# performs the fixed point method to find the zero of f, taking input c between
	# 0 and 1, an initial guess p0 and a maximum number of iterations Nmax

	# this defines a temporary function to compute g as required
	get_g = lambda x,c,f: x - c*f(x)

	p_vec = np.zeros(Nmax) #preallocate for speed
	
	p_vec[0] = p0; #store the first guess

	for iter in range(1,Nmax):
		p = get_g(p_vec[iter-1],c,f) #uses the fp method : p = g(p)
		p_vec[iter] = p; #store the new value

	return p_vec




def optParamFPiter_func(f,p0,p,TOL,Nmax):
	# function is used to find the optimal parameter c for the fp method. This is the
	# value of c that gives convergence to p inthe fewest iterations. We have the exact
	# solution p, an initial guess p0, a tolerance TOL for convergence and a max number
	# of iteratoins Nmax. We also have the function f which we find the zero of.
	#
	
	#c_vec = [0.1,0.5,1]
	c_vec = np.linspace(0.001,1,1000) #vector of parameter values [0.001,0.002,...1]
	c_store = np.zeros(len(c_vec))
	N_store = np.zeros(len(c_vec))
	get_g = lambda x,c,f: x - c*f(x) #fixpoint function definition
	
	for kk in range(0,len(c_vec)):
		p_current = p0
		c = c_vec[kk] #current parameter value
		c_store[kk] = c #store the current c value
		iter = 0; #initialise iteration counter
		while(iter <  Nmax):
			p_current = get_g(p_current,c,f) #update p using p = g(p)
			iter += 1 #update iteration counter
			
			if abs(p_current - p) < TOL: #if converges
				N_store[kk] = iter #store no of ierations toconverge
				break
				
			if (iter == Nmax or abs(p_current) > 1e10): #if not converged
				N_store[kk] = Nmax + 1 #ensures never picked	
				break

				
	N_opt = np.amin(N_store) #find the minimum value of N_store (least iterations)
	ind = np.where(N_store == N_opt) #find the location of the min values
	
	# if more than one location for optimal value, take the first
	ind = ind[0]; #extract the index values
	ind = ind[0]; #extract the first index
	
	c_opt = c_vec[ind] #extract the best parameter value

	return c_opt,N_opt

##################################################################################
##################################################################################
################################### Driver #######################################
##################################################################################
##################################################################################


c = 1/10;
p0 = 1;
Nmax = 20;
TOL = 1e-10;
p = np.sqrt(2);
#p_vec = fpiter_func(get_f,c,p0,Nmax);
#print(p_vec)

c_opt,N_opt = optParamFPiter_func(get_f,p0,p,TOL,Nmax)
print('The optimal parameter value is c = ' + str(c_opt))
print('This value gives convergence in ' + str(N_opt) + ' iterations')
