#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열 반환
'''

def divisible(array, divisor):
    result = []
    
    for i in range(len(array)):
        if array[i] % divisor == 0:
            result.append(array[i])
    
    if len(result) == 0:
        result.append(-1)

    return result

array = list(map(int, input().split()))
divisor = int(input())

result = divisible(array, divisor)

print(result)


# In[ ]:




