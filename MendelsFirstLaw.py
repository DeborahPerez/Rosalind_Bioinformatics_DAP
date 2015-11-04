
# coding: utf-8

# In[21]:

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

def find_dominant_phenotype(offspring):
    dominant_allele = 0
    for allele in offspring:
        if 'A' in allele:
            dominant_allele += 1  

    dominant_fraction = dominant_allele / 4.00
    return dominant_fraction

#probability values of each branch will be stored in a list to execute the final sum
dominant_amount = []  

#Using find_dominant_phenotype function to count offspring with dominant phenotypes in k&k.
#Find probability of kk branch with dominant offspring
dominant_amount.append(find_dominant_phenotype(kk_off) * prob2k)

#Using find_dominant_phenotype function to count offspring with dominant phenotypes in m&m
#Find probability of mm branch with dominant offspring
dominant_amount.append(find_dominant_phenotype(mm_off) * prob2m)

#Using find_dominant_phenotype function to count offspring with dominant phenotypes in n&n
#Find probability of nn branch with dominant offspring
dominant_amount.append(find_dominant_phenotype(nn_off) * prob2n)

#Using find_dominant_phenotype function to count offspring with dominant phenotypes in k&m
#Find probability of km branch with dominant offspring
dominant_amount.append(find_dominant_phenotype(km_off) *probkm)

#Using find_dominant_phenotype function to count offspring with dominant phenotypes in k&n
#Find probability of kn branch with dominant offspring
dominant_amount.append(find_dominant_phenotype(kn_off) * probkn)

#Using find_dominant_phenotype function to count offspring with dominant phenotypes in m&n
#Find probability of mn branch with dominant offspring
dominant_amount.append(find_dominant_phenotype(mn_off) *probmn)
    
print sum(dominant_amount)           


# In[ ]:



