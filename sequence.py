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

def readFile(filename, chromosome):
	"""
	Read the contents from a csv file and generate a list of lists
	 which contains all the mapped region on chromosome
	"""
	outputList=[]
	#open file to read
	with open(filename, 'rb') as splitreadsFile:
		reader = csv.reader(splitreadsFile)
		# find the start and end position of split reads
		for row in reader:
			if row[12] == chromosome:
				s = int(row[13])
				e = int(row[14])
				# dealing with reads in different orientation
				if s < e:
					region = range(s,e+1)
				elif s > e:
					region = range(e,s+1)

				outputList+=region

			if row[18] == chromosome:
				s = int(row[13])
				e = int(row[14])
				if s < e:
					region = range(s,e+1)
				elif s > e:
					region = range(e,s+1)
				outputList+=region

		print outputList


def findMinMax (inputlist):
	"""
	Take a list of lists and find the min and max value in the sublists
	"""

	

# def trackminmax(filename, chromosome):
# 	'''
# 	Read a formated csv file with filename and prints the 
# 	min base and max position on chromosome that was mapped
# 	to splitreads.
# 	'''

# 	max_num = 0
# 	min_num = chrLens.get(chromosome)
# 	# open the discord file
# 	with open(filename, 'rb') as splitreadsFile:
# 		reader = csv.reader(splitreadsFile)

# 		# find the start and end position of split reads
# 		for row in reader:
# 			# check where the split read belongs to 
# 			if row[12] == chromosome: # split read one
# 				if (int(row[13]) | int(row[14])) > max_num:
# 					max_num = max(int(row[13]), int(row[14]))
# 				if (int(row[13]) | int(row[14])) < min_num:
# 					min_num = min(int(row[13]), int(row[14]))
# 			if row[18] == chromosome: # split read two
# 			    # track start/end point of split read two
# 				if (int(row[19]) | int(row[20])) > max_num:
# 					max_num = max(int(row[19]), int(row[20]))
# 				if (int(row[19]) | int(row[20])) < min_num:
# 					min_num = min(int(row[19]), int(row[20]))

# 		#print chromosome, " min: ", min_a, min_b, " max: ", max_a, max_b
# 		results = [chromosome, min_num, max_num]
# 		print results
# 		return results


# # build lists with zero and ones for each split read match
# # merge them into one list
# def build_list(filename, results):
# 	min_value = results[1]
# 	max_value = results[2]
	
# 	with open(filename, 'rb') as splitreadsFile:
# 		reader = csv.reader(splitreadsFile)
# 		r=[]
# 		for row in reader:
# 			if row[12] == results[0]:
# 				start = int(row[13])
# 				end = int(row[14])
# 				distance = abs(start - end) + 1
# 				a1 = [0]*(min(start,end)-min_value)
# 				b1 = [1]*distance
# 				c1 = [0]*(max_value-max(start,end))
# 				buildOne = a1 + b1 + c1
# 				r.append(buildOne)
# 			if row[18] == results[0]:
# 				start = int(row[19])
# 				end = int(row[20])
# 				distance = abs(start - end) + 1
# 				a2 = [0]*(min(start,end)-min_value)
# 				b2 = [1]*distance
# 				c2 = [0]*(max_value-max(start,end))
# 				buildTwo = a2 + b2 + c2
# 				r.append(buildTwo)

# 		#print len(r[0])
# 		m = [0] * (max_value-min_value+1)
# 		#print len(m)
# 		#print m[768050]
# 		i = 0
# 		while i < len(r):
# 			m = [x + y for x, y in zip(r[i], m)]
# 			i+=1
# 		# print m
# 		print len(m)
# 		dic = {}
# 		count = 0
# 		for j in range(min_value,max_value+1):
# 			for k in m:
# 				dic[j] = m[j]
# 		print dic
# 			# k += 1
# 			# if k > 10:
# 			# 	break

# 		# zipped = [x + y for x, y in zip(buildOne, buildTwo)]


if __name__ == "__main__":
	readFile("discord.csv", "chrV")
	# r = trackminmax("discord.csv", "chrII")
	# build_list("discord.csv", r)
