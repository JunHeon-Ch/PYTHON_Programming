#!/usr/bin/env python
# coding: utf-8

# In[12]:


'''
문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬
해당 인덱스의 문자가 같은 문자열이 여럿일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치
'''

def optionalSort(array, n):
    result = sorted(sorted(array), key = lambda arr : arr[n])
    
    return result

array = list(input().split())
n = int(input())

result = optionalSort(array, n)

print(result)


# In[ ]:





# In[ ]:




