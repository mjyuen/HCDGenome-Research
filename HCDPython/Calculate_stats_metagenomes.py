# Created by Maggie Lau (maglau@princeton.edu)
# Created on Dec 17, 2015

# This script will generate "_contig_stat.txt" that contains the basic stats of the input contig file (metagenome assembly)


Usage = """python Calculate_stats_metagenomes.py contig-fasta-file"""

import os 
import sys
from Bio import SeqIO

if len(sys.argv) <= 1:
	print Usage
	exit(1)

contigs = open(sys.argv[1], 'rU')
file_name = sys.argv[1][:-3] + "_stat.txt"
file_name = os.path.basename(file_name)
stat = open(file_name, 'w')

seqlen = []
N = 0

for rec in SeqIO.parse(contigs, 'fasta'):
	seqlen.append(len(rec.seq))

for i in seqlen:
	N += 1  

avseqlen = sum(seqlen)/N

##### number of contigs longer than 1k, 3k and 5k #####

fiveKB = 0
threeKB = 0
oneKB = 0

for i in sorted(seqlen, reverse=True):
	if i >= 5000:
		fiveKB += 1
		threeKB += 1
		oneKB += 1
	elif i >= 3000:
		threeKB += 1
		oneKB += 1
	elif i >= 1000:
		oneKB += 1

##### N50 #####

N50 = 0
N50con = 0
testsum = 0 

for i in sorted(seqlen, reverse=True):
	testsum += i
	N50con += 1
	if sum(seqlen)/2.0 < testsum:
		N50 = i
		break # critical 

##### N90 #####

N90 = 0
N90con = 0
testsum = 0

for i in sorted(seqlen, reverse=True):
	testsum += i
	N90con += 1
	if sum(seqlen)*0.9 < testsum:
		N90 = i
		break # critical

stat.write('input file: %s\n' % (sys.argv[1]))
stat.write('number of contigs: %d\n' % (N))
stat.write('number of bases (bp): %d\n' % (sum(seqlen)))
stat.write('max contig length (bp): %d\n' % (max(seqlen)))
stat.write('min contig length (bp): %d\n' % (min(seqlen)))
stat.write('average contig length (bp): %d\n' % (avseqlen))
stat.write('number of contigs longer than 1 kb: %d\n' % (oneKB))
stat.write('number of contigs longer than 3 kb: %d\n' % (threeKB))
stat.write('number of contigs longer than 5 kb: %d\n' % (fiveKB))
stat.write('N50 length (bp): %d \n' % (N50))
stat.write('N50 contig: %d\n' % (N50con))
stat.write('N90 length (bp): %d\n' % (N90))
stat.write('N90 contig: %d\n' % (N90con))

contigs.close()
stat.close()



