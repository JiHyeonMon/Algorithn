#2981
#검문

import math
num = []
answer = []
for i in range(int(input())):
     num.append(int(input()))

num = sorted(num)

for i in range(2, int(math.sqrt(num[0]))+1):
     for j in num:
          if j%i==0


     
'''
for i in range(2, int(math.sqrt(max(num)))+1):
     same = True

     for j in num:
          tmp = num[0]%i
          if tmp == j%i:
               continue
          else:
               same = False
               break
     if same:
          answer.append(i)

for i in answer:
     print(i, end=' ')
     
'''
