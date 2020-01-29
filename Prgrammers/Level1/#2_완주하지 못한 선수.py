#!/usr/bin/env python
# coding: utf-8

# In[4]:


def stringInString(part, comp):
    nc = []
    
    for p in part:
        if p not in comp:
            nc = p
    
    return nc

participant = []
completion = []

n = int(input())

for i in range(n):
    s = input()
    participant.append(s)

for i in range(n-1):
    s = input()
    completion.append(s)
    
notCompletion = stringInString(participant, completion)

for nc in notCompletion:
    print(nc)


# In[ ]:




