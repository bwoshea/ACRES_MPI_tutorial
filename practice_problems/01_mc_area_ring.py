'''
This routine uses Monte Carlo integration to calculate the area of a
ring.  This is intended to be parallelized.

Part 1: Rewrite this code so that it calculates a total of N_p points
using N_t MPI tasks, with a (roughly) equal number of points being calculated
on each MPI task.  When parallizing it, consider what happens when you have
the same random seed on all processes.  Given the goals of Monte Carlo
integration, is this a desirable outcome?

Part 2 (if you have time): Take your results in Part 1 and rewrite
them so that the integration takes place iteratively: that is, after
some number of points, the root processor calculates the change in
integral value between successive additions of sets of points and
stops if the fractional change is below some desired user-determined
threshold (and the estimated error for the integration is below some
threshold).
'''

import numpy as np

def in_bounds(x,y):
    '''
    takes in points x,y and determines whether or not that
    point is within the ring between r=0.5 and r=1.0.
    returns 1 if true, 0 if false.
    '''
    r = (x**2 + y**2)**0.5
    if r >= 0.5 and r <= 1.0:
        return True
    else:
        return False

N_points = 10000

# explicity seed the random number generator (so that you get
# the exact same result each time!)
np.random.seed(8675309)

# keep track of number of points in bounds vs. total
N_in_bounds = 0
N_total = 0

# loop over points.  For each point, determine whether or not it is
# within bounds.  If so, increment N_in_bounds.  Always increment N_total.
for i in range(N_points):
    x = np.random.uniform(-1.0,1.0)
    y = np.random.uniform(-1.0,1.0)
    if in_bounds(x,y) == True:
        N_in_bounds += 1
    N_total += 1

# estimated area based on the area of the square
est_area = 4.0*float(N_in_bounds)/float(N_total)

# actual area = (1**2 - 0.5**2)*pi
actual_area = 0.75 * np.pi

# calculate fractional error
frac_error = np.abs( est_area - actual_area) / actual_area

print("est and real area:", est_area, actual_area)
print("fractional error:", frac_error)
print("total points:", N_total)
