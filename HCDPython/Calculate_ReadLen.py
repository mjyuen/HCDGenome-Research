# This script will calculate the "average read length" which can be used as an argument in the execution command with "Calculate_stats_v2.py"

# Usage:
# $ python Calculate_stats_v2.py contig-fasta-file n prefix-of-the-mappedReads.bed-file

import sys
from Bio import SeqIO

contigs = open(sys.argv[1], 'rU')
seqlen = []
N = 0

for rec in SeqIO.parse(contigs, 'fasta'):
	seqlen.append(len(rec.seq))

for i in seqlen:
	N += 1  

avseqlen = sum(seqlen)/N
totalseqlen = sum(seqlen)

print "Average read length is: %d nt" % (avseqlen)
print "Total length is: %d nt" % (totalseqlen)
 
