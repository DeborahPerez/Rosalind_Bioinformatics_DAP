
# coding: utf-8

# In[6]:

DataSet = ">Rosalind_6404CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG>Rosalind_5959CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC>Rosalind_0808CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"
   
def FASTAsection(DataSet):
    positions = []
    startposition = 0

    while True:
        i = DataSet.find(">", startposition)
        if i == -1: break
        positions.append(i)
        startposition = i + 1

    return positions

FASTAsection(DataSet)

x = FASTAsection(DataSet)

for i in x
    sequences = []
    seq = DataSet[x[i]+14:x[i+1]]
    sequences.append(seq)
    return sequences





# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



