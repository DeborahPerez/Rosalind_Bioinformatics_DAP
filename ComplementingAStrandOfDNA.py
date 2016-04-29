########################################################################
#    USAGE:
#       python3 ComplementingAStrandOfDNA.py
#   DESCRIPTION:
#       Convert a dna strand to its complement
#   ROSALIND PROBLEM:
#       http://rosalind.info/problems/revc/
#-----------------------------------------------------------------------
#   CREATED BY: Deborah Perez
#   VERSION:    20160429
########################################################################

import sys 

# ---reverse_complement-------------------------------------------------
# Converts a strand of dna to its reverse complement
def reverse_complement(dna):
    dnaComplement = ''    # Create empty string as output
# 
    for line in dna:
        reverseDna = _reverse(line) 
        for nucleotide in reverseDna:
            dnaComplement += _complement(nucleotide)
# Returns output           
    return dnaComplement    
# ---_reverse-----------------------------------------------------------
# Reverses text
# 4. Iterate through each character in the text
# 5. Append the index correlated to the value of count
def _reverse(text):    # Set text as variable for function
    reversedText = ''    # Create empty string as output
    count = len(text) - 1    # Begin countdown from length of text - 1
    for character in text:    # 4
        reversedText += text[count]    # 5
        count -=1    # Reduce count by 1
    return reversedText    # return output
# ----------------------------------------------------------------------
# Translates a dna nucleotide to its dna complement nucleotide
# 6. Set nucleotide as variable for function
def _complement(nucleotide):
    complement = '' 
    if nucleotide is 'A':    
        complement += 'T'  
    elif nucleotide is 'T':  
        complement += 'A'  
    elif nucleotide is 'C':  
        complement += 'G'  
    elif nucleotide is 'G':  
        complement += 'C'    
# Returns output       
    return complement
#-----------------------------------------------------------------------

# ---MAINCODE-----------------------------------------------------------
dna = sys.stdin.read().splitlines()
# If genome/text file is in FASTA format, delete first line of dna
del dna[0]
print (reverse_complement(dna))  
#-----------------------------------------------------------------------