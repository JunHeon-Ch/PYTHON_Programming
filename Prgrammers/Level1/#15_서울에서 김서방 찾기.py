#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수
'''

seoul = list(input().split())
index = seoul.index('Kim')

print('김서방은 {}에 있다.'.format(index))


# In[ ]:




