#!/usr/bin/env python
# coding: utf-8

# In[8]:


'''
array에 중복된 수 제거
'''

def deduplication(array):
    result = []
    result.append(array[0])
    
    for i in range(1, len(array)):
        if array[i] != array[i-1]:
            result.append(array[i])
    
    return result

array = list(map(int, input().split()))
result = deduplication(array)
print(result)


# In[ ]:




