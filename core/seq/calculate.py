class SequenceCaculate:
    
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
