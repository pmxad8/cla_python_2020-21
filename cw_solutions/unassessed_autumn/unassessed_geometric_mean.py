#### script to compute the geometric mean of two numbers ####

import math; #import the math library for the sqrt function

## user inputs
input_a = float(input('Enter an integer: '))
input_b = float(input('Enter another integer: '))

## define booleans that check positive and integer for both a and b.
are_positive = (input_a > 0) and (input_b) > 0
are_integers = (input_a.is_integer()) and (input_b.is_integer())

## if both booleans are true, do the geometric mean
if (are_positive and are_integers):
	geom_mean = math.sqrt(input_a * input_b)
	print(geom_mean)
else:
	print('Geometric mean is undefined. Exiting code...')

print('END OF EXECUTION')