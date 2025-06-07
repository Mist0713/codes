import sys
input = sys.stdin.readline

N = int(input())
# lst = [[]*(N+1)]*(N+1)

# print(lst)

# for _ in range(N-1):
#     a, b = map(int, input().split())
#     print(a, b)
#     lst[0].append(1)


lst = [[] for i in range(N+1)]

print(lst)

for _ in range(N-1):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

print(lst)