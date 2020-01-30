#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수
'''

def strange_sentence(sentence):
    words = list(sentence.split())
    result = []
    
    for word in words:
        tmp = ''
        for i in range(len(word)):
            if i%2:
                tmp += word[i].lower()
            else:
                tmp += word[i].upper()
                
        result.append(tmp)
    
    return ' '.join(result)

sentence = input()
result = strange_sentence(sentence)

print(result)


# In[ ]:




