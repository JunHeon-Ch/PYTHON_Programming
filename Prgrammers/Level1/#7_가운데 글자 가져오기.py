#!/usr/bin/env python
# coding: utf-8

# In[7]:


def midLetter(letter):
    if len(letter) % 2:
        return letter[len(letter)//2]
    else:
        return letter[len(letter)//2-1:len(letter)//2+1]

letter = input()
print(midLetter(letter))


# In[ ]:




