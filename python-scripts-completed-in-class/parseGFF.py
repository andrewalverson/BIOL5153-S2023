#! /usr/bin/env python3

# import modules
import argparse
import csv


# create an ArgumentParser object
parser = argparse.ArgumentParser(description="This script parses a GFF file")

# add positional (required) arguments
parser.add_argument("gff", help="Name of the GFF file to parse", type=str)
parser.add_argument("fasta", help="Name of the FASTA file to parse", type=str)

# parse the actual arguments
# access argument values via `args` variable
args = parser.parse_args()

# open the GFF file
with open(args.gff) as gff_file:

	# create a csv reader object
	reader = csv.reader(gff_file, delimiter='\t')

	# loop over all the lines in the file
	for line in reader:
		
		# skip blank lines
		if not line:
			continue

		# else it's not a blank line
		else:
			#line = line.strip()
			# print(line)
			# split line on tab character
			# columns      = line.split('\t')

			# give variable names to the columns
			organsim     = line[0]
			source       = line[1]
			feature_type = line[2]
			start        = int(line[3])
			end          = int(line[4])

			# add the length to column 5
			line[5] = str(end - start + 1)

			length       = line[5]
			strand       = line[6]
			attributes   = line[8]


			new_line = "\t".join(line)
			print(new_line)







