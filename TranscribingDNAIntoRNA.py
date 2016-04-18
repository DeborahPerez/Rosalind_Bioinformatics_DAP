########################################################################
#    USAGE:
#       python3 counting_dna_nucleotides.py
#   DESCRIPTION:
#       Convert 'T' in dna to 'U' in order to trascribe dna to rna
#   ROSALIND PROBLEM:
#       http://rosalind.info/problems/rna/
#-----------------------------------------------------------------------
#   CREATED BY: Deborah Perez
#   VERSION:    20160418
########################################################################

#-STDIN-----------------------------------------------------------------
import sys    # import "sys" to read from STDIN
dna = sys.stdin.read().splitlines()    # read in the input from STDIN
#-----------------------------------------------------------------------

#-MAINCODE--------------------------------------------------------------
def transcription(dna):
    transcript = []
    for line in dna:
        rna = line.replace("T", "U")
        transcript.append(rna)
    return transcript
#-----------------------------------------------------------------------

#-STDOUT----------------------------------------------------------------
print ('\n'.join(map(str, (transcription(dna)))))
#-----------------------------------------------------------------------
