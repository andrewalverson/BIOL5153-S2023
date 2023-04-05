#! /usr/bin/env python3

# import modules
import argparse

# create an ArgumentParser object
parser = argparse.ArgumentParser(description="This script returns the \
 Fibonacci number at a specified location in the sequence")

# add positional (required) arguments
parser.add_argument("num", help="The Fibonacci number you wish to calculate", type=int)

# add optional arguments
# the default for 'store_true' is . . . "False"
# if 'store_true', then assign 'True' with -v or --verbose
parser.add_argument("-v", "--verbose", help="Print verbose output (default = simple output)",
	action = 'store_true')

# parse the actual arguments
# access argument values via `args` variable
args = parser.parse_args()


# calculate the Fibonacci number/sequence
a,b = 0,1

for i in range(args.num):
	a,b = b,a+b

	fib_number = a


# print the answer
if args.verbose:
	print('The Fibonacci number for', args.num, 'is:', fib_number)
else:
	print(fib_number)








# print the answer
# print('The Fibonacci number for', args.num, 'is:', fib_number)












