#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수
'''

def caeser(sentence, n):
    result = ''
    
    for letter in sentence:
        if letter.isupper():
            result += chr((ord(letter)-ord('A')+n)%26+ord('A'))
        elif letter.islower():
            result += chr((ord(letter)-ord('a')+n)%26+ord('a'))
        else:
            result += letter
    
    return result

sentence = input()
n = int(input())

result = caeser(sentence, n)
print(result)


# In[ ]:




