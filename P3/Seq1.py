import termcolor
from pathlib import Path

class Seq:
    """A class for representing sequences"""
    NULL_SEQUENCE = 'NULL'
    INVALID_SEQUENCE = 'ERROR'

    def __init__(self, strbases=NULL_SEQUENCE):
        if strbases == Seq.NULL_SEQUENCE:
            print('Null sequence created!')
            self.strbases = strbases
        else:
            self.strbases = strbases
            if self.is_valid_sequence():
                print("New sequence created!")
            else:
                self.strbases = Seq.INVALID_SEQUENCE
                print('Incorrect sequence created!')

    @staticmethod
    def is_valid_sequence_2(bases):
        for c in self.strbases:
            if c != 'A' and c != 'C' and c != 'G' and c != 'T':
                return False
        return True

    def is_valid_sequence(self):
        for c in self.strbases:
            if c != 'A' and c != 'C' and c != 'G' and c != 'T':
                return False
        return True

    @staticmethod
    def print_seqs(list_sequences):
        for i in range(0, len(list_sequences)):
            text = 'Sequence ' + str(i) + ' : (Length: ' + list_sequences[i].len() + ' ) ' + list_sequences[i]
            termcolor.cprint(text, 'yellow')

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return 0
        else:
            return len(self.strbases)

    def count_bases(self):
        a, c, t, g = 0, 0, 0, 0
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return a, c, g, t
        else:
            for ch in self.strbases:
                if ch == "A":
                    a += 1
                elif ch == "C":
                    c += 1
                elif ch == "G":
                    g += 1
                elif ch == "T":
                    t += 1
            return a, c, g, t

    def count(self):
        a, c, t, g = self.count_bases()
        return {'A': a, 'C': c, 'T': t, 'G': g}

    def percentages(self):
        a, c, t, g = self.count_bases()
        per_a = "(" + str(round(a/self.len() * 100, 1)) + "%)"
        per_c = "(" + str(round(c / self.len() * 100, 1)) + "%)"
        per_t = "(" + str(round(t / self.len() * 100, 1)) + "%)"
        per_g = "(" + str(round(g / self.len() * 100, 1)) + "%)"
        return "A: " + str(a) + "  " + per_a + "\n" + "C: " + str(c) + "  " + per_c + "\n" + "T: " + str(t) + "  " + per_t + "\n" + "G: " + str(g) + "  " + per_g

    def reverse(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return 'NULL'
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return 'ERROR'
        else:
            return self.strbases[::-1]

    def complement(self):
        complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        empty_str = ''
        if self.strbases == Seq.NULL_SEQUENCE:
            return 'NULL'
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return 'ERROR'
        else:
            for base in self.strbases:
                empty_str += complement[base]
            return empty_str

    @staticmethod
    def take_out_first_line(seq):
        return seq[seq.find('\n'):].replace('\n', '')

    def read_fasta(self, filename):
        self.strbases = Seq.take_out_first_line(Path(filename).read_text())

    @staticmethod
    def most_freq_base(base_dict):
        return max(base_dict, key=base_dict.get)


def test_sequences():
    s1 = Seq()
    s2 = Seq("TATAC")
    s3 = Seq('Invalid seq')
    return s1, s2, s3





def generate_seqs(pattern, number):
    list_seq = []
    for i in range(0, number):
        list_seq.append(Seq(pattern * (i + 1)))
    return list_seq