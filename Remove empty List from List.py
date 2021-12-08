#!/usr/bin/env python
# coding: utf-8

# In[1]:


lst = [1, 2, 3, 4, 5, [6, 7, 8, 9], [], [11, 22, 33, 44]]
for i in lst:
    if type(i) == list:
        if len(i) == 0:
            lst.remove(i)
print(lst)


# In[ ]:




