import Seq0

ID = "U5.txt"
GENE_FOLDER = "./sequences/"

print("DNA file:",ID)
u5_Seq = Seq0.seq_read_fasta(GENE_FOLDER + ID)
print("The first 20 bases are: ", u5_Seq[0:20])