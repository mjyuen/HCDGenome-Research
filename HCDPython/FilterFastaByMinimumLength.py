#!/usr/bin python

# FilterFastaByMinimumLength.py
# Created by Maggie Lau (maglau@princeton.edu)
# Created on July 20, 2016

# Print out contigs longer than the minimum length (incluvise) as defined by the user

# define usage message
Usage =  """Usage: FilterFastaByMinimumLength.py [contigs.fasta] [number=minimum length (inclusive)]"""

import sys
from Bio import SeqIO
import itertools
import collections

#   Check to make sure that the correct number of arguments are given
if len(sys.argv) <= 1:
    print Usage
    exit(1)

fasta = open(sys.argv[1], 'rU') # open the fasta file
n = int(float(sys.argv[2]))
infilename = sys.argv[1].split(".")
outfile = open(infilename[0] + '_' + str(n) + '.' + infilename[1], 'w')

for record in SeqIO.parse(fasta, "fasta"):
	if len(record.seq) >= n:
		SeqIO.write(record, outfile, "fasta")

fasta.close()
outfile.close()


