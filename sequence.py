#!/usr/bin/python
import pysam
import sys
import csv

# chr lens value in a dictionary
chrLens={"chrI" : 249250621,"chrII" : 243199373,"chrIII" : 198022430,"chrIV" : 191154276,"chrV" : 180915260,
         "chrVI" : 171115067, "chrVII" : 159138663,"chrVIII" : 146364022,"chrIX" : 141213431,"chrX" : 135534747,
         "chrXI" : 135006516,  "chrXII" : 133851895,"chrXIII" : 115169878,"chrXIV" : 107349540,"chrXV" : 102531392,
         "chrXVI" : 90354753,  "chrXVII" : 81195210, "chrXVIII" : 78077248, "chrXIX" : 59128983,"chrXX" : 63025520,
         "chrXXI" : 48129895,  "chrXXII" : 51304566,"chrXXIII" : 155270560}

# stout to Output.txt
sys.stdout = open('Output.txt', 'w')


def trackminmax(filename, chromosome):
	'''
	Read a formated csv file with filename and prints the 
	min base and max position on chromosome that was mapped
	to splitreads.
	'''
	track_a1 = []
	track_a2 = []
	track_b1 = []
	track_b2 = []

	# open the discord file
	with open(filename, 'rb') as splitreadsFile:
		reader = csv.reader(splitreadsFile)

		# find the start and end position of split reads
		for row in reader:
			# check where the split read belongs to 
			if row[12] == chromosome: # split read one
				# track start/end point of split read one
				track_a1.append(int(row[13]))
				track_a2.append(int(row[14]))

			if row[18] == chromosome: # split read two
			    # track start/end point of split read two
				track_b1.append(int(row[19]))
				track_b2.append(int(row[20]))

		min_a = [min(track_a1), min(track_a2)]
		min_b = [min(track_b1), min(track_a1)]

		max_a = [max(track_a1), max(track_a2)]
		max_b = [max(track_b1), max(track_a1)]

	# 	print chromosome, " min: ", min_a, min_b, " max: ", max_a, max_b
		print chromosome, " min: ", min(min_a+min_b), " max: ", max(max_a+max_b)



if __name__ == "__main__":
	trackminmax("discord.csv", "chrI")
	trackminmax("discord.csv", "chrII")
	trackminmax("discord.csv", "chrIII")
