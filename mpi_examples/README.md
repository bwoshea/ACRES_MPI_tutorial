# IMPORTANT

This directory contains a variety of examples of MPI programs, 
which demonstrate different aspects of MPI (in particular, 
different types of MPI communication).  It also contains an 
example batch script for MSU's supercomputer that will run 
the python programs in this directory.  Both the programs and 
the batch script are heavily annotated to explain exactly what's 
going on.

These mpi example programs use Python 3 and mpi4py.  The HPCC does 
not have mpi4py installed, but you can load this by logging onto 
one of the development nodes of the HPCC (e.g., dev-intel16 or 
dev-intel18), and then type:

```
source ~oshea/python_MPI_setup.sh
```

Which will load up the Anaconda python distribution with Python 3,
numpy, matplotlib, scipy, and many other packages, as well as 
mpi4py.  

```
mpirun -np 4 python my_example_script.py
```

Note: these examples *should* be able to use Python 2 as 
well as Python 3, but Python 2 is not supported.  