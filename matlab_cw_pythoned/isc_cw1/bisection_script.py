#### script to complete the bisection method part of the coursework ####

#################### library imports ###################################
import numpy as np;
import matplotlib.pyplot as plt;

########################################################################
########################################################################
###################### functions written by ALD ########################
########################################################################
########################################################################

def get_f(x):
	# function defines f(x) for a given value of x
	f = x**3 + x**2 - 2*x - 2;
	return f


def bisection_func(f,a,b,Nmax):
# this function performs Nmax iterations of the bisection method to 
# find the zero of f in the interval [a,b]
	p_vec = np.zeros(Nmax); #preallocate the storage for p_vec entries
	for k in range(0,Nmax):
		mp = (a+b)/2; #take the midpoint of the interval
		p_vec[k] = mp; #update vector
		if f(mp)*f(a) > 0: #check for a zero in left half of interval
			a = mp; #if no zero, move interval right
		else:
			b = mp; #else move interval left

	return p_vec


def bisectionStop_func(f,a,b,Nmax,TOL):
# this function improves upon bisection_func by adding a break condition
# where the function stops if the values are no longer significantly 
# changing. I.e. |p_i+1 - p_i| < TOL
	p_vec = np.zeros(Nmax);
	for k in range(0,Nmax):
		mp = (a+b)/2; #take the midpoint of the interval
		p_vec[k] = mp; #update vector
		if f(mp)*f(a) > 0: #check for a zero in left half of interval
			a = mp; #if no zero, move interval right
		else:
			b = mp; #else move interval left

		# if k > 0 because need at least two values: [0] and [1]
		if k > 0:
			# if succesive iterations are within TOL of each other, we have
			# converged
			diff = abs(p_vec[k] - p_vec[k-1])
			if diff < TOL:
				print('Method has converged to a solution. Exiting code')
				break
	print(k)
	return p_vec[0:k+1] #return only the entries in p_vec that we have used


########################################################################
########################################################################
################## Driver section of the script ########################
########################################################################
########################################################################


x = np.linspace(1,2,501); # x vector
#f = x**3 + x**2 - 2*x - 2; #this is the function we find the root of
a = 1; #lower limit on region to find the zero
b = 2; #upper limit on region
Nmax = 50; #number of allowed iterations
TOL = 1e-4; # define the tolerance for the bisection method

p_vec = bisection_func(get_f,a,b,Nmax)
print(p_vec)
p_vec_stop = bisectionStop_func(get_f,a,b,Nmax,TOL)
print(p_vec_stop)
