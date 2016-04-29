########################################################################
#    USAGE:
#       python3 TranslatingRNAintoProtein.py
#   DESCRIPTION:
#       Translate an RNA sequence into a Protein sequence
#   ROSALIND PROBLEM:
#       http://rosalind.info/problems/prot/
#-----------------------------------------------------------------------
#   CREATED BY: Deborah Perez
#   VERSION:    20160429
########################################################################

import sys

# ---Dictionary---------------------------------------------------------
# Dictionary translates rna to its corresponding amino acid
rnaTranslator = {"UUU" : "F", "UUC" : "F", "UUA" : "L", "UUG" : "L", \
                 "UCU" : "S", "UCC" : "S", "UCA" : "S", "UCG" : "S", \
                 "UAU" : "Y", "UAC" : "Y", "UAA" : "X", "UAG" : "X", \
                 "UGU" : "C", "UGC" : "C", "UGA" : "X", "UGG" : "W", \
                 "CUU" : "L", "CUC" : "L", "CUA" : "L", "CUG" : "L", \
                 "CCU" : "P", "CCC" : "P", "CCA" : "P", "CCG" : "P", \
                 "CAU" : "H", "CAC" : "H", "CAA" : "Q", "CAG" : "Q", \
                 "CGU" : "R", "CGC" : "R", "CGA" : "R", "CGG" : "R", \
                 "AUU" : "I", "AUC" : "I", "AUA" : "I", "AUG" : "M", \
                 "ACU" : "T", "ACC" : "T", "ACA" : "T", "ACG" : "T", \
                 "AAU" : "N", "AAC" : "N", "AAA" : "K", "AAG" : "K", \
                 "AGU" : "S", "AGC" : "S", "AGA" : "R", "AGG" : "R", \
                 "GUU" : "V", "GUC" : "V", "GUA" : "V", "GUG" : "V", \
                 "GCU" : "A", "GCC" : "A", "GCA" : "A", "GCG" : "A", \
                 "GAU" : "D", "GAC" : "D", "GAA" : "E", "GAG" : "E", \
                 "GGU" : "G", "GGC" : "G", "GGA" : "G", "GGG" : "G"}
# ----------------------------------------------------------------------

# ---_translation-------------------------------------------------------
# Creates a list from the string slicing at every nth place, n=3
def _translation(rna):
    codonLists = create_codon_frames(rna)
# loops through the list applying the dictionary
# loop will stop while not translating "X"
    for frame in codonLists:
        protein = []
        for codon in frame:
            aminoAcid = rnaTranslator[codon]
            if aminoAcid != "X":
                protein.append(aminoAcid)
            else:
                codonList[frame] = protein
    return codonLists
# ---create_codon_frames-------------------------------------------------
def create_codon_frames(rna):
    codonLists = {}
# For all 6 frame translations start reading at +1, then +2, apply
# reverseComplement and begin read at positions 0, +1 and +2
    for strand in rna:
        codonLists['Frame1'] = [strand[i:i+3] for i in \
                              range(0, len(strand), 3)]
        codonLists['Frame2'] = [strand[i+1:i+4] for i in \
                              range(0, len(strand), 3)]
        codonLists['Frame3'] = [strand[i+2:i+5] for i in \
                              range(0, len(strand), 3)]
# Assure codon frames are even lists of 3's
    for codonFrame in codonLists:
        if len(codonFrame) % 3 == 1:
            del codonFrame[-1]
        if len(codonFrame) % 3 == 2:
            del codonFrame[-2]
    return codonLists
#---MAINCODE------------------------------------------------------------
rna = sys.stdin.read().splitlines()
# If text file is in FASTA format, delete first line of rna
#del rna[0]
print (_translation(rna))
#-----------------------------------------------------------------------
