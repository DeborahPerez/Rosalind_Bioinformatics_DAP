
# coding: utf-8

# In[10]:

#!/usr/bin/env python2

#	USAGE: python2 FindingAMotifInDNA.py
#   DESCRIPTION: Given Two DNA strings s and t (each of length at most 1 kbp) and return all locations of t as a substring of s.
#   Created by Deborah Perez

#DNA string
DNA = "GATATATGCATATACTT"

# print occurences of 'n'+1 to show 1-based numbering as opposed to the python's 0-based numbering. Given the length of the 
# string if the function finds an occurence it will print and continue from the occurence which was saved as 'n'
print [n+1 for n in xrange(len(DNA)) if DNA.find('ATAT', n) == n]


# In[ ]:



