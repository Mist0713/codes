import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().rstrip())))
isVisted = [[False]*m for _ in range(n)]

def BFS(a, b):
    queue = deque()
    queue.append((a, b))
    isVisted[a][b] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not isVisted[nx][ny] and graph[nx][ny] == 1:
                queue.append((nx, ny))
                isVisted[nx][ny] = True
                graph[nx][ny] = 1 + graph[x][y]

BFS(0,0)
print(graph[n-1][m-1])
# print(graph, isVisted)