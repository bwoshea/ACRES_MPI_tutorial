'''
This uses MPI send and receive in order to hand data in a 'ring' - at each
iteration, each MPI task sends its data to the 'right', i.e., to the task whose
rank is one greater than it.  If you're at the max task, hand back to zero.  This
is analogous to people standing in a circle, all handing things to the person to their
right.
'''

import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD

if comm.rank == 0:
    print("-"*78)
    print(" Running on %d cores" % comm.size)
    print("-"*78)

comm.Barrier()

# prior to handing things around, set the local value to the
# rank of the local MPI task.  One has to be very specific about
# the rank, which is why we use Numpy arrays.  Note this value is
# different on each task since it's using comm.rank.
my_current_val = np.array(comm.rank, dtype='int64')

print("my rank is", comm.rank, "and my_current_val is", my_current_val)

comm.Barrier()


# For each MPI task, figure out who it is sending data to (my_target)
# and who it is receiving data from (my_source).  Use modulus arithmetic
# to ensure that we don't try to hand to a task that does not exist.
my_target = (comm.rank + 1) % comm.size
my_source = (comm.rank + comm.size - 1) % comm.size

print("on process", comm.rank, "I am sending data to", my_target, "and receiving data from", my_source)

comm.Barrier()

# Now, go through as many iterations as you are using processors.  At each
# iteration, hand data to the right.  If you're on task zero, print out the
# current value: it should change every time!
for i in range(comm.size):

    comm.Send([my_current_val, MPI.INT], dest=my_target)  # send data to my_target
    comm.Recv([my_current_val, MPI.INT], source=my_source)  # receive data from my_source
    if comm.rank == 0:
        print("on step", i, "my rank is", comm.rank, "and my_current_val is", my_current_val)
    comm.Barrier()  # put in a barrier to make sure the various CPUs don't get out of step

