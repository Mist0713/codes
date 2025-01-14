import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

stack = []
visible = 0
for i in range(N-1,-1,-1):
    temp = 0
    while stack and stack[-1][1]<lst[i]:
        a = stack.pop()
        temp += a[0]
    stack.append([1+temp, lst[i]])
    visible += stack[-1][0]-1
    # print(stack)

print(visible)

