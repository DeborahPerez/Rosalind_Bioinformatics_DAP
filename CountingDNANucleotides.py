#######################################################################
#    USAGE:
#       python3 count_nucleotides.py
#   DESCRIPTION:
#       Summarize counts of all four DNA bases for a string
#       entered through standard input
#   ROSALIND PROBLEM:
#       http://rosalind.info/problems/dna/
#-----------------------------------------------------------------------
#   CREATED BY: Deborah Perez
#   VERSION:    20160424
########################################################################

import sys

# count_nucleotides ----------------------------------------------------
# Counts all four types of nucleotides (A, C, G, T) in DNA
# @param dna one or more lines of dna text
# @return an array of nucleotide counts, in the order of A, C, G, T
# ----------------------------------------------------------------------
def count_nucleotides(dna):
# Initialize dictionary associating nucleotides with count values
    nucleotideCount = {}
# Fill dictionary
    for base in 'ACGT':
        nucleotideCount[base] = 0
# Shift counts into array
    for base in 'ACGT':
        for line in dna:
            nucleotideCount[base] += line.count(base)
# Return in the order of A, C, G, T
    listOfCounts = []
    for base in sorted(nucleotideCount.keys()):
        listOfCounts.append(nucleotideCount[base])
    return listOfCounts
# ----------------------------------------------------------------------

# MAINCODE -------------------------------------------------------------
dna = sys.stdin.readline().splitlines()
# Convert count array into a space-seperated list of counts
print (' '.join(map(str,(count_nucleotides(dna)))))
# ----------------------------------------------------------------------
