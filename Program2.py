from Bio import SeqIO
inp = input("input your string : ").upper()
sequences = SeqIO.parse("file.fasta", "fasta")
temp = []
for i in sequences:
 found = i.seq.find(inp)
 if found != -1:
  temp.append(i)
print("%i matces found are : "% len(temp))
SeqIO.write(temp, "Assig3.fasta", "fasta")
print("Successfully written to Assig3.fasta")





