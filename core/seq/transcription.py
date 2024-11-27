from .sequence import *

class Transcription:
  def __init__(self,seq):
    self.sequence = seq 

  def back_transcribe(self):
    ambiguity_map = {
      'R': 'Y', 'Y': 'R', 'S': 'S', 'W': 'W',
      'K': 'M', 'M': 'K', 'B': 'V', 'D': 'H',
      'H': 'D', 'V': 'B', 'N': 'N'
    }
    seq_str = ''.join(ambiguity_map.get(base, base) for base in self.sequence.seq_str)
    seq_str = self.sequence.seq_str.replace("U", "T")
    return Sequence(seq_str)

  def transcribe(self):
    ambiguity_map = {
      'R': 'Y', 'Y': 'R', 'S': 'S', 'W': 'W',
      'K': 'M', 'M': 'K', 'B': 'V', 'D': 'H',
      'H': 'D', 'V': 'B', 'N': 'N'
    }
    seq_str = ''.join(ambiguity_map.get(base, base) for base in self.sequence.seq_str)
    seq_str = self.sequence.seq_str.replace("T", "U")
    return Sequence(seq_str)

def transcribe(sequence):
  return Transcription(sequence).transcribe()
