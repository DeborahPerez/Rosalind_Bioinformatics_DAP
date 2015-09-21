
# coding: utf-8

# In[17]:

#Need to create loop to count dominant offspring per combination and then calculate the probability.

k = 2
m = 2
n = 2
#population total
total = float(k + m + n)

#probability that both individuals are k
prob2k = k/total + k/total
#probability that both individuals are m
prob2m = m/total + m/total
#probability that both individuals are m
prob2n = n/total + n/total

#probability that individuals are k and m
probkm = k/total + m/total
#probability that individuals are k and n
probkn = k/total + n/total
#probability that individuals are m and n
probmn = m/total + n/total

#Alleles for individuals k, m, and n
k_allele = ['A','A']
m_allele = ['A','a']
n_allele = ['a','a']

#Probability that prob2k will produce offspring that inherit a dominant allele
import itertools
kk = k_allele, k_allele
kk_off = list(itertools.product(*kk))
print kk_off

#Probability that prob2m will produce offspring that inherit a dominant allele
import itertools
mm = m_allele, m_allele
mm_off = list(itertools.product(*mm))
print mm_off

#Probability that prob2k will produce offspring that inherit a dominant allele
import itertools
nn = n_allele, n_allele
nn_off = list(itertools.product(*nn))
print nn_off

#Probability that k and m produce offspring that inherit a dominant allele
import itertools
km = k_allele, m_allele
km_off = list(itertools.product(*km))
print km_off

#Probability that k and n produce offspring that inherit a dominant allele
import itertools
kn = k_allele, n_allele
kn_off = list(itertools.product(*kn))
print kn_off

#Probability that m and n produce offspring that inherit a dominant allele
import itertools
mn = m_allele, n_allele
mn_off = list(itertools.product(*mn))
print mn_off


# In[ ]:



