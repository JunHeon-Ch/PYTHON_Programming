#!/usr/bin/env python
# coding: utf-8

# In[5]:


#한개 단위로만 문자열 압축

def zip(sentence):
    cnt = 1
    next = ''
    bef = ''
    result = ''
    
    for i in sentence:
        if next != i:
            bef = next
            next = i
            
            if cnt == 1:
                result += bef
            elif cnt != 0:    
                result += str(cnt) + bef
            
            cnt = 1
        else:
            cnt += 1
    
    if cnt == 1:
        result += next
    elif cnt != 0:
        result += str(cnt) + next
    
    return result

sentence = input()
print(zip(sentence))


# In[ ]:




