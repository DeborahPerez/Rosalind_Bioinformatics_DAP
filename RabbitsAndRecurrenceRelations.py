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


def rabbit_recurrence_relations(n, k):
    maturing = 0
    breeding = 0
    matured = 0
    offspring = 1
    maturing = offspring
    breeding = matured

    for i in range(1,n):
        matured = maturing + breeding
        offspring = breeding*k
        maturing = offspring
        breeding = matured
        total = matured + offspring

    return total

#-MAINCODE--------------------------------------------------------------
import sys    # Import "sys" to read from STDIN
nAndKValues = sys.stdin.read().splitlines()    # Read in the input from STDIN
n, k = map(int, nAndKValues[0].split(" "))
print (rabbit_recurrence_relations(n, k))    # Print output as STDOUT
#-----------------------------------------------------------------------
