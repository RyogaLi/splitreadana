#Python 2
import pysam
import sys
import csv


###############  06/10th log ################# 
# Find the region on each chr that has the most number of splitread #
# Each chr is divided into chunks () #
chrLens={"chrI" : 249250621,"chrII" : 243199373,"chrIII" : 198022430,"chrIV" : 191154276,"chrV" : 180915260,"chrVI" : 171115067,
			"chrVII" : 159138663,"chrVIII" : 146364022,"chrIX" : 141213431,"chrX" : 135534747,"chrXI" : 135006516, 
			"chrXII" : 133851895,"chrXIII" : 115169878,"chrXIV" : 107349540,"chrXV" : 102531392,"chrXVI" : 90354753, 
			"chrXVII" : 81195210, "chrXVIII" : 78077248, "chrXIX" : 59128983,"chrXX" : 63025520,"chrXXI" : 48129895, 
			"chrXXII" : 51304566,"chrXXIII" : 155270560}

lol = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
# stout
sys.stdout = open('Output.txt', 'w')



# open the discord file
# with open('discord.csv', 'rb') as splitreadsFile:
# 	reader = csv.reader(splitreadsFile)
# 	for row in reader:
# 		for i in row:
# 			if i == "chrI":
# 				chrI.append(row)
# 			elif i == "chrII":
# 				chrII.append(row)
# 			elif i == "chrIII":
