#!/usr/bin/python
import sys
import csv
import collections

def makedic(filename, chromosome):
	"""
	Make a dictionary for split reads on each chromosome
	Returns a dictionary: {start posicion: [endposition, "direction", "sequence", "assembled sequence", "read pair name"]}
	"""
	reads = {}
	with open(filename, 'rb') as splitreadsFile:
		reader = csv.reader(splitreadsFile)
		# find the start and end position of split reads
		# indicate directions
		for row in reader:
			if row[12] == chromosome:
				# start posicion: [endposition, "direction", "sequence", "assembled sequence", "read pair name"]
				reads[row[13]] = [row[14], row[17], row[15], row[-2], row[2]]
				reads[row[19]] = [row[20], row[23], row[21], row[-2], row[2]]

	return reads

################################## MAIN ########################################

# if __name__ == "__main__":
# 	makedic("discord.csv", "chrV")