from .sequence import *
import random

class Mutation:
    @staticmethod
    def create_random_point_mutation(sequence):
        """
        Creates a random point mutation on a DNA sequence.
        
        Parameters:
        sequence (Sequence): The original DNA sequence (e.g., 'AGCT').
        
        Returns:
        str: The mutated DNA sequence.
        """
        sequence = sequence.seq_str
        if not sequence:
            raise ValueError("The sequence must not be empty.")
        bases = ['A', 'T', 'C', 'G']
        position = random.randint(0, len(sequence) - 1)
        current_base = sequence[position]
        new_base = random.choice([base for base in bases if base != current_base])
        mutated_sequence = sequence[:position] + new_base + sequence[position + 1:]
        
        return Sequence(mutated_sequence)