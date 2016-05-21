########################################################################
#    USAGE:
#       python3 computingGCContent.py
#   DESCRIPTION:
#       Comput the GC-content of a DNA string which is the percentage
#       of symbols in the string that are 'C' or 'G
#   ROSALIND PROBLEM:
#       http://rosalind.info/problems/gc/
#-----------------------------------------------------------------------
#   CREATED BY: Deborah Perez
#   VERSION:    20160521
########################################################################
import sys
#---compute_gc_content--------------------------------------------------
# Calculates GC content of input and returns largest and its FASTA ID
# @param dictionary of dna ID as keys and dna as values
# @return ID of highest GC content and its result
#-----------------------------------------------------------------------
def compute_gc_content(dnaWithIDs):
    highestGCContent = None
# Computes percentage of 'G's and 'C's present in a text
    for dnaID in dnaWithIDs:
        gCount = float(dnaWithIDs[dnaID].count("G"))
        cCount = float(dnaWithIDs[dnaID].count("C"))
        dnaLength = float(len(dnaWithIDs[dnaID]))
        countGC = float(((gCount + cCount) / dnaLength) * 100)
# Keeps track of highest score GC content
        if highestGCContent is None or countGC > highestGCContent:
            highestGCContent = countGC
            rosalindTag = dnaID
# Prints dnaID aka Rosalind Tag of dna with highest GC content
    print (rosalindTag)
# Returns value of highest GC content
    return round(highestGCContent, 6)
#-----------------------------------------------------------------------
#---MAINCODE------------------------------------------------------------
# Joins file data into one string
dnaFastaFormat = sys.stdin.read().splitlines()
dnaFastaFormat = (''.join(map(str,(dnaFastaFormat))))
# Creates a list of all dna strands
delimiter = '>'
dnaStrands = dnaFastaFormat.split(delimiter)
del dnaStrands[0]
# Creates a dictionary with Rosalind tags as keys and the dna as values
dnaWithIDs = {}
for strand in dnaStrands:
    rosalindTag = strand[:13]
    dna = strand[13:]
    dnaWithIDs[rosalindTag] = dna
#print (compute_gc_content(dnaWithID)
print (compute_gc_content(dnaWithIDs))
#-----------------------------------------------------------------------
