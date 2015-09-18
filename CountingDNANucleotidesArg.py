#!/usr/bin/env python
##########################################################################
#	USAGE: python CountingDNANucleotides.py DNA_STRING
#   DESCRIPTION: Summarize counts of all four DNA bases for a string entered
#   as the first argument from the commandline.
#   Created by Deborah Perez
##########################################################################
# coding: utf-8
import sys # import this to be able to grab the first, second, etc argument
# passed to the script with sys.argv[x]

# In[1]:
DNA = sys.argv[1] # this assigns the first argument to the name "DNA"
#DNA = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
#DNA = raw_input ("Enter DNA Sequence:") # Python2 version of read from standard in (STDIN)
#DNA = input("Enter DNA Sequence:") # Python3 version of read from standard in (STDIN)
# count uppercase
A = DNA.count("A")
C = DNA.count("C")
G = DNA.count("G")
T = DNA.count("T")
# count lowercase:
A = A + DNA.count("a")
C = C + DNA.count("c")
G = G + DNA.count("g")
T = T + DNA.count("t")

#print A, C, G, T
print(A, C, G, T) # Python3 version of print as a function

# In[ ]:



