import sys
from math import *
input = sys.stdin.readline

#입력
lst = []
num = []
maxSize = 0
maxSizeNum = 0
n, m = map(int, input().split())
for i in range(n):
    lst.append(int(input()))

for i in range(len(lst)):
    num.append([0, lst[i], int(log10(lst[i]))+1])
    if int(log10(lst[i]))+1 > maxSize and lst[i] > maxSizeNum:
        maxSize = int(log10(lst[i]))+1
        maxSizeNum = lst[i]
    nl = list(map(int, str(lst[i])))
    length = len(nl)
    for j in range(10 - length):
        lst[i] = lst[i] * 10 + nl[j%length]
    num[i][0] = lst[i]

num.sort(key=lambda x: (x[0]*(-1), x[2]*(-1), x[1]*(-1)))
answer = []
for i in range(len(num)):
    answer.append(num[i][1])

print(num)
print(answer)
print(maxSize, maxSizeNum)