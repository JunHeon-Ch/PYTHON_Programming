#!/usr/bin/env python
# coding: utf-8

# In[4]:


'''
길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수
'''

def n_watermelon(n):
    sentence = '수박'
    if n % 2:
        return sentence*(n//2) + '수'
    else:
        return sentence*(n//2)

n = int(input())
result = n_watermelon(n)
print(result)


# In[ ]:




