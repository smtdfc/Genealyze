def gotoh_alignment(seq1, seq2, match_score=1, mismatch_penalty=-1, gap_open=-2, gap_extend=-1):
    n, m = len(seq1), len(seq2)

    M = [[0] * (m + 1) for _ in range(n + 1)]
    X = [[0] * (m + 1) for _ in range(n + 1)]
    Y = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        M[i][0] = float("-inf")
        X[i][0] = gap_open + (i - 1) * gap_extend
        Y[i][0] = float("-inf")

    for j in range(1, m + 1):
        M[0][j] = float("-inf")
        X[0][j] = float("-inf")
        Y[0][j] = gap_open + (j - 1) * gap_extend

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match = match_score if seq1[i - 1] == seq2[j - 1] else mismatch_penalty

            M[i][j] = max(
                M[i - 1][j - 1] + match,
                X[i - 1][j - 1] + match,
                Y[i - 1][j - 1] + match,
            )

            X[i][j] = max(M[i - 1][j] + gap_open + gap_extend, X[i - 1][j] + gap_extend)

            Y[i][j] = max(M[i][j - 1] + gap_open + gap_extend, Y[i][j - 1] + gap_extend)

    max_score = max(M[n][m], X[n][m], Y[n][m])

    return max_score, M, X, Y
