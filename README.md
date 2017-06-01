# ACRES MPI tutorial

MPI tutorial for the MSU ACRES REU

Load up the mpi4py and numpy modules on the HPCC on one of the development nodes:

```
module load mpi4py
module load NumPy
```

Look at the examples in the directory mpi_examples, which are heavily annotated to explain what is happening.  You can run them with:

```
mpirun -np 4 my_example_script.py
```

where ```-np 4``` means to use 4 MPI tasks (this can be changed).

----

## Really important links

[mpi4py examples (GitHub repository)](https://github.com/jbornschein/mpi4py-examples) -- DOWNLOAD THIS!

[A Python Intro to Parallel Programming with MPI](http://materials.jeremybejarano.com/MPIwithPython/index.html)  -- this is extremely useful! 

[mpi4py website](http://pythonhosted.org/mpi4py/)

[mpi4py documentation](http://mpi4py.readthedocs.io/en/stable/index.html)

[mpi4py user manual](http://pythonhosted.org/mpi4py/usrman/index.html)

[Livermore Parallel Computing tutorial](https://computing.llnl.gov/tutorials/parallel_comp/) 

[Livermore MPI tutorial (C++/Fortran)](https://computing.llnl.gov/tutorials/mpi/)

[Introduction to Scientific Computing book](http://pages.tacc.utexas.edu/~eijkhout/istc/istc.html) by Victor Eijkhout  ([BitBucket repository](https://bitbucket.org/VictorEijkhout/hpc-book-and-course))

----

