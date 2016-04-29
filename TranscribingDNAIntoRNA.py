########################################################################
#    USAGE:
#       python3 TranscribingDnaIntoRna.py
#   DESCRIPTION:
#       Convert 'T' in dna to 'U' in order to trascribe dna to rna
#   ROSALIND PROBLEM:
#       http://rosalind.info/problems/rna/
#-----------------------------------------------------------------------
#   CREATED BY: Deborah Perez
#   VERSION:    20160428
########################################################################

import sys   

# ---_transcription-----------------------------------------------------
# Transcribes dna into rna by replacing all 'T's with 'U's
# @param dna one or more lines of dna text
# @return a string as the rna transcript
# ----------------------------------------------------------------------
def _transcription(dna):    
# Initialize rna output string
    transcript = ''   
# Transcribe all 'T's found to be 'U's
    for line in dna: 
        for nucleotide in line: 
            if nucleotide != 'T':   
                transcript += nucleotide   
            else:    
                transcript += 'U'
# Return string output
    return transcript
# ----------------------------------------------------------------------

# ---MAINCODE-----------------------------------------------------------
dna = sys.stdin.read().splitlines()    
# If genome/text file is in FASTA format, delete first line of dna
#del dna[0]
print (''.join(map(str, (_transcription(dna)))))
#-----------------------------------------------------------------------