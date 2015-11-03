
# coding: utf-8

# In[8]:

#Description: 
#Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: 
#k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

#Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele 
#and thus displaying the dominant phenotype. Assume that any two organisms can mate.

#Created By: Deborah Perez

#Leftoff: Actually calculate the probability and almost done!

k = 2
m = 2
n = 2
#population total
total = float(k + m + n)

#probability that both individuals are k
prob2k = k/total * (k-1)/(total-1)
#probability that both individuals are m
prob2m = m/total * (m-1)/(total-1)
#probability that both individuals are m
prob2n = n/total * (n-1)/(total-1)

#probability that individuals are k and m
probkm = k/total * m/(total-1)
#probability that individuals are k and n
probkn = k/total * n/(total-1)
#probability that individuals are m and n
probmn = m/total * n/(total-1)

#Alleles for individuals k, m, and n
k_allele = ['A','A']
m_allele = ['A','a']
n_allele = ['a','a']

#Probability that prob2k will produce offspring that inherit a dominant allele
import itertools
kk = k_allele, k_allele
kk_off = list(itertools.product(*kk))


#Probability that prob2m will produce offspring that inherit a dominant allele
mm = m_allele, m_allele
mm_off = list(itertools.product(*mm))


#Probability that prob2k will produce offspring that inherit a dominant allele
nn = n_allele, n_allele
nn_off = list(itertools.product(*nn))


#Probability that k and m produce offspring that inherit a dominant allele
km = k_allele, m_allele
km_off = list(itertools.product(*km))


#Probability that k and n produce offspring that inherit a dominant allele
kn = k_allele, n_allele
kn_off = list(itertools.product(*kn))


#Probability that m and n produce offspring that inherit a dominant allele
mn = m_allele, n_allele
mn_off = list(itertools.product(*mn))


#Defining a function to determine dominant phenotypes by checking for the presence of dominant characteristics 
def find_dominant_phenotype(x):
    dominantphenotype = 0
    for allele in x:
        if 'A' in allele:
            dominantphenotype += 1  
    
    ratio = dominantphenotype / 4.00
    return ratio

    
#Using find_dominant_phenotype function to count offspring with dominant phenotypes in k&k.
#Find probability of kk branch with dominant offspring
print find_dominant_phenotype(kk_off)

#Using find_dominant_phenotype function to count offspring with dominant phenotypes in m&m
print find_dominant_phenotype(mm_off) 

#Using find_dominant_phenotype function to count offspring with dominant phenotypes in n&n
print find_dominant_phenotype(nn_off) 

#Using find_dominant_phenotype function to count offspring with dominant phenotypes in k&m
print find_dominant_phenotype(km_off) 

#Using find_dominant_phenotype function to count offspring with dominant phenotypes in k&n
print find_dominant_phenotype(kn_off) 

#Using find_dominant_phenotype function to count offspring with dominant phenotypes in m&n
print find_dominant_phenotype(mn_off) 
    
            


# In[ ]:



