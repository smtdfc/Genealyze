from collections import Counter
import math

hydropathy_index = {
      'A': 1.8, 'R': -4.5, 'N': -3.5, 'D': -3.5, 'C': 2.5, 'Q': -3.5, 'E': -3.5,
      'G': -0.4, 'H': -3.2, 'I': 4.5, 'L': 3.8, 'K': -3.9, 'M': 1.9, 'F': 2.8,
      'P': -1.6, 'S': -0.8, 'T': -0.7, 'W': -0.9, 'Y': -1.3, 'V': 4.2
}

class SequenceCaculate:
    """
    A class for various sequence analysis and calculations, such as GC content, hydropathy index, 
    codon usage, sequence identity, and Hamming distance.

    Methods:
        cumulative_gc_content(sequence): Calculates the cumulative GC content for a given sequence.
        calculate_hydropathy(protein_sequence): Computes the hydropathy index of a given protein sequence.
        codon_usage(sequence): Calculates the usage frequency of each codon in a DNA sequence.
        sequence_identity(seq1, seq2): Calculates the percentage identity between two sequences.
        hamming_distance(seq1, seq2): Computes the Hamming distance between two sequences.
        gc_content(seq): Calculates the GC content of a sequence, accounting for ambiguous bases.
        tm_wallace_rule(seq): Calculate melting temperature (Tₘ) using Wallace rule.
        tm_marmur_doty(seq): Calculate melting temperature (Tₘ) using Marmur-Doty formula.
        tm_santalucia(seq): Calculate melting temperature (Tₘ) using SantaLucia formula.
        calculate_entropy(seq): Calculate the entropy of a DNA or protein sequence.
    """

    @staticmethod
    def cumulative_gc_content(sequence):
        """
        Calculates the cumulative GC content for a given sequence, which shows the GC content 
        of subsequences starting from the first base to each subsequent base.

        Args:
            sequence (Sequence): A sequence object representing the DNA or RNA sequence.

        Returns:
            list: A list of GC content percentages for subsequences of the given sequence.
        """
        sequence = sequence.seq_str
        gc_contents = []
        gc_count = 0
        for i in range(1, len(sequence) + 1):
            subsequence = sequence[:i]
            gc_count = subsequence.count('G') + subsequence.count('C')
            gc_contents.append(gc_count / i * 100)
        return gc_contents

    @staticmethod
    def calculate_hydropathy(protein_sequence):
        """
        Calculates the hydropathy index of a protein sequence using a predefined set of hydropathy values.

        Args:
            protein_sequence (Sequence): A sequence object representing the protein sequence (amino acids).

        Returns:
            float: The average hydropathy index of the sequence.
        """
        protein_sequence = protein_sequence.seq_str
        hydropathy = [hydropathy_index.get(aa, 0) for aa in protein_sequence]
        return sum(hydropathy) / len(hydropathy)

    @staticmethod
    def codon_usage(sequence):
        """
        Calculates the usage frequency of each codon in a DNA sequence.

        Args:
            sequence (Sequence): A sequence object representing the DNA sequence.

        Returns:
            dict: A dictionary with codons as keys and their usage percentages as values.
        """
        sequence = sequence.seq_str
        codons = [sequence[i:i+3] for i in range(0, len(sequence), 3)]
        codon_count = {}
        for codon in codons:
            codon_count[codon] = codon_count.get(codon, 0) + 1
        total_codons = sum(codon_count.values())
        codon_percentage = {codon: (count / total_codons) * 100 for codon, count in codon_count.items()}
        return codon_percentage

    @staticmethod
    def sequence_identity(seq1, seq2):
        """
        Calculates the percentage identity between two sequences by comparing their aligned bases.

        Args:
            seq1 (Sequence): The first sequence object.
            seq2 (Sequence): The second sequence object.

        Returns:
            float: The percentage identity between the two sequences.

        Raises:
            ValueError: If the sequences have different lengths.
        """
        if len(seq1.seq_str) != len(seq2.seq_str):
            raise ValueError("Sequences must have the same length.")
        matches = sum(1 for a, b in zip(seq1.seq_str, seq2.seq_str) if a == b)
        identity = (matches / len(seq1.seq_str)) * 100
        return identity

    @staticmethod
    def hamming_distance(seq1, seq2):
        """
        Computes the Hamming distance between two sequences, which is the number of positions 
        at which the corresponding symbols are different.

        Args:
            seq1 (Sequence): The first sequence object.
            seq2 (Sequence): The second sequence object.

        Returns:
            int: The Hamming distance between the two sequences.

        Raises:
            ValueError: If the sequences have different lengths.
        """
        if len(seq1.seq_str) != len(seq2.seq_str):
            raise ValueError("Sequences must have the same length.")
        return sum(el1 != el2 for el1, el2 in zip(seq1.seq_str, seq2.seq_str))

    @staticmethod
    def gc_content(seq):
        """
        Calculates the GC content of a sequence, taking into account ambiguous bases (e.g., R, Y, S).

        Args:
            seq (Sequence): A sequence object representing the DNA sequence.

        Returns:
            float: The GC content percentage of the sequence.
        """
        seq = seq.seq_str.upper()
        gc_weights = {
            'A': 0.0, 'T': 0.0, 'G': 1.0, 'C': 1.0,
            'R': 0.5, 'Y': 0.5, 'S': 1.0, 'W': 0.0,
            'K': 0.5, 'M': 0.5, 'B': 0.6667,
            'D': 0.6667, 'H': 0.3333, 'V': 0.6667,
            'N': 0.5
        }
        gc_count = 0.0
        valid_length = 0
        for base in seq:
            if base in gc_weights:
                gc_count += gc_weights[base]
                valid_length += 1
            if valid_length == 0:
                return 0.0
        gc_percentage = (gc_count / valid_length) * 100
        return gc_percentage
    
    @staticmethod
    def tm_wallace_rule(sequence):
        """
        Calculate melting temperature (Tₘ) using Wallace rule.
        
        Parameters:
        sequence (Sequence): DNA sequence.
        
        Returns:
        float: Melting temperature (Tₘ) in Celsius.
        """
        sequence = sequence.seq_str.upper()
        A_count = sequence.count("A")
        T_count = sequence.count("T")
        G_count = sequence.count("G")
        C_count = sequence.count("C")
        return 2 * (A_count + T_count) + 4 * (G_count + C_count)
    
    @staticmethod
    def tm_marmur_doty(sequence, na_concentration):
        """
        Calculate melting temperature (Tₘ) using Marmur-Doty formula.
        
        Parameters:
        sequence (Sequence): DNA sequence.
        na_concentration (float): Sodium ion concentration (mol/L).
        
        Returns:
        float: Melting temperature (Tₘ) in Celsius.
        """
        sequence = sequence.seq_str.upper()
        G_count = sequence.count("G")
        C_count = sequence.count("C")
        GC_content = (G_count + C_count) / len(sequence) * 100
        length = len(sequence)
        return 81.5 + 16.6 * math.log10(na_concentration) + 0.41 * GC_content - (500 / length)
    
    @staticmethod
    def tm_santalucia(sequence, dna_concentration, na_concentration):
        """
        Calculate melting temperature (Tₘ) using SantaLucia formula.
        
        Parameters:
        sequence (Sequence): DNA sequence.
        dna_concentration (float): DNA concentration (mol/L).
        na_concentration (float): Sodium ion concentration (mol/L).
        
        Returns:
        float: Melting temperature (Tₘ) in Celsius.
        """
        nearest_neighbor_params = {
            "AA": (-7.6, -21.3), "TT": (-7.6, -21.3),
            "AT": (-7.2, -20.4), "TA": (-7.2, -21.3),
            "CA": (-8.5, -22.7), "TG": (-8.5, -22.7),
            "GT": (-8.4, -22.4), "AC": (-8.4, -22.4),
            "CT": (-7.8, -21.0), "AG": (-7.8, -21.0),
            "GA": (-8.2, -22.2), "TC": (-8.2, -22.2),
            "CG": (-10.6, -27.2), "GC": (-9.8, -24.4),
            "GG": (-8.0, -19.9), "CC": (-8.0, -19.9),
        }
        
        sequence = sequence.seq_str.upper()
        R = 1.987  # Universal gas constant in cal/(mol·K)
        total_enthalpy = 0.0
        total_entropy = 0.0
    
        for i in range(len(sequence) - 1):
            pair = sequence[i:i + 2]
            if pair in nearest_neighbor_params:
                enthalpy, entropy = nearest_neighbor_params[pair]
                total_enthalpy += enthalpy
                total_entropy += entropy
    
        total_entropy += 0.368 * len(sequence) * math.log(na_concentration)
        dna_concentration_effective = dna_concentration / 4  # Adjust for duplex formation
        tm_kelvin = total_enthalpy / (total_entropy + R * math.log(dna_concentration_effective))
        tm_celsius = tm_kelvin - 273.15
        return tm_celsius
    
    @staticmethod
    def calculate_entropy(sequence):
        """
        Calculate the entropy of a DNA or protein sequence.
        
        Parameters:
        sequence (Sequence): The input sequence (e.g., "AGCTAGCT").
        
        Returns:
        float: The entropy of the sequence.
        """
        sequence = sequence.seq_str
        if not sequence:
            raise ValueError("The sequence must not be empty.")
        
        frequency = Counter(sequence)
        total_length = len(sequence)
        probabilities = [freq / total_length for freq in frequency.values()]
        entropy = -sum(p * math.log2(p) for p in probabilities)
        
        return entropy

