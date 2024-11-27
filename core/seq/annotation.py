class SequenceAnnotation:
  def __init__(self,info,seq):
    self.info = info 
    self.seq = seq
    self.name = ""
    self.description = ""
    
  def __str__(self):
    return f"Sequence Annotation: {self.info} [{self.seq.length()}]"