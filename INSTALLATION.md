# Installing Anaconda Python and mpi4py

**WARNING: AS OF May 31, 2023 this has not been verified to still be correct!**

The goal of this file is to walk you through installing the
[Anaconda Python distribution](https://www.anaconda.com/products/individual-b)
on the MSU supercomputer (managed by the
[Institute for Cyber-Enabled Research](https://icer.msu.edu/), as well
as the [mpi4py](https://mpi4py.readthedocs.io/en/stable/) bindings for
MPI (which is necessary for running parallel Python codes that use the
Message-Passing Interface).  The Anaconda Python distribution is an
extremely convenient way to get a fully-featured Python programming
environment for your computational and data science needs.  It
includes a huge number of useful Python packages, such as
[Jupyter](https://jupyter.org/), [NumPy](https://numpy.org/),
[SciPy](https://www.scipy.org/), and
[Matplotlib](https://matplotlib.org/).  It is also easy to install new
packages using conda and/or pip, which is what we will do to install
mpi4py.

**The primary challenges in installing Anaconda on a supercomputer**
  are (1) the command line environment, which many people are not all
  that familiar with, and (2) ensuring that you are actually using the
  correct version of Python.

Before you do anything else,
[log onto the supercomputer](https://wiki.hpcc.msu.edu/display/ITH/How+to+Access+HPCC)
and then onto a development node (dev-intel16, dev-intel18,
dev-amd20).

MSU's supercomputer, like most supercomputers, uses a
[module system](https://wiki.hpcc.msu.edu/display/ITH/Module+System+and+Software+Installation)
to make it easy for users to load and unload different software
packages.  A variety of them are loaded by default on the development
nodes - to see what's loaded, type:

```
module list
```

You'll note that there is a Python module loaded by default.  **This
needs to be unloaded**, or else you may run into issues later!  To do
so, you have to do the following:

```
module unload Python
```

## Installing Anaconda

Now, we're going to get the Anaconda Python distribution. You can do
this at the command line using the
[wget](https://www.gnu.org/software/wget/) tool.  You can find the
location of the Linux distribution's downloadable file by looking for
the link at the bottom of
[this page](https://www.anaconda.com/products/individual-b) - in the
"Linux" section there is a link that says "64-Bit (x86) Installer",
and if you copy that link you will get the most current version.
Then, at the command line and while you are in your home directory,
type:

```
wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh
```

(or replace that URL with an updated version, if you want.)  It may
take a few minutes for that file to download, but don't worry!  wget
will give you a progress bar.  Then install the file that you have
downloaded by typing the following, updating the file name if you have
downloaded a newer version:

```
bash ./Anaconda3-2022.05-Linux-x86_64.sh
```

For installation it's perfectly reasonable to let Anaconda use all of
the defaults, although if you know what you're doing you may wish to
NOT allow conda to be your default shell environment.  If you say no
to that option, you'll have to use a text editor such as nano, vim, or
emacs to add this line to the end of the .bashrc file, which lives in
your home directory and gets run automatically every time you log in:

```
 export PATH="$HOME/anaconda3/bin:$PATH"
```

**Either way**, you can type `source ~/.bashrc` to set up your Linux
 environment so that you can find the Anaconda Python distribution, or
 log out of the development node where you have done the installation
 (using `exit`) and then log back in again.  **If you do the latter,
 don't forget to unload the Python module again!** (You're going to
 have to do this every time you log in, unless you add a line at the
 end of your .bashrc file to automatically do it.)

Congratulations!  At this point you should have a new Python
distribution.  Type `python` and it should launch a Python
interpreter!  Also, if you exit that and type `which python`, it
should point to the file `anaconda3/bin/python` in your home
directory.

## Installing mpi4py

We'll now use the [pip](https://pypi.org/project/pip/) tool to install
mpi4py.  pip is Python's native package installer, and can be used to
install or upgrade almost any Python tool.  To install mpi4py, you
type the following at the command line:
 
```
pip install mpi4py
```

You can then test to ensure that you have mpi4py installed correctly.
At the command line, type:

```
mpirun -np 4 python ~oshea/MPI_example.py
```

and it will produce a bunch of output, starting with:

```
I'm the root task! 0
I'm NOT the root task! 1
I'm NOT the root task! 2
I'm NOT the root task! 3
```

although not necessary in that order.  If you see this,
congratulations!  You have successfully installed and tested mpi4py.
If you do NOT see this, the next step is to debug it based on the
outputs you see.

## Using Anaconda in HPCC batch scripts

While it's fine to run short computational tasks on the development
node, anything that uses significant resources (CPUs, memory, etc.)
should run using the batch system.  You can easily use your new
version of Anaconda in a [Slurm](https://wiki.hpcc.msu.edu/display/ITH/Job+Scheduling+by+SLURM) batch script.  To do so, look at the
file `mpi_examples/example_batch_script.sb` in this repository, and
note the section that starts with the comment "#### THE LINES BELOW
THIS SET UP THE PYTHON ENVIRONMENT".
