#!/bin/bash                                                                
#SBATCH -t 1:00:00
#SBATCH -o output.txt

cd $WORK
echo $RANDOM
hostname
