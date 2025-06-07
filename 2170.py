import sys
input = sys.stdin.readline

N = int(input())
answer = 0
line = []

for _ in range(N):
    x, y = map(int, input().split())
    line.append((x, y))

line.sort()

lst = (line[0][0], line[0][1])

for i in range(1, N):
    if line[i][0] <= lst[1]:
        lst = (lst[0] ,max(lst[1], line[i][1]))
    else:
        answer += lst[1] - lst[0]
        lst = (line[i][0], line[i][1])

print(answer + lst[1] - lst[0])
    
