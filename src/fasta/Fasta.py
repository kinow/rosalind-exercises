class Fasta:
    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence

def read_fasta(text):
    items = []
    index = 0
    aninstance = None
    seq = ''
    name = ''
    for line in text.splitlines():
        if line.startswith(">"):
            if index >= 1:
                items.append(aninstance)
            index += 1
            name = line[1:]
            seq = ''
            aninstance = Fasta(name, seq)
        else:
            seq += line
            aninstance = Fasta(name, seq)

    items.append(aninstance)
    return items