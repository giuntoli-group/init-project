# Kickoff assignment

[![hackmd-github-sync-badge](https://hackmd.io/xSCuTh_7TpGF2IKSgEMJ8A/badge)](https://hackmd.io/xSCuTh_7TpGF2IKSgEMJ8A)



This document provides you with the fundamental tools used in your project. You will learn how to
- use the terminal (command line)
- connect to the computer clusters (Habrok, Nieuwpoort, etc.)
- run your first simulation
- analyse the simulations using python
- interpret the results


At the end of this tutorial, you should be able to
- find your way in the terminal using the fundamental commands 
- connect to Habrok either directly from terminal (for mac and linux users) or through Putty (for windows users)
- run your first simulation on the interactive node of Habrok 
- understand the Bead-Spring model and the unit system
- write your first Python script that analyses the simulations
- call Python functions
- plot your results using matplotlib


Throughout this document, you will encounter some tasks. Please complete them in 10 days. You are highly encouraged to talk to each other and collaborate. If you are stuck in any of these steps, ask your supervisor for help. 

---


## Part 1: Introduction to command line

The command line, or terminal, is a text-based interface to the system. You can navigate through files, run programs, and even connect to other computers. For many computational projects, especially those involving computer clusters, the command line is an essential tool.

Here are some fundamental commands you will use:

- `pwd` to print the directory you're currently in
- `ls` to list the files and directories in the current directory
- `cd` to change the directory
- `mkdir` to create a new directory
- `rm` to remove files or directories
- `cp` to copy files or directories

> **DANGER**: Never type `rm -rf` in your home directory. This will delete everything in your system and it's not reversible.



### Remote connection to Habrok

To connect to computer clusters like Habrok and Nieuwpoort, you'll use SSH (Secure Shell). SSH allows you to securely connect to another computer over the internet. Click [here](https://wiki.hpc.rug.nl/habrok/connecting_to_the_system/connecting) for more information on how to connect to Habrok

For Mac and Linux users, open the terminal and type:

```bash!
ssh s123456@interactive1.hb.hpc.rug.nl
```

Replace `s123456` by your student number.

There are 4 possible ways of connecting to Habrok. If the above node is irresponsive, you can try the following:

```bash
ssh s123456@login1.hb.hpc.rug.nl
ssh s123456@login2.hb.hpc.rug.nl
ssh s123456@interactive2.hb.hpc.rug.nl
```


For Windows users, you'll need to download and install Putty, a free SSH client. Once installed, open Putty, enter the hostname (e.g., `s123456@interactive1.hb.hpc.rug.nl`), and click 'Open' to connect. More information for Windows users [here](https://wiki.hpc.rug.nl/habrok/connecting_to_the_system/windows)


### Task 1: Complete [this tutorial](https://linuxsurvival.com/linux-tutorial-introduction/) on the command line

Optional task: Watch [this video](https://www.youtube.com/watch?v=s3ii48qYBxA) 

### Task 2: Connect to Habrok and type the following command
```bash
echo $USER
```
What is the output on the screen?


## Running your first simulation


After connecting to Habrok, you'll navigate to a suitable directory to run your simulation. We will run this simple simulation on the interactive node, but please note that the purpose of the interactive node is to test your simulations. Never run an actual simulation on the login/interactive nodes once you start working your own project.

First, navigate to the scratch partition on Habrok by typing the following.

```bash!
cd /scratch/$USER
```
### Task 3: Create a new directory named ```tutorial``` in this partition.


Before running our simulations, we need to load our simulation software LAMMPS. This is already installed on Habrok. Type the following: 

```bash=
module load LAMMPS/23Jun2022-foss-2021b-kokkos
lmp
```
in the given order. `lmp` is the name of the executable that launches the LAMMPS interface. You should see something like the following after typing this command.

```bash
LAMMPS (23 Jun 2022 - Update 1)
OMP_NUM_THREADS environment is not set. Defaulting to 1 thread. (src/comm.cpp:98)
using 1 OpenMP thread(s) per MPI task
```

Once you verify that you have access to `lmp` command, hit `ctrl+c` to exit. Now, we are ready to run our first simulation. 

### Task 4: Navigate to ```tutorial``` and copy the LAMMPS script and the data file from your computer to here. (TODO: add the chain creation with python as a separate step)

Type the following and make sure that you are in the correct directory and you have the necessary files.
```bash=
pwd
ls
```
Make sure that your output is the same as the ones below

![image](https://hackmd.io/_uploads/SkzEnE31C.png)


Now, we are ready to run our first simulation. Type the following

```bash!
lmp -in in.single_chain 
```
This should take approximately two minutes and you will see that information on your screen at the end of the simulation.

![image](https://hackmd.io/_uploads/H1geRV3J0.png)


## Introduction to Polymer Physics

## TODO:

Understanding the Bead-Spring model is crucial in coarse-grained molecular dynamics (CGMD) simulations. This model simplifies the polymer chain into a series of beads (monomers) connected by springs (bonds). This abstraction allows us to study the properties of polymers without having to learn chemistry.

### Task 5: Read the first two chapters of Polymer Physics by Rubinstein

The unit system in CGMD simulations typically involves reduced units. This system simplifies calculations and can be converted to real-world units based on the material being simulated if needed (you will probably not). The unit system in our LAMMPS simulations is known as Lennard-Jones (LJ) units. You will hear this name quite often. 

### Task 6: Read the [wikipedia page](https://en.wikipedia.org/wiki/Lennard-Jones_potential#) of Lennard-Jones potential and corresponding LAMMPS [units](https://docs.lammps.org/units.html)


### Task 7: Search for all the command you see in `in.single_chain` on LAMMPS [documentation](https://docs.lammps.org/Manual.html) and learn what they do


## Introduction to Python


Python is a powerful programming language that's widely used in scientific computing for its simplicity and the extensive library ecosystem. For analysing simulations, you'll often use libraries such as Numpy for numerical calculations and matplotlib for plotting. We heavily rely on the following libraries: MDAnalysis, signac, ... . It is very likely that you're not familiar with these libraries. Luckily you can always ask us or read their documentations. The latter is highly encouraged and [here](https://how-to.dev/how-to-read-the-documentation) is a guideline on how to read the documentation. Note that this applies to terminal commands as well. If you don't remember how to use a certain command, type `man` in front of the command. For python functions, type `help(<your_function_here>)` in your interpreter.

## TODO:

Here's how to install these libraries using conda:

```bash
conda env create -f environment.yml
```

And a simple script to analyse your simulation results:

```bash
python post_processing.py
```

Plot the anlysis results:


```python
import numpy as np
import matplotlib.pyplot as plt
```

## Interpreting your results

After running your simulation and analysing the data with Python, the next step is to interpret your results. This involves understanding what the data tell you about the polymer's behaviour under certain conditions and comparing your findings with theoretical predictions.

Plotting your results can help visualise trends and patterns that may not be apparent from raw data alone. For example, you might plot the average end-to-end distance of a polymer chain as a function of temperature to study its thermal properties.

