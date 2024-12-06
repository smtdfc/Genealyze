class FASTAOpener:
    """
    A class to read and parse FASTA files into sequences with annotations.

    The FASTA format is commonly used to represent nucleotide or peptide sequences.
    Each sequence in the file is identified by a header line starting with '>', 
    followed by lines of sequence data.

    Attributes:
        path (str): Path to the FASTA file to be read.

    Methods:
        read() -> list[SequenceAnnotation]:
            Reads and parses the FASTA file, returning a list of SequenceAnnotation objects.
    """
    def __init__(self, path):
        """
        Initialize the FASTAOpener with the path to the FASTA file.

        Args:
            path (str): The file path to the FASTA file.
        """
        self.path = path

    def read(self):
        """
        Reads the FASTA file and parses it into sequence annotations.

        Each sequence in the FASTA file is stored as a SequenceAnnotation object, 
        containing the sequence ID and the corresponding sequence.

        Returns:
            list[SequenceAnnotation]: A list of SequenceAnnotation objects parsed 
            from the FASTA file.

        Raises:
            Exception: If the file is not found or if an error occurs while reading the file.
        """
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