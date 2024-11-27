def needleman_wunsch_alignment(seq1, seq2, match=1, mismatch=-1, gap=-2):
  n = len(seq1)
  m = len(seq2)

  dp = [[0] * (m + 1) for _ in range(n + 1)]

  for i in range(1, n + 1):
    dp[i][0] = dp[i - 1][0] + gap
  for j in range(1, m + 1):
    dp[0][j] = dp[0][j - 1] + gap

  for i in range(1, n + 1):
    for j in range(1, m + 1):
      match_score = match if seq1[i - 1] == seq2[j - 1] else mismatch
      dp[i][j] = max(
        dp[i - 1][j - 1] + match_score,
        dp[i - 1][j] + gap,
        dp[i][j - 1] + gap
      )

  aligned_seq1 = []
  aligned_seq2 = []
  i, j = n, m
  while i > 0 and j > 0:
    match_score = match if seq1[i - 1] == seq2[j - 1] else mismatch
    if dp[i][j] == dp[i - 1][j - 1] + match_score:
      aligned_seq1.append(seq1[i - 1])
      aligned_seq2.append(seq2[j - 1])
      i -= 1
      j -= 1
    elif dp[i][j] == dp[i - 1][j] + gap:
      aligned_seq1.append(seq1[i - 1])
      aligned_seq2.append('-')
      i -= 1
    else:
      aligned_seq1.append('-')
      aligned_seq2.append(seq2[j - 1])
      j -= 1

  while i > 0:
    aligned_seq1.append(seq1[i - 1])
    aligned_seq2.append('-')
    i -= 1
  while j > 0:
    aligned_seq1.append('-')
    aligned_seq2.append(seq2[j - 1])
    j -= 1

  return ''.join(reversed(aligned_seq1)), ''.join(reversed(aligned_seq2)), dp[n][m],dp

