class Sequence:
    """
    Class representing a biological sequence (such as DNA or RNA) and providing methods
    to analyze and manipulate the sequence.

    Attributes:
        seq_str (str): The sequence string, stored in uppercase.
    
    Methods:
        __init__(seq): Initializes the Sequence object with the given sequence.
        count(element): Returns the number of occurrences of a given element in the sequence.
        reverse(): Returns a new Sequence object with the reversed sequence.
        __str__(): Returns the string representation of the sequence.
        length(): Returns the length of the sequence.
        find_promoter(): Finds and returns all occurrences of the "TATAAA" promoter pattern in the sequence.
        find_terminator(): Finds and returns all occurrences of the "AATAAA" terminator pattern in the sequence.
        segment_length_analysis(motif): Analyzes and returns the positions of all occurrences of a given motif in the sequence.
        complement(): Returns a new Sequence object representing the complement of the sequence.
        reverse_complement(): Returns a new Sequence object representing the reverse complement of the sequence.
    """
  
    def __init__(self, seq):
        """
        Initializes the Sequence object with the given sequence.

        Args:
            seq (str): The sequence string to initialize the object with.
        """
        self.seq_str = seq.upper()

    def count(self, element=""):
        """
        Returns the number of occurrences of a given element in the sequence.

        Args:
            element (str): The element to count in the sequence. Defaults to an empty string, 
                           which counts the total length of the sequence.

        Returns:
            int: The count of the element in the sequence.
        """
        return self.seq_str.count(element)

    def reverse(self):
        """
        Returns a new Sequence object with the reversed sequence.

        Returns:
            Sequence: A new Sequence object with the reversed sequence.
        """
        return Sequence(self.seq_str[::-1])

    def __str__(self):
        """
        Returns the string representation of the sequence.

        Returns:
            str: The sequence string in uppercase.
        """
        return self.seq_str

    def length(self):
        """
        Returns the length of the sequence.

        Returns:
            int: The length of the sequence.
        """
        return len(self.seq_str)

    def find_promoter(self):
        """
        Finds and returns all occurrences of the "TATAAA" promoter pattern in the sequence.

        Returns:
            list: A list of Sequence objects containing the promoter sequences found.
        """
        promoter_pattern = "TATAAA"
        return [Sequence(seq) for seq in self.seq_str.find(promoter_pattern)]

    def find_terminator(self):
        """
        Finds and returns all occurrences of the "AATAAA" terminator pattern in the sequence.

        Returns:
            list: A list of Sequence objects containing the terminator sequences found.
        """
        terminator_pattern = "AATAAA"
        return [Sequence(seq) for seq in self.seq_str.find(terminator_pattern)]

    def segment_length_analysis(self, motif):
        """
        Analyzes and returns the positions of all occurrences of a given motif in the sequence.

        Args:
            motif (str): The motif to search for in the sequence.

        Returns:
            list: A list of integers representing the starting positions of the motif in the sequence.
        """
        positions = []
        sequence = self.seq_str
        for i in range(len(sequence) - len(motif) + 1):
            if sequence[i:i + len(motif)] == motif:
                positions.append(i)
        return positions

    def complement(self):
        """
        Returns a new Sequence object representing the complement of the sequence.

        Returns:
            Sequence: A new Sequence object with the complement sequence.
        """
        seq = self.seq_str.upper()
        complement_map = {
            'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G',
            'R': 'Y', 'Y': 'R', 'S': 'S', 'W': 'W',
            'K': 'M', 'M': 'K', 'B': 'V', 'D': 'H',
            'H': 'D', 'V': 'B', 'N': 'N'
        }
        complement_seq = ''.join(complement_map.get(base, base) for base in seq)
        return Sequence(complement_seq)

    def reverse_complement(self):
        """
        Returns a new Sequence object representing the reverse complement of the sequence.

        Returns:
            Sequence: A new Sequence object with the reverse complement sequence.
        """
        seq = self.complement()
        seq.seq_str = seq.seq_str[::-1]
        return seq