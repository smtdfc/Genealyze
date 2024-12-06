def hirschberg_alignment(seq_1, seq_2, match=1, mismatch=-1, gap=-2):
    """
    Perform global sequence alignment using the Hirschberg algorithm.

    The Hirschberg algorithm is a space-efficient version of the Needleman-Wunsch
    algorithm that divides the alignment problem into smaller subproblems, recursively
    solving them for an optimal global alignment.

    Parameters:
    - seq_1 (str): The first sequence to be aligned.
    - seq_2 (str): The second sequence to be aligned.
    - match (int): The score for matching nucleotides (default is 1).
    - mismatch (int): The penalty for mismatching nucleotides (default is -1).
    - gap (int): The penalty for introducing a gap (default is -2).

    Returns:
    - tuple: A tuple containing two aligned sequences (str) with gaps ('_') inserted, 
             representing the optimal global alignment.
    """
    def diagonal(a, b):
        return match if a == b else mismatch

    def argmax(arr):
        max_index = 0
        max_value = arr[0]
        for i in range(1, len(arr)):
            if arr[i] > max_value:
                max_value = arr[i]
                max_index = i
        return max_index

    def NWScore(seq_1, seq_2):
        score = [[0] * (len(seq_2) + 1), [0] * (len(seq_2) + 1)]

        for j in range(1, len(seq_2) + 1):
            score[0][j] = score[0][j - 1] + gap

        for i in range(1, len(seq_1) + 1):
            score[1][0] = score[0][0] + gap

            for j in range(1, len(seq_2) + 1):
                score_sub = score[0][j - 1] + diagonal(seq_1[i - 1], seq_2[j - 1])
                score_del = score[0][j] + gap
                score_ins = score[1][j - 1] + gap
                score[1][j] = max(score_sub, score_del, score_ins)

            score[0][:] = score[1][:]

        return score[1]

    seq_align_1 = ""
    seq_align_2 = ""

    if len(seq_1) == 0:
        seq_align_1 = "_" * len(seq_2)
        seq_align_2 = seq_2

    elif len(seq_2) == 0:
        seq_align_1 = seq_1
        seq_align_2 = "_" * len(seq_1)

    elif len(seq_1) == 1 or len(seq_2) == 1:
        while len(seq_1) < len(seq_2):
            seq_1 = seq_1 + "_"
        while len(seq_2) < len(seq_1):
            seq_2 = seq_2 + "_"

        for i in range(len(seq_1)):
            seq_align_1 += seq_1[i]
            seq_align_2 += seq_2[i]
    else:
        n = len(seq_1)
        m = len(seq_2)
        seq_1_mid = n // 2

        score_left = NWScore(seq_1[:seq_1_mid], seq_2)
        score_right = NWScore(seq_1[seq_1_mid:][::-1], seq_2[::-1])

        score_sum = [score_left[i] + score_right[m - i] for i in range(m + 1)]
        seq_2_mid = argmax(score_sum)

        align_left_1, align_left_2 = hirschberg_alignment(
            seq_1[:seq_1_mid], seq_2[:seq_2_mid], match, mismatch, gap
        )
        align_right_1, align_right_2 = hirschberg_alignment(
            seq_1[seq_1_mid:], seq_2[seq_2_mid:], match, mismatch, gap
        )

        seq_align_1 = align_left_1 + align_right_1
        seq_align_2 = align_left_2 + align_right_2

    return seq_align_1, seq_align_2