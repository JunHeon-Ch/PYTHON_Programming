#!/usr/bin/env python
# coding: utf-8

# In[9]:


'''
두 정수 a, b 사이에 속한 모든 정수의 합을 구하라
'''

def sumOfWhole(a, b):
    if a < b:
        return sum(range(a, b+1))
    else:
        return sum(range(b, a+1))
    
a, b = map(int, input().split())
result = sumOfWhole(a, b)

print(result)


# In[ ]:




