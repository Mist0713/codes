import sys
from collections import deque
input = sys.stdin.readline

result = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))
isVisited = [[False]*n for _ in range(n)]

def BFS(a, b):
    global result
    queue = deque()
    queue.append((a, b))
    isVisited[a][b] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and not isVisited[nx][ny] and graph[nx][ny] == 1:
                isVisited[nx][ny] = True
                queue.append((nx, ny))
                graph[nx][ny] = 0
                result += 1

resultLst = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result = 0
            graph[i][j] = 1
            BFS(i, j)
            resultLst.append(result)

print(len(resultLst))
resultLst.sort()
for i in range(len(resultLst)):
    print(resultLst[i])