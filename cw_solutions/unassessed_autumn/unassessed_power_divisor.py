#### script to find the greatest power of two divisor between two integers ####

## this solution is clunky but intuitive. We simply divide each integer by two until it is no longer even

input_a = float(input('Enter an integer: '))
input_b = float(input('Enter another integer: '))

## define booleans that check positive and integer for both a and b.
are_positive = (input_a > 0) and (input_b) > 0
are_integers = (input_a.is_integer()) and (input_b.is_integer())

## if both booleans are true, do the division
if (are_positive and are_integers):
		power_counter = 0; # this initialises our power of two
		while( (input_a%2==0) and (input_b%2==0)): #while both a and b are even
		# divide both by 2 and update the power of two
			input_a = input_a/2 
			input_b = input_b/2
			power_counter += 1

		## conditional output
		if(power_counter == 0):
			print('No power of two divisors')
		else:
			print('Greatest power of two divisor is:' + str(2**power_counter))

else:
	print('Inputs must be positive integers. Exiting code...')

print('END OF EXECUTION')