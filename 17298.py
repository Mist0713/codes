import sys
input = sys.stdin.readline

n = int(input())
stack = list(map(int, input().split()))

for i in range(len(stack)):
    cnt = stack.pop(i)
    for j in range(len(stack)):
        cnt = stack
    