class SequenceAnnotation:
    """
    Class representing a sequence annotation, which includes metadata and associated sequence.

    Attributes:
        info (str): Information or description related to the sequence.
        seq (Sequence): The sequence object associated with this annotation.
        name (str): The name of the sequence annotation.
        description (str): A detailed description of the sequence annotation.
    
    Methods:
        __init__(info, seq): Initializes the SequenceAnnotation object with the provided information and sequence.
        __str__(): Returns a string representation of the sequence annotation, including its info and sequence length.
    """
  
    def __init__(self, info, seq):
        """
        Initializes the SequenceAnnotation object with the provided information and sequence.

        Args:
            info (str): The metadata or information associated with the sequence annotation.
            seq (Sequence): The Sequence object associated with this annotation.
        """
        self.info = info
        self.seq = seq
        self.name = ""
        self.description = ""
    
    def __str__(self):
        """
        Returns a string representation of the sequence annotation, including its info and sequence length.

        Returns:
            str: A string in the format "Sequence Annotation: <info> [<sequence length>]" where
                 <info> is the information associated with the annotation and <sequence length>
                 is the length of the associated sequence.
        """
        return f"Sequence Annotation: {self.info} [{self.seq.length()}]"