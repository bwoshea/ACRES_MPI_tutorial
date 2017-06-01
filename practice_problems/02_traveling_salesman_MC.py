# ############################################################
#
#  This file contains a serial version of the Traveling
#    Salesman Problem, solved using repeated randomized paths.
#    Note that this is *not* the optimal way to solve this
#    problem, but it's a good example of a solution that can
#    easily be parallelized.
#
# ############################################################
import numpy as np
import matplotlib.pyplot as plt
import itertools
from time import clock

##############################################################

def calc_total_distance(table_of_distances, city_order):
    '''
    Calculates distances between a sequence of cities.
    
    Inputs: N x N table containing distances between each pair of the N
    cities, as well as an array of length N+1 containing the city order,
    which starts and ends with the same city (ensuring that the path is
    closed)

    Returns: total path length for the closed loop.
    '''
    total_distance = 0.0

    # loop over cities and sum up the path length between successive pairs
    for i in range(city_order.size-1):
        total_distance += table_of_distances[city_order[i]][city_order[i+1]]

    return total_distance
        
def minimize_distance(table_of_distances, tries):
    '''
    For a given set of cities, randomize the city order for a given number of
    tries and get the shortest distance of all of the tries.

    Inputs: N x N table containing distances between each pair of the N
    cities, as well as an integer containing the number of times that
    the cities should be randomized.

    Returns: tuple containing the minimized distance and the order of
    city traversal.
    '''

    # keeps the smallest distance; set this to be an insanely large number at the outset
    smallest_distance = 1.0e+20;

    # this array will store the city ordering that corresponds to the smallest distance
    smallest_distance_city_order = np.zeros(shape=table_of_distances.shape[0]+1)

    # loop through and randomize the ordering of cities.  For each ordering,
    # calculate the total distance, and keep it if it's the smallest so far.
    for i in range(0, tries):

        # create the list of cities and then shuffle it.
        this_order = np.arange(table_of_distances.shape[0])
        np.random.shuffle(this_order)

        # tack on the first city to the end of the array, since that ensures a closed loop
        this_order = np.append(this_order, this_order[0])

        # calculate total distance of this arrangement of cities
        this_dist = calc_total_distance(table_of_distances, this_order)

        # check to see if this arrangement is the shortest; if so, keep it!
        if(this_dist < smallest_distance):
            smallest_distance = this_dist
            smallest_distance_city_order = np.copy(this_order)

    # return smallest distance, city ordering
    return smallest_distance, smallest_distance_city_order

##############################################################

############## USER SETS THESE ############

# seed for RNG: so we get the same value every time!
np.random.seed(8675309)

# number of cities we'll use.
number_of_cities = 10

# total number of times to randomize cities (for minimization purposes)
N_iters = 10**4

###########################################

# create random x,y positions for our current number of cities.

city_x = np.random.random(size=number_of_cities)
city_y = np.random.random(size=number_of_cities)

# table of city distances
city_distances = np.zeros((number_of_cities,number_of_cities))

# calculate distnace between each pair of cities and store it in the table.
# technically we're calculating 2x as many things as we need (as well as the
# diagonal), but whatever, it's cheap.
for a, b in itertools.product(range(number_of_cities), range(number_of_cities)):
    city_distances[a][b] = ((city_x[a]-city_x[b])**2 + (city_y[a]-city_y[b])**2 )**0.5

# keep track of time: start.
start_walltime = clock()

# call minimize_distance - this is where the magic happens, folks.
dist, order = minimize_distance(city_distances, N_iters)

# keep track of time: end.
stop_walltime = clock()

# calculate mean time used per iteration of the solver
time_iter = (stop_walltime-start_walltime)/N_iters

# print out some data
print("")
print("minimized distance:  %.3f" % dist, "after", N_iters, "steps for", number_of_cities, "cities")
print("city order:", order)
print("simulation took", stop_walltime-start_walltime, "seconds for", N_iters, "steps.  (%.3e sec. per iteration)" % time_iter)
print("")

# Make a plot of city positions - first make x,y arrays, then plot everything!
x = []
y = []

for i in range(0, city_distances.shape[0]):
    x.append(city_x[order[i]])
    y.append(city_y[order[i]])

x.append(city_x[order[0]])
y.append(city_y[order[0]])

plt.plot(city_x,city_y,'bo', x, y, 'r-')
plt.xlim(-0.2, 1.2)
plt.ylim(-0.2, 1.2)
plt.savefig("plot_dirs.png")
plt.close()
