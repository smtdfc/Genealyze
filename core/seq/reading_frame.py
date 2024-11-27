class ReadingFrameGroup:
  def __init__(self,frames=[]):
    self.frames = []

class ReadingFrame:
  @staticmethod
  def create(sequence, num_frames=3, start=0):
    frames = []
    for i in range(num_frames):
        frames.append(sequence.seq_str[start + i:])
    frames = [frame[:len(frame) - len(frame) % 3] for frame in frames]
    
    return ReadingFrameGroup([Sequence(frame) for frame in frames])
