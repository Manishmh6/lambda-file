#!/usr/bin/env python
# coding: utf-8

# In[9]:


from functools import reduce
val = [1,2,3,4,5,6]
max = reduce(lambda a,b:a if a>b else b,val)
min = reduce(lambda a,b:b if a>b else a,val)
print(max)
print(min)


# In[10]:


from functools import reduce

val = [1,2,3,4,5]
add = reduce(lambda a,b:a+b,val)
print(add)


# In[11]:


# filter with  lambda with map 
a = [1,2,3,4,5,6,7,8,9,10]
l = filter(lambda a:a<8,a)
s = list(map(lambda a:a*a,l))
print("Square ",s)


# In[12]:


a = [1,2,3,4,5,6,7,8,9,10]

evan = list(filter(lambda a:a%2==0,a))

for i in evan:
   print("Evan No =",i)


# In[13]:


# lambda with filter

ages  = [5, 12, 15, 18, 24, 32]

age = filter(lambda a:a>18,ages)
for i in age:
    print(i)


# In[ ]:




