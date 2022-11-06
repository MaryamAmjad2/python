from Bio import SeqIO
genbank_file = SeqIO.parse("sequence.gb", "genbank")  # downloaded from ncbi
converted_to_fasta = SeqIO.convert("sequence.gb", "genbank", "sequence.fasta", "fasta")

print("Successfully converted genbank file to fasta")
