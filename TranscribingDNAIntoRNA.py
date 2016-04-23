########################################################################
#    USAGE:
#       python3 TranscribingDnaIntoRna.py
#   DESCRIPTION:
#       Convert 'T' in dna to 'U' in order to trascribe dna to rna
#   ROSALIND PROBLEM:
#       http://rosalind.info/problems/rna/
#-----------------------------------------------------------------------
#   CREATED BY: Deborah Perez
#   VERSION:    20160422
########################################################################

#-FUNCTIONS-------------------------------------------------------------
# Transcribes dna into rna by replacing all 'T's with 'U's
def transcription(dna):    # Set dna as variable for function.
    transcript = ''    # Create empty string for transcription
    
# 1. Iterate through each nucleotide of each line in dna
    for line in dna:    # Iterate through each line in list dna
        for nucleotide in line:    # 1
            if nucleotide != 'T':    # If the nucleotide isn't 'T'
                transcript += nucleotide    # Append it to 'transcript'
            else:    #If the nucleotide is 'T'
                transcript += 'U'    # Append a 'U' to transcript
    return transcript    # Return output
#-----------------------------------------------------------------------

#-MAINCODE--------------------------------------------------------------
import sys    # Import "sys" to read from STDIN
dna = sys.stdin.read().splitlines()    # Read in the input from STDIN
print (transcription(dna))    # Print output as STDOUT
#-----------------------------------------------------------------------