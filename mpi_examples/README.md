# IMPORTANT

These examples use Python 3 and mpi4py.  The HPCC does 
not have these installed by default, but you can load this by logging
onto one of the development nodes of the HPCC (e.g., dev-intel14 or dev-intel16) and then type:

```
source ~oshea/python_MPI_setup.sh
```

Which will load up the Anaconda python distribution with Python 3, numpy, matplotlib, scipy, and many other packages, as well as mpi4py.  It will also set up the right system modules to use the correct compilers and MPI libraries.

Note: these examples *should* be able to use Python 2 as well as Python 2, but this is not supported.  If you want to try that, you should be able to log onto a dev node of the HPCC and type:

```
module load mpi4py
module load numpy
```

and it should work.