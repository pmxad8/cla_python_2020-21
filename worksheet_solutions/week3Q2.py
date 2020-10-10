#### script to check whether the product of two numbers is even ####

input_a = float(input('Enter an integer:'))
input_b = float(input('Enter another integer: '))

if input_a.is_integer() and input_b.is_integer(): #this checks both inputs are integers, and if they are continues
	prod = input_a * input_b; #find the product of a and b
	out = prod % 2; # this returns the remainder of (a*b)/2. If a*b is even we retrn 0, else we return 1.
else:
	print('Inputs must be integers')
	break


print(out)
print('END OF EXECUTION')
