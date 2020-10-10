##### script to check if a number is prime ####

import math #needed for the sqrt and ceiling function

userInput = float(input('Enter a positive integer ')) #user input
isInt = userInput.is_integer() #checks if input is an integer
isPositive = userInput > 0
primeSum = 0 #this is just to add up the number of things that FAIL to divide userInput

# if not an integer, stop execution
if isInt and isPositive:
	print('Your integer is: ' + str(userInput)) 
	primeCheck = range(2,math.ceil(math.sqrt(userInput))) # we only need to check if N is divisible by numbers upto sqrt(n). Ceil is to ensure whole number for the range function
	for n in primeCheck: #loop over all possible divisors
		tmp = userInput % n #check if is a divisor
		primeSum += tmp #this adds 0 if is a divisor, 1 if not
		#if we have a divisor, stop because not prime
		if tmp == 0:
			primeSum = 0; #reset to zero as thing is definitely not prime now we have a divisor
			print(str(userInput) + ' is not prime')
			print(str(n) + ' divides ' + str(userInput) )
			break

else:
	print('Input must be a positive integer')


if primeSum > 0: #if all possible divisors fail, we have a prime
	print(str(userInput) + ' is prime')

print('END OF EXECUTION')
