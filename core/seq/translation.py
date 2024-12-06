from .sequence import *

# Translation tables for different codon-to-amino acid mappings
Translation_Tables = {
    "Standard": { ... },  # Standard translation table
    "Vertebrate Mitochondrial": { ... },  # Vertebrate mitochondrial translation table
}

class Translation:
    """
    A class to represent the translation of an RNA sequence into a protein sequence.

    Attributes:
        sequence (Sequence): A Sequence object representing the RNA sequence to be translated.

    Methods:
        translate(table="Standard", to_end=False, cds=False, stop_symbol="*"): 
            Translates the RNA sequence into a protein sequence using the specified translation table.
    """
    
    def __init__(self, seq):
        """
        Initializes the Translation object with an RNA sequence.

        Args:
            seq (Sequence): A Sequence object representing the RNA sequence to be translated.
        """
        self.sequence = seq

    def translate(self, table="Standard", to_end=False, cds=False, stop_symbol="*"):
        """
        Translates the RNA sequence into a protein sequence.

        The function uses a translation table (default: Standard) to convert codons into amino acids.
        It also handles the optional conditions like translation ending, CDS validation, and stop codon symbol.

        Args:
            table (str): The translation table to use (default: "Standard").
            to_end (bool): If True, translation stops when a stop codon is encountered.
            cds (bool): If True, checks if the sequence is a valid CDS (starts with 'M' and length is divisible by 3).
            stop_symbol (str): The symbol used to represent the stop codon (default: "*").

        Returns:
            Sequence: A Sequence object representing the translated protein sequence.

        Raises:
            Exception: If the translation table is invalid, or if the sequence is not a valid CDS when required.
        """
        if not Translation_Tables.get(table, False):
            raise Exception("Invalid translation table!")
        
        table = Translation_Tables.get(table, {})
        seq_str = ""
        
        for i in range(0, len(self.sequence.seq_str), 3):
            codon = self.sequence.seq_str[i:i+3]
            aa = table.get(codon, False)
            
            if not aa:
                # Skip unknown codons
                continue
            
            if aa == "*":
                aa = stop_symbol
            
            if aa == stop_symbol and to_end == True:
                break
            seq_str += aa
        
        if cds:
            if not (seq_str[0] == "M" and len(seq_str) % 3 == 0):
                raise Exception("Invalid CDS Sequence")
        
        return Sequence(seq_str)
    
def translate(sequence, *args):
    """
    A utility function to translate an RNA sequence into a protein sequence.

    Args:
        sequence (Sequence): A Sequence object representing the RNA sequence to be translated.
        *args: Additional arguments to pass to the translate method.

    Returns:
        Sequence: A Sequence object representing the translated protein sequence.
    """
    return Translation(sequence).translate(*args)