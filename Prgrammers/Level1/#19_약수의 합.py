#!/usr/bin/env python
# coding: utf-8

# In[6]:


'''
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수
'''

def sumOfaliquot(n):
    sum = 0
    
    for i in range(n, 0, -1):
        if n % i == 0:
            sum += i
    
    return sum

n = int(input())
result = sumOfaliquot(n)

print(result)
            


# In[ ]:




