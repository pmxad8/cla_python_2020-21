#### script to check whatever we agreed on ####
input_N = int(input('Enter a positive integer: '))


sum_counter = 0
k = 1;
while (k < input_N + 1):
	sum_counter = sum_counter + k# or sum_counter += k
	k = k + 1; # or k += 1

print(sum_counter)