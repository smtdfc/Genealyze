def gotoh_local_alignment(seq1, seq2, match_score=1, mismatch_score=-1, gap_open=-2, gap_extend=-1):
    n = len(seq1)
    m = len(seq2)


    M = [[0] * (m + 1) for _ in range(n + 1)]
    Ix = [[float('-inf')] * (m + 1) for _ in range(n + 1)]
    Iy = [[float('-inf')] * (m + 1) for _ in range(n + 1)]
    traceback = [[None] * (m + 1) for _ in range(n + 1)]

    max_score = 0
    max_pos = (0, 0)


    for i in range(1, n + 1):
        for j in range(1, m + 1):
            Ix[i][j] = max(Ix[i - 1][j] + gap_extend, M[i - 1][j] + gap_open + gap_extend)
            Iy[i][j] = max(Iy[i][j - 1] + gap_extend, M[i][j - 1] + gap_open + gap_extend)
            M[i][j] = max(0,  
                          M[i - 1][j - 1] + (match_score if seq1[i - 1] == seq2[j - 1] else mismatch_score), 
                          Ix[i][j], 
                          Iy[i][j])

            if M[i][j] > max_score:
                max_score = M[i][j]
                max_pos = (i, j)

            
            if M[i][j] == 0:
                traceback[i][j] = None  
            elif M[i][j] == M[i - 1][j - 1] + (match_score if seq1[i - 1] == seq2[j - 1] else mismatch_score):
                traceback[i][j] = 'D'  
            elif M[i][j] == Ix[i][j]:
                traceback[i][j] = 'U'  
            else:
                traceback[i][j] = 'L'  

    aligned_seq1 = []
    aligned_seq2 = []
    i, j = max_pos

    while i > 0 and j > 0 and M[i][j] != 0:
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

    return ''.join(aligned_seq1), ''.join(aligned_seq2), max_score


