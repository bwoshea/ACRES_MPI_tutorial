# ACRES MPI tutorial

MPI tutorial for the MSU ACRES REU

This tutorial requires use of Python 3 and mpi4py.  The HPCC does 
not have these installed by default, but you can load this by logging
onto one of the development nodes of the HPCC (e.g., dev-intel14 or dev-intel16) and then type:

```
source ~oshea/python_MPI_setup.sh
```

Which will load up the Anaconda python distribution with Python 3, numpy, matplotlib, scipy, and many other packages, as well as mpi4py.  It will also set up the right system modules to use the correct compilers and MPI libraries.

Look at the examples in the directory mpi_examples, which are heavily annotated to explain what they are doing.  You can run them with:

```
mpirun -np 4 my_example_script.py
```

where ```-np 4``` means to use 4 MPI tasks (this can be changed, 
but people often choose to use use powers of two).

----

## Really important links

[mpi4py examples (GitHub repository)](https://github.com/jbornschein/mpi4py-examples) -- very useful mpi4py examples!


[mpi4py website](http://mpi4py.scipy.org/docs/)

[mpi4py documentation](http://mpi4py.readthedocs.io/en/stable/index.html)

[Livermore Parallel Computing tutorial](https://computing.llnl.gov/tutorials/parallel_comp/) 

[Livermore MPI tutorial (C++/Fortran)](https://computing.llnl.gov/tutorials/mpi/)

[A comprehensive MPI Tutorial resource](http://mpitutorial.com/) - lots of example tutorials

[Introduction to Scientific Computing book](http://pages.tacc.utexas.edu/~eijkhout/istc/istc.html) by Victor Eijkhout  ([BitBucket repository](https://bitbucket.org/VictorEijkhout/hpc-book-and-course))

----

