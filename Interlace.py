
import sys
from Bio import SeqIO

Usage = """Usage: python Interlace.py [R1.fasta] [R2.fasta] [out filename]"""

if len(sys.argv) < 2:
	print Usage
	exit(1)

Forward = open(sys.argv[1], 'rU')
Reverse = open(sys.argv[2], 'rU')
output = open(sys.argv[3] + '.fasta', 'w')

Fseqdict = {}

for record in SeqIO.parse(Forward, "fasta"):
	col = record.id.split('/')
	title = col[0]
	seq = record.seq
	Fseqdict[title] = seq

for record in SeqIO.parse(Reverse, "fasta"):
	col = record.id.split('/')
	title = col[0]
	seq = record.seq
	output.write('>%s/1\n%s\n' % (title, Fseqdict[title]))
	output.write('>%s/2\n%s\n' % (title, seq))

Forward.close()
Reverse.close()
output.close()
		
