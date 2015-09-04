
# coding: utf-8

# In[33]:

DataSet = ">Rosalind_6404CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG>Rosalind_5959CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC>Rosalind_0808CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"
delimiter = '>'
RFLIST = DataSet.split(delimiter)
#Created a list of all individual FASTA strands
def delete_head(RFLIST):
    del RFLIST[0]
    
delete_head(RFLIST)

#Calculated GC content of each strand and had Python remember the largest and the FASTA ID of that strand as it went through the list
def GC_CONTENT(RFLIST):
    largest = None
    for STRAND in RFLIST:
        G = float(STRAND.count("G"))
        C = float(STRAND.count("C"))
        L = float(len(STRAND)-13)
        GC_COUNT = float(((G + C) / L) * 100)
        STRAND_ID = STRAND[0:14]
    if largest is None or GC_COUNT > largest:
        largest = GC_COUNT
    print STRAND_ID
    print round(largest, 6)

GC_CONTENT(RFLIST)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



