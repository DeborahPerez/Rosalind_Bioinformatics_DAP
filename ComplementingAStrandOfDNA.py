########################################################################
#    USAGE:
#       python3 ComplementingAStrandOfDNA.py
#   DESCRIPTION:
#       Convert a dna strand to its complement
#   ROSALIND PROBLEM:
#       http://rosalind.info/problems/revc/
#-----------------------------------------------------------------------
#   CREATED BY: Deborah Perez
#   VERSION:    20160521
########################################################################
import sys 
# ---reverse_complement-------------------------------------------------
# Converts a strand of dna to its reverse complement
# @param dna one or more lines of dna text
# @return string of nucleotides as reverse complement
# ----------------------------------------------------------------------
def reverse_complement(dna):
# Initializes string to be returned for reverse complement
    dnaComplement = ''
# Reverses the order of the input string
    for line in dna:
        reverseDna = _reverse(line) 
# Applies complements of reversed input to dnaComplement
        for nucleotide in reverseDna:
            dnaComplement += _complement(nucleotide)
# Returns output           
    return dnaComplement
# ----------------------------------------------------------------------
# ---_reverse-----------------------------------------------------------
# Reverses text
# @param string of text
# @return string text in reverse order
# ----------------------------------------------------------------------
def _reverse(text):
# Initializes string to be returned for reverse order
    reversedText = ''
# Appends the index of text correlated to the value of count
    count = len(text) - 1
    for character in text:
        reversedText += text[count]
        count -=1
# Returns output      
    return reversedText
# ----------------------------------------------------------------------
# ---_complement--------------------------------------------------------
# Translates complement of nucleotides: A=T, T=A, C=G, and G=C
# @param string of text
# @return string text with complement translation
# ----------------------------------------------------------------------
def _complement(nucleotide):
# Initializes string to be returned for translated complements
    complement = '' 
# Translates a dna nucleotide to its dna complement nucleotide
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
#del dna[0]
print (reverse_complement(dna))  
#-----------------------------------------------------------------------