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
    a = 0
    c = 0
    g = 0
    t = 0

    for line in dna:
        a += line.count("A")
        c += line.count("C")
        g += line.count("G")
        t += line.count("T")

    eachNucleotideCount = a, c, g , t
    return eachNucleotideCount
#-----------------------------------------------------------------------

#-STDOUT----------------------------------------------------------------
print (' '.join(map(str, (counting_nucleotides(dna)))))
#-----------------------------------------------------------------------
