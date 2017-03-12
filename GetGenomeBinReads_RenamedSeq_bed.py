## Created on July 22, 2016
## Creaded by Maggie Lau (maglau@princeton.edu)

## This script is to extract the paired-end reads that mapped to the genome bins, whether both F & R reads mapped or one of the pairs mapped.

## This is created for Michelle Yuen's project, in which the postQC reads have been renamed, that means, the seq in R1, R2 and singles files sharing the same title but they are not the same sequences.

## input files are (1) the reference genome of a hydrocarbon-degrading microbe, the .bed file and files containing the reads used in the Bowtie mapping analysis.

Usage = """ python GetGenomeBinReads_bed.py [.bed file] [R1 reads] [R2 reads] [U or single reads] [outfile basename]"""

import sys
from Bio import SeqIO

if len(sys.argv) <= 2:
	print Usage
	exit(0)

bed = open(sys.argv[1], 'rU')
R1 = open(sys.argv[2], 'rU')
R2 = open(sys.argv[3], 'rU')
U = open(sys.argv[4], 'rU')
R1out = open(sys.argv[5] + '_R1.fasta', 'w')
R2out = open(sys.argv[5] + '_R2.fasta', 'w')
Uout = open(sys.argv[5] + '_U.fasta', 'w')

RDict = {}
UDict = {}

for line in bed:
	line = line.strip()
	col = line.split('\t')
	if "/" not in col[3] and col[3] not in UDict:
		UDict[col[3]] = 1
	else:			
		COL = col[3].split('/')
		if COL[0] not in RDict:
			RDict[COL[0]] = 1

def screen(reads, Dict, out):
	name = None
	for record in SeqIO.parse(reads, 'fasta'):
		name = record.id
		if name in Dict:
			SeqIO.write(record, out, "fasta")

screen(R1, RDict, R1out)
screen(R2, RDict, R2out)
screen(U, UDict, Uout)

bed.close()
R1.close()
R2.close()
U.close()
R1out.close()
R2out.close()
Uout.close()



