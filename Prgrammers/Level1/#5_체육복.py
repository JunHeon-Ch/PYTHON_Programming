#!/usr/bin/env python
# coding: utf-8

# In[21]:


'''
여벌의 체육복을 가지고 있는 학생은 앞뒤 번호의 학생에게만 체육복을 빌려줄 수 있다.
전체 학생 n명 중 최대 몇명이 체육 수업을 들을 수 있는지 구하라. 
'''

def physicalClass(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
            
    return n-len(set_lost)

n = int(input())
lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))

print(physicalClass(n, lost, reserve))


# #

# In[ ]:




