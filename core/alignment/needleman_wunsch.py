def needleman_wunsch_alignment(seq_1, seq_2, match=1, mismatch=-1, gap=-1):
    """
    Perform global sequence alignment using the Needleman-Wunsch algorithm.

    The Needleman-Wunsch algorithm aligns two sequences by maximizing the alignment 
    score based on match, mismatch, and gap penalties. The algorithm constructs a 
    scoring matrix and then traces back through the matrix to find the optimal alignment.

    Args:
        seq_1 (str): The first sequence to align.
        seq_2 (str): The second sequence to align.
        match (int, optional): Score for matching characters (default is 1).
        mismatch (int, optional): Penalty for mismatched characters (default is -1).
        gap (int, optional): Penalty for a gap (default is -1).

    Returns:
        tuple: A tuple containing:
            - str: Aligned version of the first sequence.
            - str: Aligned version of the second sequence.
            - int: The maximum alignment score.
    """
    def diagonal(i, j):
        return match if seq_1[i-1] == seq_2[j-1] else mismatch

    n = len(seq_1)
    m = len(seq_2)

    F = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        F[i][0] = gap * i
    for j in range(m + 1):
        F[0][j] = gap * j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match_score = F[i-1][j-1] + diagonal(i, j)
            delete_score = F[i-1][j] + gap
            insert_score = F[i][j-1] + gap
            F[i][j] = max(match_score, delete_score, insert_score)

    seq_align_1 = ""
    seq_align_2 = ""
    i, j = n, m
    max_score = F[n][m]

    while i > 0 or j > 0:
        if i > 0 and j > 0 and F[i][j] == F[i-1][j-1] + diagonal(i, j):
            seq_align_1 = seq_1[i-1] + seq_align_1
            seq_align_2 = seq_2[j-1] + seq_align_2
            i -= 1
            j -= 1
        elif i > 0 and F[i][j] == F[i-1][j] + gap:
            seq_align_1 = seq_1[i-1] + seq_align_1
            seq_align_2 = "_" + seq_align_2
            i -= 1
        else:
            seq_align_1 = "_" + seq_align_1
            seq_align_2 = seq_2[j-1] + seq_align_2
            j -= 1

    return seq_align_1, seq_align_2, max_score