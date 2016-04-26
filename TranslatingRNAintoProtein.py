########################################################################
#    USAGE:
#       python3 TranslatingRNAintoProtein.py
#   DESCRIPTION:
#       Translate an RNA sequence into a Protein sequence
#   ROSALIND PROBLEM:
#       http://rosalind.info/problems/prot/
#-----------------------------------------------------------------------
#   CREATED BY: Deborah Perez
#   VERSION:    20160426
########################################################################

import sys   

# Dictionary to translate RNA to protein
 rnaDictionary = {"UUU" : "F", "UUC" : "F", "UUA" : "L", "UUG" : "L", "UCU" : "S", "UCC" : "S", "UCA" : "S", "UCG" : "S", "UAU" : "Y", "UAC" : "Y", "UAA" : "X", "UAG" : "X", "UGU" : "C", "UGC" : "C", "UGA" : "X", "UGG" : "W", "CUU" : "L", "CUC" : "L", "CUA" : "L", "CUG" : "L", "CCU" : "P", "CCC" : "P", "CCA" : "P", "CCG" : "P", "CAU" : "H", "CAC" : "H", "CAA" : "Q", "CAG" : "Q", "CGU" : "R", "CGC" : "R", "CGA" : "R", "CGG" : "R", "AUU" : "I", "AUC" : "I", "AUA" : "I", "AUG" : "M", "ACU" : "T", "ACC" : "T", "ACA" : "T", "ACG" : "T", "AAU" : "N", "AAC" : "N", "AAA" : "K", "AAG" : "K", "AGU" : "S", "AGC" : "S", "AGA" : "R", "AGG" : "R", "GUU" : "V", "GUC" : "V", "GUA" : "V", "GUG" : "V", "GCU" : "A", "GCC" : "A", "GCA" : "A", "GCG" : "A", "GAU" : "D", "GAC" : "D", "GAA" : "E", "GAG" : "E", "GGU" : "G", "GGC" : "G", "GGA" : "G", "GGG" : "G"}
    
# Created a list from the string parsing at every nth place, n=3 and print
def _translation(rna):
    for strand in rna:
        codonList = [strand[i:i+3] for i in range(0, len(strand), 3)]

# loop through the list using the dictionary and appending the translation to a new string. If "X" is a translation the 
# loop will stop while not translating "X" 
protein = []
for codon in CodonList:
    aminoAcid = rnaToProteinDictionary[codon]
    if aminoAcid != "X":
        PROTEIN.append(aminoAcid)
        continue
    else:     
        return ''.join(protein)
#-MAINCODE-------------------------------------------------------------- 
rna = sys.stdin.read().splitlines()    # read in the input from STDIN
#print ('\n'.join(map(str, (transcription(dna)))))
print (reverseComplement(dna))
#-----------------------------------------------------------------------