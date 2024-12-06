from .transcription import *
from .translation import *

class ReadingFrameGroup:
    """
    A class to represent a group of reading frames, which includes methods for transcription and translation.

    Attributes:
        frames (list): A list of ReadingFrame objects.

    Methods:
        get(index): Retrieves the reading frame at the specified index.
        transcribe(): Transcribes all reading frames in the group into RNA sequences.
        translate(*args): Translates all reading frames in the group into protein sequences.
    """
    
    def __init__(self, frames=[]):
        """
        Initializes the ReadingFrameGroup with a list of ReadingFrame objects.

        Args:
            frames (list, optional): A list of ReadingFrame objects to initialize the group with. Defaults to an empty list.
        """
        self.frames = []

    def get(self, index):
        """
        Retrieves the reading frame at the specified index.

        Args:
            index (int): The index of the reading frame to retrieve.

        Returns:
            ReadingFrame: The reading frame at the specified index.
        """
        return self.frames[index]
    
    def transcribe(self):
        """
        Transcribes all reading frames in the group into RNA sequences.

        Returns:
            list: A list of RNA sequences corresponding to the transcription of each reading frame.
        """
        sequences = []
        for seq in self.frames:
            sequences.append(transcribe(seq))
        return sequences

    def translate(self, *args):
        """
        Translates all reading frames in the group into protein sequences.

        Args:
            *args: Additional arguments to pass to the translation function.

        Returns:
            list: A list of protein sequences corresponding to the translation of each reading frame.
        """
        sequences = []
        for seq in self.frames:
            sequences.append(translate(seq, *args))
        return sequences


class ReadingFrame:
    """
    A class to represent a single reading frame, which is derived from a DNA sequence.

    Methods:
        create(sequence, num_frames=3, start=0): Creates a group of reading frames from a DNA sequence.
    """
    
    @staticmethod
    def create(sequence, num_frames=3, start=0):
        """
        Creates a group of reading frames from a given DNA sequence.

        Args:
            sequence (Sequence): A Sequence object representing the DNA sequence.
            num_frames (int, optional): The number of reading frames to create. Defaults to 3.
            start (int, optional): The starting position in the sequence to begin the reading frames. Defaults to 0.

        Returns:
            ReadingFrameGroup: A group of reading frames derived from the given sequence.
        """
        frames = []
        for i in range(num_frames):
            frames.append(sequence.seq_str[start + i:])
        frames = [frame[:len(frame) - len(frame) % 3] for frame in frames]
        
        return ReadingFrameGroup([Sequence(frame) for frame in frames])