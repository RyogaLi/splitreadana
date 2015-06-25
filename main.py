#!/usr/bin/python
from makedic import *
from sequence import *
import sys
import os
from collections import OrderedDict


if __name__ == "__main__":
	# create files for output
	chromosome = sys.argv[1]

	# change file name here
	# seedsFile = chromosome + ".splitreads"
	seedsFile = chromosome + ".seeds"
	sys.stdout = open(seedsFile, 'w')
	thresh = sys.argv[2]

	# process data in .csv file
	outputList = readFile("discord.csv", chromosome)
	infolist = findMinMax(outputList, chromosome)
	build = buildLists(outputList, infolist)
	d = AssociatePos(build, infolist)

	# creates a dictionary of all the reads
	reads = makedic("discord.csv", chromosome)

	# divide d into bins with consecutive numbers
	c = collapse(d)

	# get the start and end position
	readsPos = reads.keys()
	title = ""
	sequences = []
	
	# seeds = ""
	# sreads = ""
	# for each dictionary in collapsed d
	for b in c:
		count = 0
		areads = ""
		for i in b.keys():

			if str(i) in readsPos:
				count += 1
				# assemble output files
				# reads title
				title = ">" + chromosome + "|" + str(i) + "|" + reads[str(i)][0] + "|" + reads[str(i)][1] + "\n"
				# split reads sequence
				split = reads[str(i)][2] + "\n" 
				# assembled sequences
				assembled = reads[str(i)][3] + "\n"
				# read pair name 
				name = reads[str(i)][4]

				#######################################################################
				# get rid of duplicates
				if assembled not in sequences:
					sequences.append(assembled)
					areads += ">" + name + title + assembled
				#######################################################################
				# splitreads are seperated in bins and printed along with their assembled sequences
				# sreads += title + split + assembled
		#sreads += "================================\n"
	# print sreads
		################################################################################
		# print assembled sequences to file 
		# select based on threshold provided by user
		if count >= thresh:
			print areads

	# create seeds file


