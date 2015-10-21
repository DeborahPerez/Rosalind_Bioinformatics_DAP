
# coding: utf-8

# In[7]:

#Description:
#Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
#Return: The protein string encoded by s.

#Created By: Deborah Perez

#Sample Dataset in a string
SampleDataset = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"

#Dictionary to translate RNA to protein
RNA_Trans = {"UUU" : "F", "UUC" : "F", "UUA" : "L", "UUG" : "L", "UCU" : "S", "UCC" : "S", "UCA" : "S", "UCG" : "S", "UAU" : "Y", "UAC" : "Y", "UAA" : "X", "UAG" : "X", "UGU" : "C", "UGC" : "C", "UGA" : "X", "UGG" : "W", "CUU" : "L", "CUC" : "L", "CUA" : "L", "CUG" : "L", "CCU" : "P", "CCC" : "P", "CCA" : "P", "CCG" : "P", "CAU" : "H", "CAC" : "H", "CAA" : "Q", "CAG" : "Q", "CGU" : "R", "CGC" : "R", "CGA" : "R", "CGG" : "R", "AUU" : "I", "AUC" : "I", "AUA" : "I", "AUG" : "M", "ACU" : "T", "ACC" : "T", "ACA" : "T", "ACG" : "T", "AAU" : "N", "AAC" : "N", "AAA" : "K", "AAG" : "K", "AGU" : "S", "AGC" : "S", "AGA" : "R", "AGG" : "R", "GUU" : "V", "GUC" : "V", "GUA" : "V", "GUG" : "V", "GCU" : "A", "GCC" : "A", "GCA" : "A", "GCG" : "A", "GAU" : "D", "GAC" : "D", "GAA" : "E", "GAG" : "E", "GGU" : "G", "GGC" : "G", "GGA" : "G", "GGG" : "G"}

#Created a list from the string parsing at every nth place, n=3 and print
SDList = [SampleDataset[i:i+3] for i in range(0, len(SampleDataset), 3)]
print SDList 

#loop through the list using the dictionary and appending the translation to a new string
PROTEIN = []
for codon in SDList:
    PRO = RNA_Trans[codon]
    PROTEIN.append[PRO]
    print codon, PRO, PROTEIN



# In[ ]:



