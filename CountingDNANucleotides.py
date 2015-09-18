
# coding: utf-8

# In[1]:
#DNA = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
DNA = raw_input ("Enter DNA Sequence:") # Python2 version of read from standard in (STDIN)
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

print A, C, G, T
#print(A, C, G, T) # Python3 version of print as a function

# In[ ]:



