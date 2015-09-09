
# coding: utf-8

# In[16]:

string1 = "GAGCCTACTAACGGGAT"
string2 = "CATCGTAATGACGGCCT"

#Turned strings into lists
ls1 = list(string1)
ls2 = list(string2)

#counted differences using built in zip function to mirror indices when comparing
count = 0
for base,pair in zip (ls1, ls2):
    if base != pair:
        count = count + 1
print count
            


# In[ ]:



