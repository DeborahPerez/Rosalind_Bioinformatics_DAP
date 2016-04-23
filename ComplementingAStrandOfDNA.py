########################################################################
#    USAGE:
#       python3 ComplementingAStrandOfDNA.py
#   DESCRIPTION:
#       Convert a dna strand to its complement
#   ROSALIND PROBLEM:
#       http://rosalind.info/problems/revc/
#-----------------------------------------------------------------------
#   CREATED BY: Deborah Perez
#   VERSION:    20160423
########################################################################

#-FUNCTIONS-------------------------------------------------------------
# Converts a strand of dna to its complement
def reverseComplement(dna):    # Set dna as variable for function
    dnaComplement = ''    # Create empty string as output

# 1. Use reverse function to reverse the line text
# 2. Iterate through each nucleotide in the line
# 3. Append the output from application of the complement function
    for line in dna:    # Iterate through each line in list dna
        reverseDna = _reverse(line)    # 1
        for nucleotide in reverseDna:    # 2
            dnaComplement += _complement(nucleotide)    # 3
    return dnaComplement    # return output
#-----------------------------------------------------------------------
# Reverses text
# 4. Iterate through each character in the text
# 5. Append the index correlated to the value of count
def _reverse(text):    # Set text as variable for function
    reversedText = ''    # Create empty string as output
    count = len(text) - 1    # Begin countdown from length of text - 1
    for character in text:    # 4
        reversedText += text[count]    # 5
        count -=1    # Reduce count by 1
    return reversedText    # return output
#-----------------------------------------------------------------------
# Translates a dna nucleotide to its dna complement nucleotide
# 6. Set nucleotide as variable for function
def _complement(nucleotide):    # 6
    complement = ''   # Create empty string as output
    if nucleotide is 'A':    # if nucleotide is Adenine('A')
        complement += 'T'    # Append its complement Thymine('T')
    elif nucleotide is 'T':    # if nucleotide is Thymine('T')
        complement += 'A'    # Append its complement Adenine('A')
    elif nucleotide is 'C':    # if nucleotide is Cytosine('C')
        complement += 'G'    # Append its complement Guanine('G')
    elif nucleotide is 'G':    # if nucleotide is Guanine('G')
        complement += 'C'    # Append its complement Cytosine('C')
    else:    # For all other cases
        stop    # Stop
    return complement    # Return output
#-----------------------------------------------------------------------

#-MAINCODE--------------------------------------------------------------
import sys    # Import "sys" to read from STDIN
dna = sys.stdin.read().splitlines()    # Read in the input from STDIN
print (reverseComplement(dna))    # Print results as STDOUT
#-----------------------------------------------------------------------