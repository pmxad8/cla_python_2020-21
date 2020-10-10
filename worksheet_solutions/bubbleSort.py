#### Script to merge two lists ####
## this uses a bubble sort that is covered in the decision further maths modules!

# disclaimer - the merge sort is the optimal way to do this, but the coding is significantly harder

import math
# these are hard coded which is bad practice but hey ho
first_list = [14,33,27,10]
second_list = [35,19,42,44]

init_list = first_list + second_list #combine the lists into an unsorted list
sorted_list = init_list.copy() #make a copy of the initial list so we can change it

ind_range = len(sorted_list) #find the length of the list we're dealing with
indices = range(ind_range) #this is apparently how you can loop over indices in python?

## this nested loop compares the iith entry with all others and shifts it to the right if it's larger
for ii in indices:
	for jj in indices:
		if sorted_list[jj] > sorted_list[ii]: #if the jth entry is bigger ....
			sorted_list[jj],sorted_list[ii] = sorted_list[ii],sorted_list[jj] #... move it to the right (this line switches the order of the two compared entries)


print('Initial list: ' + str(init_list))
print('Sorted list: ' + str(sorted_list))

print('END OF EXECUTION')