#! /usr/bin/env python3

# import modules
import argparse

# create an ArgumentParser object
parser = argparse.ArgumentParser(description="This script parses a GFF file")

# add positional (required) arguments
parser.add_argument("gff", help="Name of the GFF file to parse", type=str)
parser.add_argument("fasta", help="Name of the FASTA file to parse", type=str)

# parse the actual arguments
# access argument values via `args` variable
args = parser.parse_args()

# open the GFF file
with open(args.gff) as beyonce:

	# loop over all the lines in the file
	for line in beyonce:
		
		# skip blank lines
		if not line.strip():
			continue

		# else it's not a blank line
		else:
			line = line.strip()

			# split line on tab character
			columns      = line.split('\t')

			# give variable names to the columns
			organsim     = columns[0]
			source       = columns[1]
			feature_type = columns[2]
			start        = int(columns[3])
			end          = int(columns[4])
			length       = columns[5]
			strand       = columns[6]
			attributes   = columns[8]

			# add the length to column 5
			columns[5] = str(end - start + 1)

			new_line = "\t".join(columns)
			print(new_line)







