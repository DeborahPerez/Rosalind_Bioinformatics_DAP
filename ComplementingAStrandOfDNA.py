########################################################################
#    USAGE:
#       python3 ComplementingAStrandOfDNA.py
#   DESCRIPTION:
#       Convert a dna strand to its complement
#   ROSALIND PROBLEM:
#       http://rosalind.info/problems/revc/
#-----------------------------------------------------------------------
#   CREATED BY: Deborah Perez
#   VERSION:    20160422
########################################################################

#-FUNCTIONS-------------------------------------------------------------
def reverseComplement(dna):
    dnaComplement = '' 

    for line in dna:    # Iterate through each line in list dna
        reverseDna = reverse(line)
        for nucleotide in reverseDna:
            dnaComplement += complement(nucleotide)
    return dnaComplement
#-----------------------------------------------------------------------
def reverse(text):
    result = ''
    count = len(text) -1
    for x in text:
        result += text[count]
        count -=1
    return result
#-----------------------------------------------------------------------
def complement(nucleotide):
    comp = '' 
#    for base in Nucleotide:
    if nucleotide is 'A':
        comp += 'T'
    elif nucleotide is 'T':
        comp += 'A'
    elif nucleotide is 'C':
        comp += 'G'
    elif nucleotide is 'G':
        comp += 'C'
    else:
        stop
    return comp

#-MAINCODE--------------------------------------------------------------
import sys    # import "sys" to read from STDIN
dna = sys.stdin.read().splitlines()    # read in the input from STDIN
#print ('\n'.join(map(str, (transcription(dna)))))
print (reverseComplement(dna))
#-----------------------------------------------------------------------