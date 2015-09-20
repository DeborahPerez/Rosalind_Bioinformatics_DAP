
# coding: utf-8

# In[ ]:

#Given: Three positive integers k, m, and n, representing a population containing  organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

#Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

#k = AA, m = Aa, n = aa, ie: K + m = AA * Aa = AA, AA, Aa, Aa ; K + n = AA * aa = Aa, Aa, Aa, Aa ; m + n = Aa * aa = Aa, Aa, aa, aa

#probability for k and m that offspring has dominant allele = 2 + 2 + 1 + 1 = 6/8
#probability for k and n that offspring has dominant allele = 1 + 1 + 1 + 1 = 4/8
#probability for n and m that offspring has dominant allele = 1 + 1 + 0 + 0 = 2/8
#probability for K and K that offspring has dominant allele = 1 = 8/8
#probability for m and m that offspring has dominant allele = 2 + 1 + 1 + 0 = 4/8
#probability for n and n that pffspring has dominant allele = 0 = 0/8

