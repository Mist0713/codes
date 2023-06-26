import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

def BFS(start, end):
    isvisited = [False] * (n+1)
    queue = deque()
    queue.append((start, 0))
    isvisited[start] = True
    while queue:
        S, D = queue.popleft()
        if S == end:
            return D
        for i, j in graph[S]:
            if not isvisited[i]:
                isvisited[i] = True
                queue.append((i, D+j))

for _ in range(n-1):
    a, b, length = map(int, input().split())
    graph[a].append((b, length))
    graph[b].append((a, length))

for _ in range(m):
    s, e = map(int, input().split())
    print(BFS(s, e))
