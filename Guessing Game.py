#!/usr/bin/env python
# coding: utf-8

# In[ ]:


guess=0
secret_number=5
guess = int(input("guess the number :  "))
last_guess=guess
count=1
while(guess !=secret_number):
    if secret_number>guess:
        if guess==secret_number-1:
            print("You are too close.")
        else:
            print("Guessed no. is to small ")  
    else:   
            if guess==secret_number+1:
                print("You are too close.")
            else:
                print("Guessed no. is to big ") 
    guess = int(input("You can try again :"))
    if guess == last_guess:
        count=count
    else:
        count=count+1   
print("you are right!!!") 
print(f"you tried total {count} numbers.")


# In[ ]:




