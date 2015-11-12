
# coding: utf-8

# In[4]:

COLLECTION = ">Rosalind_1ATCCAGCT>Rosalind_2GGGCAACT>Rosalind_3ATGGATCT>Rosalind_4AAGCAACC>Rosalind_5TTGGAACT>Rosalind_6ATGCCATT>Rosalind_7ATGGCACT"
delimiter = '>'
COLLECTION_LIST = COLLECTION.split(delimiter)

#Created a list of all individual strands
def delete_head(COLLECTION_LIST):
    del COLLECTION_LIST[0]
    print COLLECTION_LIST
    
delete_head(COLLECTION_LIST)



# In[ ]:



