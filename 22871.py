import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

def solve(limit, start): #start는 index
    stack = [start]
    while stack:
        for i in range(len(lst)):
            if i>start and (i-start)*(1+abs(lst[start]-lst[i]))<=limit:
                stack.append()
for i in range(n):
    print("hello")