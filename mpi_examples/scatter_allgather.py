'''
This program scatters data from the root task to all of the other MPI tasks,
does something to it, and then gathers it all up again.  The Scatter command breaks
the data to be scattered into equally-sized chunks and shares it with the other
tasks.  Note that this is different that Bcast, which broadcasts the *entire*
object (or array, or whatever) to all other tasks.

Note: this program adapted from code in https://github.com/jbornschein/mpi4py-examples
'''
import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD

if comm.rank == 0:
    print("-"*78)
    print(" Running on %d cores" % comm.size)
    print("-"*78)
    
# set size of local data size as well as the big
# data array on all tasks
my_N = 4
N = my_N * comm.size 

if comm.rank == 0:
    A = np.arange(N, dtype=np.float64)
else:
    A = np.empty(N, dtype=np.float64)

my_A = np.empty(my_N, dtype=np.float64)

# Scatter data from A into my_A arrays (each my_A array only
# gets a portion of the entire dataset - they should all be
# different on different tasks).
comm.Scatter( [A, MPI.DOUBLE], [my_A, MPI.DOUBLE] )

print("After Scatter:")
for r in range(comm.size):
    if comm.rank == r:
        print("[%d] %s" % (comm.rank, my_A))
    comm.Barrier()

# Everybody is multiplying by 2 - proof that it's not the same data, and has been modified.
my_A *= 2

# Allgather data into A again.  Note that this will gather
# my_A into A... and since it is an Allgather, you now have
# *all* of the data on *all* of the tasks.  You can also use
# Gather instead of Allgather, but it would just collect
# everything onto task zero instead of on all tasks.  Try it!
comm.Allgather( [my_A, MPI.DOUBLE], [A, MPI.DOUBLE] )

print("After Allgather:")
for r in range(comm.size):
    if comm.rank == r:
        print("[%d] %s" % (comm.rank, A))

comm.Barrier()

