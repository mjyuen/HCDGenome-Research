
## This script is to extract the paired-end reads that mapped to the genome bins, whether both F & R reads mapped or one of the pairs mapped.

## input files are a list of scaffolds in the genome bins, the .bedpe file and a file containing all reads used in the Bowtie mapping analysis.

Usage = """ python GetGenomeBinReads.py [list of scaffolds in genome bins] [.bedpe file] [all reads] [output filename]"""

import sys
from Bio import SeqIO

if len(sys.argv) <= 2:
	print Usage
	exit(0)

scaffolds = open(sys.argv[1], 'rU')
bedpe = open(sys.argv[2], 'rU')
reads = open(sys.argv[3], 'rU')
out = open(sys.argv[4], 'w') 

scaffoldsDict = {}

for line in scaffolds:
	line = line.strip()
	if line not in scaffoldsDict:
		scaffoldsDict[line] = 1

readsDict ={}

for line in bedpe:
	line = line.strip()
	col = line.split('\t')
	if col[0] or col[3] in scaffoldsDict:
		readsDict[col[6]] = 1

for record in SeqIO.parse(reads, 'fasta'):
	name = record.id
	if name in readsDict:
		SeqIO.write(record, out, "fasta")

scaffolds.close()
bedpe.close()
reads.close()
out.close()

