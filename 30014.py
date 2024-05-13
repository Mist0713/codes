import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
value = list(map(int, input().split()))
lst = deque()

for i in range(N):
    if i%2==0:
        lst.append(value[i])
    else:
        lst.appendleft(value[i])

a = lst.pop()
result = lst[0]*a
