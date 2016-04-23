########################################################################
#    USAGE:
#       python3 RabbitsAndRecurrenceRelations.py
#   DESCRIPTION:
#       Given integers n and k, return the total number of rabbit pairs 
#       that will be present after n months if we begin with 1 pair and 
#       in each generation, every pair of reproduction-age rabbits 
#       produces a litter of k rabbit pairs (instead of only 1 pair).
#   ROSALIND PROBLEM:
#       http://rosalind.info/problems/fib/
#-----------------------------------------------------------------------
#   CREATED BY: Deborah Perez
#   VERSION:    20160423
########################################################################

#-FUNCTIONS-------------------------------------------------------------
# Recurrence relation (Fn=Fn−1+Fn−2) (with F1=F2=1 to initiate the 
# sequence) is used to determine how many pairs of rabbits are present 
# after n months starting with k pairs of rabbits. 
def rabbit_recurrence_relations(n, k):
    maturing = 0
    breeding = 0
    matured = 0
    offspring = 1
    maturing = offspring
    breeding = matured

    for i in range(1,n):    # Iterate through range (1 to n)
        # Fibonacci sequence below
        matured = maturing + breeding
        offspring = breeding*k
        maturing = offspring
        breeding = matured
        total = matured + offspring 
    
    return total
#-----------------------------------------------------------------------

#-MAINCODE--------------------------------------------------------------
import sys    # Import "sys" to read from STDIN
nAndKValues = sys.stdin.read().splitlines()    # Read in the input from STDIN
n, k = map(int, nAndKValues.split(" "))
print (transcription(dna))    # Print output as STDOUT
#-----------------------------------------------------------------------