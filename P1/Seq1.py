class Seq:
    NULL = "NULL"
    ERROR = "ERROR"

    def __init__(self, stringbases=NULL):
        if stringbases == self.NULL:
            self.stringbases = self.NULL
            print("NULL sequence created")
            return

        for b in stringbases:
            if b not in ["A", "C", "T", "G"]:
                self.stringbases = "ERROR"
                print("Invalid sequence Created")
                return

        self.stringbases = stringbases
        print("New sequence created!")

    def __str__(self):
        return self.stringbases

    def len(self):
        if self.stringbases == self.NULL:
            return 0
        elif  self.stringbases == "ERROR":
            return 0
        else:
            return len(self.stringbases)

    def count_base(self, base):
        return self.stringbases.count(base)
    def count(self):
        d = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        if self.stringbases == self.NULL:
            d = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        elif self.stringbases == "ERROR":
            d = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        else:
            for bases in self.stringbases:
                if bases == "A":
                    d["A"] += 1
                elif bases == "C":
                    d["C"] += 1
                elif bases == "T":
                    d["T"] += 1
                else:
                    d["G"] += 1
        return d

    def seq_count_base(self, base):
        counter = 0
        if self.stringbases == self.NULL:
            counter = 0
        elif self.stringbases == "ERROR":
            counter = 0
        else:
            for element in self.stringbases:
                if element == base:
                    counter += 1
        return counter, round((counter/self.len()) * 100, 1)

    def reverse(self):
        if self.stringbases == self.NULL:
            return self.stringbases
        elif self.stringbases == "ERROR":
            return self.stringbases
        else:
            return self.stringbases[::-1]

    def complement(self):
        if self.stringbases == self.NULL:
            return self.stringbases
        elif self.stringbases == "ERROR":
            return self.stringbases
        else:
            d = {"A": "T", "T": "A", "C": "G", "G": "C"}
            newseq = ""
            for element in self.stringbases:
                newseq += d[element]
            return newseq

    def read_fasta(self, filename):
        from pathlib import Path
        file_contents = Path(filename).read_text()
        body = file_contents.split("\n")[1:]
        self.stringbases = "".join(body)
        return self



def generate_seqs(pattern, number):
    seq_list = []
    for element in range(1, number + 1):
        sequence = pattern * element
        seq_list.append(Seq(sequence))
    return seq_list


def print_seqs(seq_list):
    index = 0
    for sequence in seq_list:
        index += 1
        print(f"Sequence {index}:(Length {sequence.len()}) {sequence}")