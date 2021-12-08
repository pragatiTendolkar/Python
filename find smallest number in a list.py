#!/usr/bin/env python
# coding: utf-8

# In[5]:


prize = [11,44,66,33,45]

smallest_number = prize[0]

for i in prize:
    if i < smallest_number:
        smallest_number = i
        
print(f"smallest number in list : { smallest_number }")


# In[ ]:




