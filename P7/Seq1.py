import termcolor
from pathlib import Path


class Seq:
    BASES_VALID = ["A", "C", "G", "T"]

    def __init__(self, bases="NULL"):
        if bases == "NULL":
            print("NULL Sequence created!")
            self.bases = bases
            return

        for c in bases:
            if c not in Seq.BASES_VALID:
                self.bases = "ERROR"
                print("INCORRECT Sequence detected!")
                return
        self.bases = bases
        print("New Sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""
        return self.bases

    def len(self):
        """Calculate the length of the sequence"""
        if self.bases == "NULL" or self.bases == "ERROR":
            return 0
        return len(self.bases)

    def count_base(self, base):
        if self.bases == "NULL" or self.bases == "ERROR":
            return 0
        return self.bases.count(base)

    def percentage_base(self, base):
        if self.bases == "NULL" or self.bases == "ERROR":
            return 0
        return (self.count_base(base) * 100) / self.len()

    def read_fasta(self, filename):
        file_contents = Path(filename).read_text()
        body = file_contents.splitlines()[1:]
        self.bases = ""
        for line in body:
            self.bases += line

    def count(self):
        result = {}
        for base in Seq.BASES_VALID:
            result[base] = self.count_base(base)
        return result

    def info(self):
        result = f"Total length: {self.len()}\n"
        for base, count in self.count().items():
            result += f"{base}: {count} ({self.percentage_base(base)}%)"
        return result

    def complement(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return self.bases

        result = ""
        complements = {"A": "T", "T": "A", "C": "G", "G": "C"}
        for base in self.bases:
            result += complements[base]
        return result

    def reverse(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return self.bases
        return self.bases[::-1]

    def frequent_base(dict_count):
        return max(dict_count, key=dict_count.get)