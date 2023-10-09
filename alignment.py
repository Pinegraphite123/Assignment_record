from Bio import pairwise2
from Bio import SeqIO
from Bio.Align import substitution_matrices

blosum62 = substitution_matrices.load("BLOSUM62")
seq1 = SeqIO.read("ldha.fasta", "fasta")
seq2 = SeqIO.read("ldhb.fasta", "fasta")
alignments = pairwise2.align.globalds(seq1.seq, seq2.seq, blosum62, -10, -0.5) #or alignments = pairwise2.align.globalxx(seq1.seq, seq2.seq)
print(len(alignments))
print(pairwise2.format_alignment(*alignments[0], full_sequences=False))


