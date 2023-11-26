import sys
input = sys.stdin.readline

n = int(input())

lst = [1,3] + [0]*(n-1)

for i in range(2,n+1):
    lst[i] = (lst[i-2] + lst[i-1]*2)%9901

print(lst[n])