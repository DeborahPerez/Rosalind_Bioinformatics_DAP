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
#   VERSION:    20160423
########################################################################

#-FUNCTIONS-------------------------------------------------------------

def compute_gc_content(dnaFastAFormat):


def delete_head(RFLIST):
    del RFLIST[0]

delete_head(RFLIST)

#Calculated GC content of each strand and had Python remember the largest and the FASTA ID of that strand as it went through the list
# Computes percentage of 'G's and 'C's present in a text
def compute_gc_content(dnaFastAFormat):
    largest = None
    for STRAND in RFLIST:
        G = float(STRAND.count("G"))
        C = float(STRAND.count("C"))
        L = float(len(STRAND)-13)
        GC_COUNT = float(((G + C) / L) * 100)
        STRAND_ID = STRAND[0:14]
    if largest is None or GC_COUNT > largest:
        largest = GC_COUNT
    print STRAND_ID
    print round(largest, 6)

GC_CONTENT(RFLIST)

#-MAINCODE--------------------------------------------------------------
# 1. Joins list into one string
# 2. Creates a list of all individual dna strands
import sys    # Import "sys" to read from STDIN
dnaFastAFormat = sys.stdin.read().splitlines()    # Read in the input from STDIN
dnaFastAFormat = (''.join(map(str,(dnaFastAFormat))))    # 1
delimiter = '>'    # '>' character where splitting occurs
dnaStrands = dnaFastAFormat.split(delimiter)    # 2
print (compute_gc_content(dnaFastAFormat):)    # Print results as STDOUT
#-----------------------------------------------------------------------
