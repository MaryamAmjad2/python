from Bio import SeqIO

sequences = SeqIO.parse("ls_orchid.fasta", "fasta")
input_str = input("Enter the string: ")

matched_sequences = []

for seq in sequences: 
    is_found = seq.seq.find(input_str)
    
    if is_found != -1:
        matched_sequences.append(seq)

print("%i matches found: "% len(matched_sequences))
