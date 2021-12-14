#!/usr/bin/env python
# coding: utf-8

# In[7]:


num = [12,24,56,78,45,34,72,22]
Largest = num[0]
a= []

for i in num:
        if i > Largest:
            Largest = i
a = num                
a.remove(Largest)
second_largest = a[0]
for j in a:
    if j > second_largest:
        second_largest = j
    
print(f"second largest number in list : { second_largest }")


# In[ ]:




