'''
This program creates different data on each task, does something to it, and then sums it all up
on the root task using the Reduce command (or does the same thing but sums it all up
on *every* task using the Allreduce command, depending on what you comment out).

Note: this program adapted from code in https://github.com/jbornschein/mpi4py-examples
'''
import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD

if comm.rank == 0:
    print("-"*78)
    print(" Running on %d cores" % comm.size)
    print("-"*78)

# create an array of length my_N and multiply it by rank+1
# (so that it is different on each MPI task)
my_N = 4
my_A = np.arange(my_N, dtype=np.float64)
my_A *= float(comm.rank + 1)

# sum everything up on this task - should be different on every task!
my_sum = np.array(my_A.sum())

print("my rank is", comm.rank, "and my_A is", my_A, "and my_sum is", my_sum)

comm.Barrier()

all_sum = np.zeros_like(my_sum)

# now we call a Reduce which takes my_sum and sums it into all_sum, but
# only on the root task (task zero).  The other tasks should not get *any*
# information.
comm.Reduce( [my_sum, MPI.DOUBLE], [all_sum, MPI.DOUBLE], op=MPI.SUM, root=0)

# Try commenting out comm.Reduce and uncommenting the following
# command (comm.Allreduce), and see how the results differ.  You should now
# find out that all_sum is now set to the total sum on *all* tasks.

#comm.Allreduce( [my_sum, MPI.DOUBLE], [all_sum, MPI.DOUBLE], op=MPI.SUM)

# Try commenting out comm.Reduce and uncommenting the following command
# (comm.Allreduce), which is a little bit different than the previous command.
# It now takes my_sum on each rank and replaces it with the sum of my_sum.
# all_sum will now be 0.0 on all tasks!  

#comm.Allreduce( [my_sum, MPI.DOUBLE], [my_sum, MPI.DOUBLE], op=MPI.SUM)

comm.Barrier()

print("after reduce, on rank", comm.rank,  "my_sum is", my_sum, "and all_sum is", all_sum)


