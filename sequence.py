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
# contains a dictionary which maps the position and total number of mappings 
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

				outputList.append(region)

			if row[18] == chromosome:
				s = int(row[13])
				e = int(row[14])
				if s < e:
					region = range(s,e+1)
				elif s > e:
					region = range(e,s+1)
				outputList.append(region)

		return outputList


def findMinMax (inputlist, chromosome):
	"""
	Take a list of lists and find the min and max value in the whole lists
	"""
	max_value = 0
	min_value = chrLens.get(chromosome)

	for i in inputlist:
		if i[0] < min_value:
			min_value = min(i)

		if i[0] > max_value:
			max_value = max(i)

	results = [chromosome,min_value,max_value]
	return results


def buildLists(inputlist, infolist):
	"""
	Build a new list for each list in inputlist. Use 0 and 1 to indicate the mapped region
	infolist contains chromosome name and min&max position
	"""
	chrName = infolist[0]
	min_value = infolist[1]
	max_value = infolist[2]
	builtlist = []
	for i in inputlist:
		region = range(min_value,max_value+1)
		k = [0]*(i[0]-min_value)
		n = [1]*(len(i))
		m = [0]*(max_value-i[-1])
		built = k + n + m
		builtlist.append(built)

	return builtlist


def AssociatePos(inputlist, infolist):
	"""
	Merge the lists in inputlist, build a dictionary to map them with position
	"""
	region = range(infolist[1],infolist[2]+1)
	merge = [0]*(infolist[2]-infolist[1]+1)
	for i in inputlist:
		merge = [x + y for x, y in zip(i, merge)]
	dictionary = dict(zip(region, merge))

	print dictionary


if __name__ == "__main__":
	outputList = readFile("discord.csv", "chrV")
	infolist = findMinMax(outputList, "chrV")
	build = buildLists(outputList, infolist)
	AssociatePos(build, infolist)
	# r = trackminmax("discord.csv", "chrII")
	# build_list("discord.csv", r)
