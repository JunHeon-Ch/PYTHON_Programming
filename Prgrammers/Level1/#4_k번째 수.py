#!/usr/bin/env python
# coding: utf-8

# In[8]:


def solution(array, command):
    result = []
    
    for n in command:
        i, j, k = n
        arr = array[i-1:j]
        arr.sort()
        result.append(arr[k-1])
    
    return result

array = [1, 5, 2, 6, 3, 7, 4]
command = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, command))


# In[ ]:




