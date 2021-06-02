from Seq1 import Seq

folder = "../P0/Sequences/"
bases = ["A", "C", "T", "G"]
listseq = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
txt = ".txt"
print("-----| Exercise 1, Exercise 10 |------")

for sequences in listseq:
    s = Seq()
    sequence = s.read_fasta(folder + sequences + txt)
    dict_bases = s.count()
    min_value = 0
    frc_base = ""
    for base, value in dict_bases.items():
        while value > min_value:
            min_value = value
            frc_base = base

    print("Gene", sequences, " : Most frequent Base: ", frc_base)