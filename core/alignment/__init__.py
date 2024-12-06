from core.seq.sequence import *
from core.seq.annotation import *
from .needleman_wunsch import*
from .smith_waterman import *
from .gotoh import *
from .gotoh_local import *
from .hirschberg import *

class Alignment:
    """
    A class for performing various sequence alignment algorithms, including
    Needleman-Wunsch, Smith-Waterman, Gotoh, Hirschberg, and Gotoh Local. 

    Each method aligns two sequences and returns the aligned sequences along with
    the alignment score.
    """

    @staticmethod
    def needleman_wunsch(seq_1, seq_2, match=1, mismatch=-1, gap=-2):
        """
        Perform global sequence alignment using the Needleman-Wunsch algorithm.
        
        This algorithm aligns two sequences and returns the globally aligned 
        sequences and the alignment score.

        Parameters:
        - seq_1 (Sequence): The first sequence to be aligned.
        - seq_2 (Sequence): The second sequence to be aligned.
        - match (int): The score for matching nucleotides (default is 1).
        - mismatch (int): The penalty for mismatching nucleotides (default is -1).
        - gap (int): The penalty for introducing a gap (default is -2).

        Returns:
        - Tuple: A tuple containing two aligned sequences (Sequence objects) and the alignment score (int).
        """
        seq_str_1 = seq_1.seq_str
        seq_str_2 = seq_2.seq_str
        seq_aligned_1, seq_aligned_2, max_score = needleman_wunsch_alignment(seq_str_1, seq_str_2, match, mismatch, gap)
        return (
            Sequence(seq_aligned_1),
            Sequence(seq_aligned_2),
            max_score,
        )

    @staticmethod
    def smith_waterman(seq_1, seq_2, match=1, mismatch=-1, gap=-2):
        """
        Perform local sequence alignment using the Smith-Waterman algorithm.
        
        This algorithm aligns specific regions of two sequences (local alignment)
        and returns the aligned sequences and the maximum score.

        Parameters:
        - seq_1 (Sequence): The first sequence to be aligned.
        - seq_2 (Sequence): The second sequence to be aligned.
        - match (int): The score for matching nucleotides (default is 1).
        - mismatch (int): The penalty for mismatching nucleotides (default is -1).
        - gap (int): The penalty for introducing a gap (default is -2).

        Returns:
        - Tuple: A tuple containing two aligned sequences (Sequence objects) and the alignment score (int).
        """
        seq_str_1 = seq_1.seq_str
        seq_str_2 = seq_2.seq_str
        seq_aligned_1, seq_aligned_2, max_score = smith_waterman_alignment(
            seq_str_1,
            seq_str_2,
            match, 
            mismatch,
            gap
        )
        return (
            Sequence(seq_aligned_1),
            Sequence(seq_aligned_2),
            max_score,
        )

    @staticmethod
    def gotoh(seq_1, seq_2, match_score=1, mismatch_penalty=-1, gap_open=-3, gap_extend=-1):
        """
        Perform global sequence alignment using the Gotoh algorithm with affine gap penalties.
        
        This algorithm aligns two sequences globally with different gap-opening and 
        gap-extension penalties.

        Parameters:
        - seq_1 (Sequence): The first sequence to be aligned.
        - seq_2 (Sequence): The second sequence to be aligned.
        - match_score (int): The score for matching nucleotides (default is 1).
        - mismatch_penalty (int): The penalty for mismatching nucleotides (default is -1).
        - gap_open (int): The penalty for opening a gap (default is -3).
        - gap_extend (int): The penalty for extending a gap (default is -1).

        Returns:
        - Tuple: A tuple containing two aligned sequences (Sequence objects) and the alignment score (int).
        """
        seq_str_1 = seq_1.seq_str
        seq_str_2 = seq_2.seq_str
        seq_aligned_1, seq_aligned_2, max_score = gotoh_alignment(
            seq_str_1,
            seq_str_2,
            match_score, 
            mismatch_penalty,
            gap_open,
            gap_extend
        )
        return (
            Sequence(seq_aligned_1),
            Sequence(seq_aligned_2),
            max_score,
        )

    @staticmethod
    def hirschberg(seq_1, seq_2, match_score=1, mismatch_penalty=-1, gap=-2):
        """
        Perform global sequence alignment using the Hirschberg algorithm.
        
        The Hirschberg algorithm is a space-efficient version of the Needleman-Wunsch
        algorithm, which divides the problem into smaller subproblems and computes the
        alignment recursively.

        Parameters:
        - seq_1 (Sequence): The first sequence to be aligned.
        - seq_2 (Sequence): The second sequence to be aligned.
        - match_score (int): The score for matching nucleotides (default is 1).
        - mismatch_penalty (int): The penalty for mismatching nucleotides (default is -1).
        - gap (int): The penalty for introducing a gap (default is -2).

        Returns:
        - Tuple: A tuple containing two aligned sequences (Sequence objects).
        """
        seq_str_1 = seq_1.seq_str
        seq_str_2 = seq_2.seq_str
        seq_aligned_1, seq_aligned_2 = hirschberg_alignment(
            seq_str_1,
            seq_str_2,
            match_score, 
            mismatch_penalty,
            gap
        )
        return (
            Sequence(seq_aligned_1),
            Sequence(seq_aligned_2),
        )

    @staticmethod
    def gotoh_local(seq_1, seq_2, match_score=1, mismatch_penalty=-1, gap_open=-3, gap_extend=-1):
        """
        Perform local sequence alignment using the Gotoh algorithm with affine gap penalties.
        
        This algorithm performs local sequence alignment with distinct gap-opening and 
        gap-extension penalties.

        Parameters:
        - seq_1 (Sequence): The first sequence to be aligned.
        - seq_2 (Sequence): The second sequence to be aligned.
        - match_score (int): The score for matching nucleotides (default is 1).
        - mismatch_penalty (int): The penalty for mismatching nucleotides (default is -1).
        - gap_open (int): The penalty for opening a gap (default is -3).
        - gap_extend (int): The penalty for extending a gap (default is -1).

        Returns:
        - Tuple: A tuple containing two aligned sequences (Sequence objects) and the alignment score (int).
        """
        seq_str_1 = seq_1.seq_str
        seq_str_2 = seq_2.seq_str
        seq_aligned_1, seq_aligned_2, max_score = gotoh_local_alignment(
            seq_str_1,
            seq_str_2,
            match_score, 
            mismatch_penalty,
            gap_open,
            gap_extend
        )
        return (
            Sequence(seq_aligned_1),
            Sequence(seq_aligned_2),
            max_score,
        )