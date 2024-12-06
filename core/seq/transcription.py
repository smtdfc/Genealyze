from .sequence import *

class Transcription:
    """
    A class to represent the transcription of a DNA sequence into an RNA sequence.

    Attributes:
        sequence (Sequence): A Sequence object representing the DNA sequence to be transcribed.

    Methods:
        back_transcribe(): Converts an RNA sequence back to its corresponding DNA sequence by replacing 'U' with 'T'.
        transcribe(): Converts a DNA sequence into its corresponding RNA sequence by replacing 'T' with 'U'.
    """
    
    def __init__(self, seq):
        """
        Initializes the Transcription object with a DNA sequence.

        Args:
            seq (Sequence): A Sequence object representing the DNA sequence to be transcribed.
        """
        self.sequence = seq

    def back_transcribe(self):
        """
        Converts an RNA sequence back to its corresponding DNA sequence.

        The function replaces 'U' with 'T' and also resolves ambiguous bases (e.g., 'R' to 'Y', 'K' to 'M').

        Returns:
            Sequence: A Sequence object representing the transcribed DNA sequence.
        """
        ambiguity_map = {
            'R': 'Y', 'Y': 'R', 'S': 'S', 'W': 'W',
            'K': 'M', 'M': 'K', 'B': 'V', 'D': 'H',
            'H': 'D', 'V': 'B', 'N': 'N'
        }
        seq_str = ''.join(ambiguity_map.get(base, base) for base in self.sequence.seq_str)
        seq_str = self.sequence.seq_str.replace("U", "T")
        return Sequence(seq_str)

    def transcribe(self):
        """
        Converts a DNA sequence into its corresponding RNA sequence.

        The function replaces 'T' with 'U' and also resolves ambiguous bases (e.g., 'R' to 'Y', 'K' to 'M').

        Returns:
            Sequence: A Sequence object representing the transcribed RNA sequence.
        """
        ambiguity_map = {
            'R': 'Y', 'Y': 'R', 'S': 'S', 'W': 'W',
            'K': 'M', 'M': 'K', 'B': 'V', 'D': 'H',
            'H': 'D', 'V': 'B', 'N': 'N'
        }
        seq_str = ''.join(ambiguity_map.get(base, base) for base in self.sequence.seq_str)
        seq_str = self.sequence.seq_str.replace("T", "U")
        return Sequence(seq_str)

def transcribe(sequence):
    """
    A utility function to transcribe a DNA sequence into an RNA sequence.

    Args:
        sequence (Sequence): A Sequence object representing the DNA sequence to be transcribed.

    Returns:
        Sequence: A Sequence object representing the transcribed RNA sequence.
    """
    return Transcription(sequence).transcribe()