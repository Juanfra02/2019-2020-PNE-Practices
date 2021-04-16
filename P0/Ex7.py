import Seq0

ID = "U5.txt"
GENE_FOLDER = "./sequences/"
print("-----|Excersise 7|-----")

u5_Seq = Seq0.seq_read_fasta(GENE_FOLDER + ID)
print("The first 20 bases are:", u5_Seq[0:20])
print("Complementary seq: ",Seq0.seq_complement(u5_Seq[0:20]))