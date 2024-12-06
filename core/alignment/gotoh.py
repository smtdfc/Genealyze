def gotoh_alignment(seq1, seq2, match_score=1, mismatch_score=-1, gap_open=-2, gap_extend=-1):
    """
    Perform global sequence alignment using the Gotoh algorithm with affine gap penalties.

    The Gotoh algorithm is an extension of the Needleman-Wunsch algorithm that handles 
    affine gap penalties, which separate gap opening and gap extension penalties. 
    It provides a more accurate alignment for sequences with gaps.

    Parameters:
    - seq1 (str): The first sequence to be aligned.
    - seq2 (str): The second sequence to be aligned.
    - match_score (int): The score for matching characters (default is 1).
    - mismatch_score (int): The penalty for mismatching characters (default is -1).
    - gap_open (int): The penalty for opening a gap (default is -2).
    - gap_extend (int): The penalty for extending a gap (default is -1).

    Returns:
    - tuple: A tuple containing three values:
      - Aligned sequence 1 (str) with gaps ('-') inserted.
      - Aligned sequence 2 (str) with gaps ('-') inserted.
      - The alignment score (int), which is the value of M[n][m] representing the best alignment score.

    The function uses dynamic programming to calculate the optimal alignment and traceback to 
    reconstruct the aligned sequences.
    """
    n = len(seq1)
    m = len(seq2)

    M = [[0] * (m + 1) for _ in range(n + 1)]
    Ix = [[float('-inf')] * (m + 1) for _ in range(n + 1)]
    Iy = [[float('-inf')] * (m + 1) for _ in range(n + 1)]
    traceback = [[None] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        Ix[i][0] = gap_open + (i - 1) * gap_extend
        M[i][0] = Ix[i][0]
        traceback[i][0] = 'U' 

    for j in range(1, m + 1):
        Iy[0][j] = gap_open + (j - 1) * gap_extend
        M[0][j] = Iy[0][j]
        traceback[0][j] = 'L'  

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            Ix[i][j] = max(Ix[i - 1][j] + gap_extend, M[i - 1][j] + gap_open + gap_extend)
            Iy[i][j] = max(Iy[i][j - 1] + gap_extend, M[i][j - 1] + gap_open + gap_extend)
            M[i][j] = max(M[i - 1][j - 1] + (match_score if seq1[i - 1] == seq2[j - 1] else mismatch_score), 
                          Ix[i][j], Iy[i][j])

            if M[i][j] == M[i - 1][j - 1] + (match_score if seq1[i - 1] == seq2[j - 1] else mismatch_score):
                traceback[i][j] = 'D' 
            elif M[i][j] == Ix[i][j]:
                traceback[i][j] = 'U'  
            else:
                traceback[i][j] = 'L'  


    aligned_seq1 = []
    aligned_seq2 = []
    i, j = n, m

    while i > 0 or j > 0:
        if traceback[i][j] == 'D':
            aligned_seq1.append(seq1[i - 1])
            aligned_seq2.append(seq2[j - 1])
            i -= 1
            j -= 1
        elif traceback[i][j] == 'U':
            aligned_seq1.append(seq1[i - 1])
            aligned_seq2.append('-')
            i -= 1
        elif traceback[i][j] == 'L':
            aligned_seq1.append('-')
            aligned_seq2.append(seq2[j - 1])
            j -= 1

    aligned_seq1.reverse()
    aligned_seq2.reverse()

    return ''.join(aligned_seq1), ''.join(aligned_seq2), M[n][m]