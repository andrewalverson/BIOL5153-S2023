#! /usr/bin/env python3

# import modules
import argparse
import csv
from collections import defaultdict


# create an ArgumentParser object
parser = argparse.ArgumentParser(description="This script parses presidents.csv for learning dictionaries")

# add positional (required) arguments
parser.add_argument("data", help="name of the presidents data file", type=str)

# parse the actual arguments
# access argument values via `args` variable
args = parser.parse_args()

# make an empty dictionary; key = name, value = party
party = defaultdict(dict)

# make an empty dictionary; key = party name, value = cumulative num presidents in that party
party_count = defaultdict(dict)

# open the GFF file
with open(args.data) as file:

	# create a csv reader object
	reader = csv.reader(file)

	# loop over all the lines in the file
	for line in reader:
		
		# skip blank lines
		if not line:
			continue

		# skip the header line
		elif(line[0] == 'Presidency '):
			continue
		
		# else it's data
		else:
			# name = line[1]; party = line[5]
			
			# print(line[1], line[5])
			pres_name  = line[1]
			pres_party = line[5]
			# print(pres_name, pres_party)
			
			# loading our dictionary
			party[pres_name] = pres_party

			# this does the same thing, but it looks weird
			# party[line[1]] = line[5]

# print out our dictionary key-value pairs
for pres, part in party.items():
	# test whether this party is present/defined in our list
	# if we've seen this party before, this will return true
	# and we can increment our counter
	if(party_count[part]):
		party_count[part] += 1
	# else this is the first time we've seen this party
	# so we set it == 1
	else:
		party_count[part] = 1

	print("\t".join([pres, part, str(party_count[part])]))













