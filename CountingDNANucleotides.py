
# coding: utf-8

# In[1]:

DNA = raw_input ("Enter DNA Sequence:") 
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


# In[ ]:



