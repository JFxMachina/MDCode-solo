#!/usr/bin/env bash

yn(){
	echo $1 [Y/n]
	for i in {1..3}; do
		read ans
		if [[ $ans == Y ]]; then
			return 1
		elif [[ $ans == n ]]; then
			return 0
		else
			echo "Please answer with either 'Y' (yes) or 'n' (no)."
			echo $1 [Y/n]
		fi
	done
	return 0
}

mkdir tmQM > /dev/null 2> /dev/null # surpress error in case folder exists
echo "=============================="
echo "Downloading tmQM dataset into:"
echo $PWD"/tmQM"
yn "Would you like to continue?"
if [[ 0 -eq $? ]]; then
    echo "Aborting."
    echo "=============================="
    exit 1
fi
echo "------------------------------"
wget -O - http://quantum-machine.org/data/tmQM/tmQM_X.xyz.gz |
    gunzip > tmQM/tmQM_X.xyz
wget -O -  http://quantum-machine.org/data/tmQM/tmQM_y.csv.gz |
    gunzip > tmQM/tmQM_y.csv
echo "------------------------------"
echo "Done"
echo "=============================="

