#! /usr/bin/env python3

# import modules
import argparse

# create an ArgumentParser object
parser = argparse.ArgumentParser(description="This script creates a \
	SLURM file for jobs on the AHPCC cluster")

# add positional (required) arguments
parser.add_argument("job_name", help="Name of the job",type= str)

# add optional arguments
parser.add_argument("-n", "--num_nodes", help="Number of nodes to request",\
	default = '1', type=int)
parser.add_argument("-p", "--num_processors", help="Number of processors \
	to request", default = '24', type=int)
parser.add_argument("-w", "--walltime", help="Length of the job", \
	default = '72', type=int)
parser.add_argument("-q", "--queue", help="Requested queue (comp01, comp06 \
	comp72)", default = 'comp72', type = str)

# parse the actual arguments
# access argument values via `args` variable
args = parser.parse_args()


# print bash header
print('#!/bin/bash')

print()

# print SBATCH commands
print('#SBATCH --job-name=' + args.job_name)
print('#SBATCH --partition', args.queue)
print('#SBATCH --nodes=' + str(args.num_nodes))
print('#SBATCH --qos comp')
print('#SBATCH --tasks-per-node=' + str(args.num_processors))
print('#SBATCH --time=' + str(args.walltime) + ':00:00')
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
