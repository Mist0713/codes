import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
graph = []
isVisited = [[False]*m for _ in range(n)]
result = 0

for i in range(n):
    graph.append(list(input().rstrip()))

def BFS(a, b):
    global result
    queue = deque()
    queue.append((a, b))
    isVisited[a][b] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]
            if 0<=n_x<n and 0<=n_y<m and not isVisited[n_x][n_y] and graph[n_x][n_y] != "X":
                if graph[n_x][n_y] == "P":
                    graph[n_x][n_y] = "O"
                    result += 1
                isVisited[n_x][n_y] = True
                queue.append((n_x, n_y))

for i in range(n):
    for j in range(m):
        if graph[i][j] == "I":
            BFS(i, j)

if result == 0:
    print("TT")
else:
    print(result)