#!/usr/bin/env python
# coding: utf-8

# In[21]:


#n개 단위로 문자열 압축

def n_zip(s):
    min = len(s)
    
    for n in range(1, len(s)+1):
        si = 0
        cnt = 0
        result = ''
        next = ''
        current = ''
        
        while si < len(s):
            current = next
            next = s[si:si+n]
            
            if current != next:
                if cnt == 1:
                    result += current
                elif cnt > 1:
                    result += str(cnt) + current
                cnt = 1
                
            else:
                cnt += 1  
            
            si += n
        
        if cnt == 1:
            result += next
        elif cnt > 1:
            result += str(cnt) + next
              
        print(result)
        
        if min > len(result):
            min = len(result)

    return min

s = input()
print(n_zip(s))


# In[ ]:





# In[ ]:




