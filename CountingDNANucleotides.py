########################################################################
#    USAGE:
#       python3 count_nucleotides.py
#   DESCRIPTION:
#       Summarize counts of all four DNA bases for a string
#       entered through standard input
#   ROSALIND PROBLEM:
#       http://rosalind.info/problems/dna/
#-----------------------------------------------------------------------
#   CREATED BY: Deborah Perez
#   VERSION:    20160422
########################################################################

#-FUNCTIONS-------------------------------------------------------------
# Counts all four types of nucleotides (A, C, G, T) in DNA.
def count_nucleotides(dna):    # Set dna as variable for function.
    nucleotideCount = {}    # Create array for nucleotide counts.
    for base in 'ACGT':    # Set up keys in array to be nucleotides.
        nucleotideCount[base] = 0    # Initialize values in array to 0.

    for line in dna:    #Iterate through each line in list dna
        nucleotideCount['A'] += line.count('A')     #count all 'A's
        nucleotideCount['C'] += line.count('C')     #count all 'C's
        nucleotideCount['G'] += line.count('G')     #count all 'G's
        nucleotideCount['T'] += line.count('T')     #count all 'T's

# return count of 'A' 'C' 'G' 'T' in that order
    listOfCounts = []    # Create an empty list 'listOfCounts
    
# 1. Iterate through a sorted nucleotideCount by key name
# 2. Append values of sorted keys to listOfCounts
    for count in sorted(nucleotideCount.keys()): # 1
        listOfCounts.append(nucleotideCount[count]) # 2
    return listOfCounts
#-----------------------------------------------------------------------

#-MAINCODE--------------------------------------------------------------
import sys    # import "sys" to read from STDIN
dna = sys.stdin.read().splitlines()    # read STDIN and create list

# Converts list to a string and joins values with a space (' ')
print (' '.join(map(str,(count_nucleotides(dna)))))    # output
#-----------------------------------------------------------------------