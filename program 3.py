from Bio import SeqIO
sequence = [(SeqIO.parse("sequence.gb", "genbank"))]
print("found  i% record")
for seq in len(sequence):
    last = sequence[-1]
    print(last.id)
    print(repr(last.seq))
    first = sequence = [0]
    print(first.id)
    print(repr(first.seq)





