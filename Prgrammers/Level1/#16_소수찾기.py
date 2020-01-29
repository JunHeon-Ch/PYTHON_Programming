#!/usr/bin/env python
# coding: utf-8

# In[11]:


'''
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수
'''

def primeNumber(n):
    numbers = set([i for i in range(3, n+1, 2)])
    
    for i in range(3, n+1, 2):
        numbers -= set([i for i in range(i*2, n+1, i)])
    
    return len(numbers)+1

n = int(input())
result = primeNumber(n)

print(result)


# In[ ]:




