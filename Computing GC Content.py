
# coding: utf-8

# In[16]:

DataSet = ">Rosalind_6404CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG>Rosalind_5959CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC>Rosalind_0808CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"
delimiter = '>'
RFLIST = DataSet.split(delimiter)

def delete_head(RFLIST):
    del RFLIST[0]
    
delete_head(RFLIST)
print RFLIST

#def FASTAsection(DataSet):
#   positions = []
#    startposition = 0

#    while True:
#       i = DataSet.find(">", startposition)
#        if i == -1: break
#        positions.append(i)
#        startposition = i + 1

#    return positions

#FASTAsection(DataSet)

#x = FASTAsection(DataSet)

#for i in x:
    #sequences = []
    #s = (i + 1)
    #print DataSet[i:s]
    #sequences.append(seq)






# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



