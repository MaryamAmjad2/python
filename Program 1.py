from Bio import SeqIO
from Bio import Entrez
Entrez.email = "fa20-bcs-009@cuiatk.edu.pk"
gen_file = Entrez.efetch(id="HE805982.1", db="nucleotide", rettype="gb", retmode="txt" )
fas_file="File.fasta"
inp=open(gen_file,"r")
out=open(fas_file,"w")
for seq_record in SeqIO.parse(inp,"genbank"):
 out.write(">%s %s\n%s\n" %(
     seq_record.id,
     seq_record.description,
     seq_record.seq))
 out.close()
 inp.close()






