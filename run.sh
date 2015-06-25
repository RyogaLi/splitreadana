#!/bin/bash

# generate a directory for each chromosome
# create chr.seeds
# chr.reads

# create chromosome array
chromosome=(chrI chrII chrIII chrIV chrV chrVI chrVII chrVIII chrIX chrX chrXI chrXII chrXIII chrXIV chrXV chrXI chrM)

if [ $1 -eq 0 ] 
then

	for i in ${chromosome[@]}
	do
		python main.py $i 5
	done
	#python main.py "chrM"

elif [ $1 -eq 10 ] 
then
	python sequence.py
elif [ $1 -eq 2 ] 
then
	python makedic.py
fi