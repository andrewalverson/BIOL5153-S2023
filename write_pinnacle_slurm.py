#! /usr/bin/env python3

# set some variables
job_name = '<JOB-NAME>'
queue = 'comp01'
walltime = 1
num_nodes = 1
num_processors = 24

# print bash header
print('#!/bin/bash')

print()

# print SBATCH commands
print('#SBATCH --job-name=' + job_name)
print('#SBATCH --partition', queue)
print('#SBATCH --nodes=' + str(num_nodes))
print('#SBATCH --qos comp')
print('#SBATCH --tasks-per-node=' + str(num_processors))
print('#SBATCH --time=' + str(walltime) + ':00:00')
print('#SBATCH -o aja_%j.out')
print('#SBATCH -e aja_%j.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=aja@uark.edu')

print()

# purge all the modules
print('module purge')

print()

# cd into the submit directory
print('cd $SLURM_SUBMIT_DIR')

print()

print('# job command here')
