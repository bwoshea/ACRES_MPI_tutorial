'''
This simple python program starts up MPI, has each MPI task print out its own rank
(i.e., its task number or name), the total number of tasks accessible, and then
exits.

You can call this from the command line with:

mpirun -np 4 python ./hello_world.py

Note that '4' can be replaced with any number you want, though using a
larger number than you have available computational cores won't really help much.

Note: this program adapted from code in https://github.com/jbornschein/mpi4py-examples
'''

from mpi4py import MPI

# this initiates MPI in this script and creates the communicator 'comm'.
# All MPI functions are now accessed through 'comm'
comm = MPI.COMM_WORLD

# the "rank" is this process's MPI task ID; this is unique to each process in the communicator.
# you can also get to it with comm.rank
my_rank = comm.Get_rank()

# the "size" is the total number of MPI tasks; each process gets the same number.
# you can also get to it with comm.size
my_size = comm.Get_size()

print("Hello! I'm rank %d from %d running in total..." % (my_rank, my_size) )

# wait for everybody to synchronize here.  Nothing after this line can
# happen until all MPI processes reach the barrier.
comm.Barrier()

# each process gets the same code, but since each process
# has a different rank we can do different things on each one.

# this will only happen on processor zero.
if my_rank == 0:
    print("and an extra-special hello from the root processor, whose rank is ", my_rank)
else:
    print("rank", my_rank, "says hi too")



