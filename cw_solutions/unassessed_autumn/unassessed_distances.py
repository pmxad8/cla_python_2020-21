#### script to compute the distance travelled in ex.3 ####

############### Crow Flies (Euclidean or Pythagorean Distance) ####################################
## We start at the origin, and must find the final position we reach, then simply compute 
## sqrt(xcoord^2 + ycoord^2)
###################################################################################################

############## Total Distance (taxi cab distance) #################################################
# regardless of direction, if we take a step, we travel a distance of 1, so we increase our distance
# by 1 each time we find an entry that isn't zero in seq. Taxi cab distance is the final distance
import math  #imports the sqrt function

# we hard code a sequence for now. Update to give an input later 

x_position = 0;
y_position = 0;
total_dist = 0;

seq = [0,-1,-1,2,0,2,-2,1,1,0,-2] #this is out "random" sequence of numbers

num_steps = range(0,len(seq))
for kk in num_steps:
	if (seq[kk] == 1): ## move to the left
		x_position += 1
		total_dist += 1
	elif (seq[kk] == -1): ## move to the right (cha cha real smooth)
		x_position -= 1
		total_dist += 1
	elif (seq[kk] == 2): ## move up
		y_position += 1
		total_dist += 1
	elif (seq[kk] == -2): ## move down
		y_position -= 1
		total_dist += 1
	## there's an implied else do nothing here, but we don't need to do anything as we don't move

crow_distance = math.sqrt(x_position**2 + y_position**2) #compute the pythagorean distance
## print both distances
print('Crow distance = ' + str(crow_distance)) 
print('Total distance = ' + str(total_dist))