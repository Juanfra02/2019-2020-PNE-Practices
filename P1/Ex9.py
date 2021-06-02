from Seq1 import Seq
print("------| Practice 1, Exercise 9 |------")
s = Seq()
folder = "../P0/Sequences/"
filename = "U5.txt"
FILENAME = folder + filename
s.read_fasta(FILENAME)

print(f"Sequence :(Length {s.len()}) {s}")
print(f"Bases:  {s.count()}")
print(f"Rev:   {s.reverse()}")
print(f"Comp:  {s.complement()}")
