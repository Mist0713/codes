import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def BFS(v):
    queue = deque()
    queue.append(v)
    isVisited[v] = 1
    while queue:
        num = queue.popleft()
        for i in graph[num]:
            if not isVisited[i]:
                isVisited[i] = isVisited[num] + 1
                queue.append(i)

result = []
for i in range(1, n+1):
    isVisited = [0] * (n+1)
    BFS(i)
    result.append(sum(isVisited))

print(result.index(min(result))+1)