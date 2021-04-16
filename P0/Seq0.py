from pathlib import Path
def seq_ping():
    print("OK")

def take_out(seq):
    return seq[seq.find("\n") + 1:].replace("\n","")

def seq_read_fasta(filename):
    sequence = take_out(Path(filename).read_text())
    return sequence

def seq_len(seq):
    return len(seq)

def seq_count_base(seq,base):
    return seq.count(base)

def seq_count(seq):
    gene_dict = {'A':0,'C':0,'T':0,'G':0}
    for d in seq:
        gene_dict[d] += 1
    return gene_dict

def seq_reverse(seq):
    subsequence = seq[0:20]
    return subsequence[::-1]
def seq_complement(seq):
    base_dictionary = {"A":"T","C":"G","T":"A","G":"C"}
    list1 = []
    for l in seq:
        list1.append(base_dictionary[l])
    final_list = ''.join(list1)
    return final_list


