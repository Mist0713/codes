import sys
input = sys.stdin.readline

N, M = map(int, input().split()) #N is range of list "LST", M is number of Query

lst = []

for _ in range(N):
    lst.append(int(input()))

for i in range(1, M+1):
    for j in range(N-1):
        if lst[j]%i > lst[j+1]%i:
            lst[j], lst[j+1] = lst[j+1], lst[j]

print(*lst, sep='\n')