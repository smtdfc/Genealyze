hydropathy_index = {
      'A': 1.8, 'R': -4.5, 'N': -3.5, 'D': -3.5, 'C': 2.5, 'Q': -3.5, 'E': -3.5,
      'G': -0.4, 'H': -3.2, 'I': 4.5, 'L': 3.8, 'K': -3.9, 'M': 1.9, 'F': 2.8,
      'P': -1.6, 'S': -0.8, 'T': -0.7, 'W': -0.9, 'Y': -1.3, 'V': 4.2
}

class SequenceCaculate:
    @staticmethod
    def cumulative_gc_content(sequence):
      sequence = sequence.seq_str
      gc_contents = []
      gc_count = 0
      for i in range(1, len(sequence) + 1):
          subsequence = sequence[:i]
          gc_count = subsequence.count('G') + subsequence.count('C')
          gc_contents.append(gc_count / i * 100)
      return gc_contents
    
    @staticmethod
    def calculate_hydropathy(protein_sequence):
      protein_sequence = protein_sequence.seq_str
      hydropathy = [hydropathy_index.get(aa, 0) for aa in protein_sequence]
      return sum(hydropathy) / len(hydropathy)
   
    @staticmethod
    def codon_usage(sequence):
      sequence = sequence.seq_str
      codons = [sequence[i:i+3] for i in range(0, len(sequence), 3)]
      codon_count = {}
      for codon in codons:
          codon_count[codon] = codon_count.get(codon, 0) + 1
      total_codons = sum(codon_count.values())
      codon_percentage = {codon: (count / total_codons) * 100 for codon, count in codon_count.items()}
      return codon_percentage
  
    
    @staticmethod
    def sequence_identity(seq1, seq2):
      if len(seq1.seq_str) != len(seq2.seq_str):
          raise ValueError("Sequences must have the same length.")
      matches = sum(1 for a, b in zip(seq1.seq_str, seq2.seq_str) if a == b)
      identity = (matches / len(seq1.seq_str)) * 100
      return identity

    @staticmethod
    def hamming_distance(seq1, seq2):
      if len(seq1.seq_str) != len(seq2.seq_str):
          raise ValueError("Sequences must have the same length.")
      return sum(el1 != el2 for el1, el2 in zip(seq1.seq_str, seq2.seq_str))
    
    @staticmethod
    def gc_content(seq):
      seq = seq.seq_str.upper()
      gc_weights = {
        'A': 0.0, 'T': 0.0, 'G': 1.0, 'C': 1.0,
        'R': 0.5, 'Y': 0.5, 'S': 1.0, 'W': 0.0,
        'K': 0.5, 'M': 0.5, 'B': 0.6667,
        'D': 0.6667, 'H': 0.3333, 'V': 0.6667,
        'N': 0.5
      }
      gc_count = 0.0
      valid_length = 0
      for base in seq:
        if base in gc_weights:
          gc_count += gc_weights[base]
          valid_length += 1
        if valid_length == 0:
          return 0.0
      gc_percentage = (gc_count / valid_length) * 100
      return gc_percentage
