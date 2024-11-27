from core.seq.sequence import *
from core.seq.annotation import *


class FASTAOpener:
  def __init__(self, path):
    self.path = path

  def read(self):
    sequences = []
    try:
      with open(self.path, "r") as file:
        sequence_id = None
        sequence = []
        for line in file:
          line = line.strip()
          if not line:
            continue
          if line.startswith(">"):
            if sequence_id:
              sequences.append(SequenceAnnotation(
                sequence_id,
                Sequence(''.join(sequence))
              ))
            sequence_id = line[1:]
            sequence = []
          else:
            sequence.append(line)
        if sequence_id:
          sequences.append(SequenceAnnotation(
            sequence_id,
            Sequence(''.join(sequence))
          ))
    except FileNotFoundError:
      raise Exception(f"File not found: {self.path}")
    except Exception as e:
      raise Exception(f"An error occurred: {e}")
    return sequences
