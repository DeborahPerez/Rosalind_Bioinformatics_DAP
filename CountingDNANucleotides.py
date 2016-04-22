########################################################################
#    USAGE:
#       python3 counting_nucleotides.py
#   DESCRIPTION:
#       Summarize counts of all four DNA bases for a string
#       entered through standard input
#   ROSALIND PROBLEM:
#       http://rosalind.info/problems/dna/
#-----------------------------------------------------------------------
#   CREATED BY: Deborah Perez
#   VERSION:    20160418
########################################################################

#-STDIN-----------------------------------------------------------------
import sys    # import "sys" to read from STDIN
dna = sys.stdin.read().splitlines()    # read in the input from STDIN
#-----------------------------------------------------------------------

#-MAINCODE--------------------------------------------------------------
def counting_nucleotides(dna):
    nucleotideCount = {}
    for base in "ACGT":
        nucleotideCount[base] = 0

    for line in dna:
        nucleotideCount["A"] += line.count("A")
        nucleotideCount["C"] += line.count("C")
        nucleotideCount["G"] += line.count("G")
        nucleotideCount["T"] += line.count("T")

    return nucleotideCount
#-----------------------------------------------------------------------

#-STDOUT----------------------------------------------------------------
print (counting_nucleotides(dna))
#-----------------------------------------------------------------------
