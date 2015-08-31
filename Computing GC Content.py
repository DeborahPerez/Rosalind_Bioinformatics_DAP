
# coding: utf-8

# In[11]:

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

x = FASTAsection(DataSet)

seq1 = DataSet[x[0]+14:x[1]]
print seq1

for i in x



# In[ ]:



