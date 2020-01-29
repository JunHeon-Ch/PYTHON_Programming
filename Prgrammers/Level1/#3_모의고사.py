#!/usr/bin/env python
# coding: utf-8

# In[7]:


'''
#1: 1, 2, 3, 4, 5, ...
#2: 2, 1, 2, 3, 2, 4, 2, 5, ...
#3: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
정답이 주어졌을 때 가장 많이 맞춘 사람을 골라라
'''

#학생별 찍는 방법 초기화
def initList(length):
    student1 = []
    student2 = []
    student3 = []
    
    cnt1 = 1
    cnt2 = 1

    for i in range(length):
        #student1
        student1.append(int(i) % 5 + 1)
            
        #student2
        if int(i) % 2:
            if cnt1 == 6:
                cnt1 = 1
            if cnt1 == 2:
                cnt1 = 3
            student2.append(cnt1)
            cnt1 += 1
        else:
            student2.append(2)
            
        #student3
        n = int(i) % 10
        if n < 2:
            student3.append(3)
        else:
            if cnt2 == 3:
                cnt2 = 4
            student3.append(cnt2)
            if n % 2:
                cnt2 += 1

    return student1, student2, student3

# 찍은 정답 맞은지 확인 후 제일 많이 맞춘 학생 리턴
def abacadaba(answer):
    student1, student2, student3 = initList(len(answer))
    correct = [0, 0, 0]
    
    i = 0
    for n in answer:
        if int(n) == student1[i]:
            correct[0] += 1
        if int(n) == student2[i]:
            correct[1] += 1
        if int(n) == student3[i]:
            correct[2] += 1
        i += 1
    
    m = max(correct)
    result = [i + 1 for i,  j in enumerate(correct) if j == m]
    
    return result

answer = input()
print(abacadaba(answer))


# In[ ]:





# In[ ]:





# In[ ]:




