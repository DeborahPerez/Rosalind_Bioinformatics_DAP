
# coding: utf-8

# In[4]:

DNA = raw_input ("Insert DNA Sequence")
rDNA = DNA[::-1]
RNA = rDNA.replace("A", "t").replace("T", "A").replace("C", "g").replace("G", "C").replace("g", "G").replace("t", "T")
print RNA


# In[ ]:



