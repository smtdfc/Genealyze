from core.seq.sequence import *
from core.seq.annotation import *
from .needleman_wunsch import*
from .smith_waterman import *
from .gotoh import *
from .gotoh_local import *


class Alignment:
  @staticmethod
  def needleman_wunsch(seq_1,seq_2,match=1, mismatch=-1, gap=-2):
    seq_str_1 = seq_1.seq_str
    seq_str_2 = seq_2.seq_str
    seq_aligned_1,seq_aligned_2,max_score= needleman_wunsch_alignment(seq_str_1,seq_str_2,match, mismatch, gap)
    return (
      Sequence(seq_aligned_1),
      Sequence(seq_aligned_2),
      max_score,
    )
    
  @staticmethod
  def smith_waterman(seq_1,seq_2,match=1, mismatch=-1, gap=-2):
    seq_str_1 = seq_1.seq_str
    seq_str_2 = seq_2.seq_str
    seq_aligned_1,seq_aligned_2,max_score ,scores= smith_waterman_alignment(
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
      scores
    )
  
  @staticmethod
  def gotoh(seq_1, seq_2, match_score=1, mismatch_penalty=-1, gap_open=-3, gap_extend=-1):
      seq_str_1 = seq_1.seq_str
      seq_str_2 = seq_2.seq_str
      seq_aligned_1,seq_aligned_2,max_score = gotoh_alignment(
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
  def gotoh_local(seq_1, seq_2, match_score=1, mismatch_penalty=-1, gap_open=-3, gap_extend=-1):
      seq_str_1 = seq_1.seq_str
      seq_str_2 = seq_2.seq_str
      seq_aligned_1,seq_aligned_2,max_score = gotoh_local_alignment(
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