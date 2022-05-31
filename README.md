# ACRES MPI tutorial

Author: Brian O'Shea, oshea@msu.edu (CMSE and Physics+Astronomy)

## MPI tutorial for the MSU ACRES REU

This tutorial requires use of Python 3 and
[mpi4py](https://mpi4py.readthedocs.io/en/stable/), which is the set
of Python bindings to the Message Passing Interface (MPI) library.  The
HPCC does not have mpi4py installed, but you can load up a version of
Python that includes mpi4py by first logging onto one of the
development nodes of the HPCC (e.g., dev-intel16, dev-intel18,
dev-amd20), and then typing the following at the command prompt:

```
source ~oshea/python_MPI_setup.sh
```

This shell script will unload the system Python modules and will load
up the [Anaconda python distribution](https://www.anaconda.com/products/individual-b)
with Python 3.8, NumPy, Matplotlib, SciPy, and many other packages, as
well as mpi4py.  (You can see what this script actually does by typing
`cat ~oshea/python_MPI_setup.sh` .)

If you want to install the Anaconda Python distribution and mpi4py in
your own home directory on the HPCC, there is a file called
`INSTALLATION.md` in this repository.

Look at the examples in the directory mpi_examples, which are heavily
annotated to explain what they are doing.  You can run them on the
development nodes with:

```
mpirun -np 4 python my_example_script.py
```

where ```-np 4``` means to use 4 MPI tasks (this can be changed, 
but people often choose to use powers of two).

## Before the tutorial


1. Read [Chapter 1 (through section 1.3.4.3)](http://pages.tacc.utexas.edu/~eijkhout/istc/html/sequential.html)
of the book [Introduction to High-Performance Scientific Computing](http://pages.tacc.utexas.edu/~eijkhout/istc/html/index.html),
by Victor Eijkhout.  Optionally, skim through
[Chapter 2](http://pages.tacc.utexas.edu/~eijkhout/istc/html/parallel.html)
of that book as well.

2. Read through the file `supercomputing_and_MPI_notes.pdf`, 
   which is included in this repository.

----

## Really important links

[mpi4py examples (GitHub repository)](https://github.com/jbornschein/mpi4py-examples) -- very useful mpi4py examples!

[mpi4py website](https://bitbucket.org/mpi4py/mpi4py/src)

[mpi4py documentation](http://mpi4py.readthedocs.io/en/stable/index.html)

[Livermore Parallel Computing tutorial](https://hpc.llnl.gov/documentation/tutorials/introduction-parallel-computing-tutorial) 

[Livermore MPI tutorial (C++/Fortran)](https://hpc-tutorials.llnl.gov/mpi/)

[Introduction to Scientific Computing book](https://theartofhpc.com/istc/index.html) by [Victor Eijkhout at TACC](http://www.eijkhout.net/)

[Parallel Programming in MPI and OpenMP](https://theartofhpc.com/pcse/index.html), also by Victor Eijkhout 

----

