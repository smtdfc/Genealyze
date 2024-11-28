def smith_waterman_alignment(seq_1, seq_2, match=1, mismatch=-1, gap=-2):
    def diagonal(i, j):
      return match if seq_1[i-1] == seq_2[j-1] else mismatch
    
    n = len(seq_1)
    m = len(seq_2)
    
    F = [[0] * (m + 1) for _ in range(n + 1)]
    max_score = 0
    max_score_pos = (0,0)
    
    for i in range(1,n):
      for j in range(1,m):
        match_score = F[i-1][j-1] + diagonal(i, j)
        delete_score = F[i-1][j] + gap
        insert_score = F[i][j-1] + gap
        F[i][j] = max(match_score, delete_score, insert_score,0)
        
        if F[i][j] > max_score:
          max_score = F[i][j]
          max_score_pos=(i,j)
    
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
    return seq_align_1,seq_align_2,max_score

