import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
friends = list(map(int, input().split()))

answer = m

for i in range(m):
    if lst[i] in friends:
        answer -= 1

print(answer)
