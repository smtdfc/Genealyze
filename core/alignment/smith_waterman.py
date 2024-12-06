def smith_waterman_alignment(seq_1, seq_2, match=1, mismatch=-1, gap=-2):
    """
    Perform local sequence alignment using the Smith-Waterman algorithm.

    The Smith-Waterman algorithm aligns two sequences by finding the highest-scoring 
    local alignment, allowing for mismatches and gaps. The algorithm constructs a 
    scoring matrix and traces back from the maximum score to determine the optimal 
    local alignment.

    Args:
        seq_1 (str): The first sequence to align.
        seq_2 (str): The second sequence to align.
        match (int, optional): Score for matching characters (default is 1).
        mismatch (int, optional): Penalty for mismatched characters (default is -1).
        gap (int, optional): Penalty for a gap (default is -2).

    Returns:
        tuple: A tuple containing:
            - str: Aligned portion of the first sequence.
            - str: Aligned portion of the second sequence.
            - int: The maximum alignment score.
    """
    def diagonal(i, j):
        return match if seq_1[i-1] == seq_2[j-1] else mismatch

    n = len(seq_1)
    m = len(seq_2)

    F = [[0] * (m + 1) for _ in range(n + 1)]
    max_score = 0
    max_score_pos = (0, 0)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match_score = F[i-1][j-1] + diagonal(i, j)
            delete_score = F[i-1][j] + gap
            insert_score = F[i][j-1] + gap
            F[i][j] = max(match_score, delete_score, insert_score, 0)

            if F[i][j] > max_score:
                max_score = F[i][j]
                max_score_pos = (i, j)

    seq_align_1 = ""
    seq_align_2 = ""
    i, j = max_score_pos

    while F[i][j] > 0:
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