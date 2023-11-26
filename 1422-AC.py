import sys
from math import *
input = sys.stdin.readline

#입력
lst = []
num = []
maxSizeNum = 0
n, m = map(int, input().split())
for i in range(n):
    lst.append(int(input()))

for i in range(len(lst)):
    num.append([0, lst[i]])
    if lst[i] > maxSizeNum:
        maxSizeNum = lst[i]
    nl = list(map(int, str(lst[i])))
    length = len(nl)
    for j in range(10 - length):
        lst[i] = lst[i] * 10 + nl[j%length]
    num[i][0] = lst[i]

num.sort(key=lambda x: (x[0]*(-1), x[1]*(-1)))
answer = []
for i in range(len(num)):
    answer.append(num[i][1])

NumIndex = answer.index(maxSizeNum)
a = ''
for i in range(m-n+1):
    a += str(maxSizeNum)
answer[NumIndex] = int(a)
    

# print(num)
print(*answer, sep='')
# print(maxSizeNum)