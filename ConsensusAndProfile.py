
# coding: utf-8

# In[22]:

COLLECTION = ">Rosalind_1ATCCAGCT>Rosalind_2GGGCAACT>Rosalind_3ATGGATCT>Rosalind_4AAGCAACC>Rosalind_5TTGGAACT>Rosalind_6ATGCCATT>Rosalind_7ATGGCACT"

#separate each strand into a list using the delimeter separating each element by '>'
delimiter = '>'
COLLECTION_LIST = COLLECTION.split(delimiter)

#Create a list of all individual strands as well as define a function to delete the first 10 characters
def delete_head(COLLECTION_LIST):
    del COLLECTION_LIST[0]
    
delete_head(COLLECTION_LIST)

#loop to iterate through each element in the list, replace each element with a version that is without the first 10 characters
NEW_COLLECTION = []
for strand in COLLECTION_LIST:
    newstrand = strand[10:]
    NEW_COLLECTION.append(newstrand)
print NEW_COLLECTION

#


# In[ ]:



