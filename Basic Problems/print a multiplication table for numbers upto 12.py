#!/usr/bin/env python
# coding: utf-8

# In[4]:


# write a program that print a multiplication table for numbers upto 12

for number1 in range(1,13):
    for number2 in range(1,13):
        table=number1*number2
        print(f"{number1}*{number2}={table}")

