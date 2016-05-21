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
#   VERSION:    20160521
########################################################################
import sys
#---rabbit_recurrence_relations-----------------------------------------
# Recurrence relation (Fn=Fn−1+Fn−2) (with F1=F2=1 to initiate the
# sequence) is used to determine how many pairs of rabbits are present
# after n months starting with k pairs of rabbits.
# @param text with two integers n and k separated by a space
# @return an integer representing total rabbit pairs after n months
def rabbit_recurrence_relations(n, k):
# Initializes maturing, breeding, and matured rabbits to 0 before
# procreation. Initializes offspring to 1.
    maturing = 0
    breeding = 0
    matured = 0
    offspring = 1
# Initializes the maturing set to be the same amount as offspring and
# breeding set to be the same amount of matured rabbits.
    maturing = offspring
    breeding = matured
# Pattern of procreation per month with k rabbits. n = months
    for i in range(1,n):
        matured = maturing + breeding
        offspring = breeding*k
        maturing = offspring
        breeding = matured
        total = matured + offspring
# Returns output
    return total
#-----------------------------------------------------------------------
#-MAINCODE--------------------------------------------------------------
nAndKValues = sys.stdin.read().splitlines()
n, k = map(int, nAndKValues[0].split(" "))
print (rabbit_recurrence_relations(n, k))
#-----------------------------------------------------------------------
