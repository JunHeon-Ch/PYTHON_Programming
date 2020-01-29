#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
2016년 1월 1일이 금요일일 때 2016년 a월 b일은 무슨 요일인지 구하라.
'''

def findDay(a, b):
    from datetime import date
    
    d1 = date(2016, 1, 1)
    d2 = date(2016, a, b)
    day = (d2 - d1).days % 7
    
    return day

days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'TUR']
a, b = map(int, input().split())

day = findDay(a, b)
print(days[day])


# In[ ]:




