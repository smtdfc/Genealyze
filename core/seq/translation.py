from .sequence import *


Translation_Tables = {
    "Standard": {
      "UUU": "F", "UUC": "F",  # Phenylalanine
      "UUA": "L", "UUG": "L",  # Leucine
      "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",  # Leucine
      "AUU": "I", "AUC": "I", "AUA": "I",  # Isoleucine
      "AUG": "M",  # Methionine (start codon)
      "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",  # Valine
      "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",  # Serine
      "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",  # Proline
      "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",  # Threonine
      "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",  # Alanine
      "UAU": "Y", "UAC": "Y",  # Tyrosine
      "UAA": "*", "UAG": "*",  # Stop codon
      "CAU": "H", "CAC": "H",  # Histidine
      "CAA": "Q", "CAG": "Q",  # Glutamine
      "AAU": "N", "AAC": "N",  # Asparagine
      "AAA": "K", "AAG": "K",  # Lysine
      "GAU": "D", "GAC": "D",  # Aspartic acid
      "GAA": "E", "GAG": "E",  # Glutamic acid
      "UGU": "C", "UGC": "C",  # Cysteine
      "UGA": "*",  # Stop codon
      "UGG": "W",  # Tryptophan
      "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",  # Arginine
      "AGU": "S", "AGC": "S",  # Serine
      "AGA": "R", "AGG": "R",  # Arginine
      "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"   # Glycine
    },
    "Vertebrate Mitochondrial": {
        "UUU": "F", "UUC": "F",
        "UUA": "L", "UUG": "L",
        "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
        "AUU": "I", "AUC": "I", "AUA": "M",
        "AUG": "M",
        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "UAU": "Y", "UAC": "Y",
        "UAA": "*", "UAG": "*",
        "CAU": "H", "CAC": "H",
        "CAA": "Q", "CAG": "Q",
        "AAU": "N", "AAC": "N",
        "AAA": "K", "AAG": "K",
        "GAU": "D", "GAC": "D",
        "GAA": "E", "GAG": "E",
        "UGU": "C", "UGC": "C",
        "UGA": "W",
        "UGG": "W",
        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
        "AGU": "S", "AGC": "S",
        "AGA": "*", "AGG": "*",
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
  },
  
}

class Translation:
  def __init__(self,seq):
    self.sequence = seq 
    
  def translate(self,table="Standard",to_end=False,cds=False,stop_symbol="*"):
    if not Translation_Tables.get(table,False):
      raise Exception("Invalid translation table !")
    
    table = Translation_Tables.get(table,{})
    seq_str = ""
    for i in range(0,len(self.sequence.seq_str),3):
      codon= self.sequence.seq_str[i:i+3]
      aa = table.get(codon,False)
      
      if not aa:
        #unknown codon
        continue
      
      if aa=="*":
        aa = stop_symbol
      
      if aa == stop_symbol and to_end ==True:
        break
      seq_str+=aa
    
    if cds:
      if not (seq_str[0] == "M" and len(seq_str) % 3 == 0):
        raise Exception("Invalid CDS Sequence")
    
    return Sequence(seq_str)
    
def translate(sequence,*args):
  return Translation(sequence).translate(*args)
  
