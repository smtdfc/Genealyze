from .transcription import *
from .translation import *

class ReadingFrameGroup:
  def __init__(self,frames=[]):
    self.frames = []

  def get(self,index):
    return self.frames[index]
    
  def transcribe(self):
    sequences = []
    for seq in self.frames:
      sequences.append(transcribe(seq))
    
    return sequences

  def translate(self,*args):
    sequences = []
    for seq in self.frames:
      sequences.append(translate(seq,*args))
    
    return sequences
  

class ReadingFrame:
  @staticmethod
  def create(sequence, num_frames=3, start=0):
    frames = []
    for i in range(num_frames):
        frames.append(sequence.seq_str[start + i:])
    frames = [frame[:len(frame) - len(frame) % 3] for frame in frames]
    
    return ReadingFrameGroup([Sequence(frame) for frame in frames])
