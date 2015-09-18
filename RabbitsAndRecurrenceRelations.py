
# coding: utf-8

# In[ ]:

months = raw_input("Enter Months:")
n = int(months)
pairs = raw_input("Enter Offspring Pairs Per Litter:")
k = int(pairs)
try:
    n = int(months)
    k = int(pairs)
except:
    print "Please Enter a Number"
    
maturing = 0
breeding = 0
RArabbits = 0
offspring = 1
maturing = offspring
breeding = RArabbits

for i in xrange(1,n):
    RArabbits = maturing + breeding
    offspring = breeding*k
    maturing = offspring
    breeding = RArabbits 
    total = RArabbits + offspring 
    
print total



# In[ ]:



