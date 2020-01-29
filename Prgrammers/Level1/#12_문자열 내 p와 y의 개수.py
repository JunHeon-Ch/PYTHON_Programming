#!/usr/bin/env python
# coding: utf-8

# In[6]:


'''
대소 구분없이 문자열 내의 p와 y의 개수 비교
개수가 같으면 True 다르면 False
p, y 둘 다 없으면 True
'''

def numberOfPY(sentence):
    sentence = sentence.lower()
    np = sentence.count('p')
    ny = sentence.count('y')
    
    if np == 0 and ny == 0:
        return True
    elif np == ny:
        return True
    else:
        return False
    
sentence = input()
result = numberOfPY(sentence)

print(result)


# In[ ]:




