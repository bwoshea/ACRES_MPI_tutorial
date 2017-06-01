'''
Uses the MPI Bcast command to broadcast a vector of data from the 
root processor (0) to all other processors.  Use numpy to create arrays!

Note: this program adapted from code in https://github.com/jbornschein/mpi4py-examples
'''

import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD

if comm.rank == 0:
    print("-"*78)
    print(" Running on %d cores" % comm.size)
    print("-"*78)

comm.Barrier()

# Prepare a vector of N=5 elements to be broadcast...
N = 5

# On the root process (0), create the actual array of data.  On the other
# processes, create empty arrays that will be filled up.  Explicitly make
# them all the same array. 
if comm.rank == 0:
    A = np.arange(N, dtype=np.float64)    # rank 0 has proper data
else:
    A = np.zeros(N, dtype=np.float64)     # all other arrays are just zero


# Everybody should now have the same...
print("Before Bcast:  [%02d] %s" % (comm.rank, A))

comm.Barrier()

# Broadcast A from rank 0 to everybody.
# note that you have to tell MPI what it's broadcasting
# so that it doesn't make a mess of it.  The 'Bcast' command
# works for objects that have MPI definitions.  The 'bcast' command
# (used below) can be used for anything (since it uses pickle) but
# is generally much slower.
comm.Bcast( [A, MPI.DOUBLE] )

# Everybody should now have the same...
print("After Bcast: [%02d] %s" % (comm.rank, A))

comm.Barrier()

# We can also broadcast other things.  Make a list of random stuff and
# broadcast it from rank 0 to all others!
if comm.rank == 0:
   data = ['monkey', 1, 7, 'asdf']
else:
   data = None

print("Before bcast: my rank is", comm.rank, "and my data is", data)

comm.Barrier()

   
# broadcast it using 'bcast', which works pretty much the same as
# 'Bcast', except that it pickles objects and can send anything.
# this means that it is much slower!
data = comm.bcast(data)

print("After bcast: my rank is", comm.rank, "and my data is", data)
