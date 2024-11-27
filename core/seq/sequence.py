

class Sequence:
  def __init__(self,seq):
    self.seq_str = seq.upper()

  def count(self, element=""):
    return self.seq_str.count(element)

  def reverse(self):
    return Sequence(self.seq_str[::-1])
  
  def __str__(self):
    return self.seq_str

  def length(self):
    return len(self.seq_str)
  
  def complement(self):
    seq = self.seq_str.upper()
    complement_map = {
      'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G',
      'R': 'Y', 'Y': 'R', 'S': 'S', 'W': 'W',
      'K': 'M', 'M': 'K', 'B': 'V', 'D': 'H',
      'H': 'D', 'V': 'B', 'N': 'N'
    }
    
    complement_seq = ''.join(complement_map.get(base, base) for base in seq)
    return Sequence(complement_seq)
  
  def reverse_complement(self):
    seq = self.complement()
    seq.seq_str = seq.seq_str[::-1]
    return seq
  