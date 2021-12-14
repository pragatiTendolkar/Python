#!/usr/bin/env python
# coding: utf-8

# In[ ]:


number = 4
i=0
while number % 4 == 0:
    number = int(input(" Enter year "))
    for i in range(20): 
        if number % 4 == 0:
            print(number)
            number=number+4
        else:
            number=number+1
        


# In[ ]:




