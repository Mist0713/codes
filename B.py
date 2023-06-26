import sys
from collections import deque
input = sys.stdin.readline

testCase = int(input())

dx = [1, -1, 0 , 0]
dy = [0, 0, 1, -1]

def BFS(a, b):
    count = 1
    global isVisited
    queue = deque()
    queue.append((a, b))
    isVisited[a][b] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]
            if 0<=n_x<=2 and 0<=n_y<=2 and isVisited[n_x][n_y] == False:
                isVisited[n_x][n_y] = True
                if graph[n_x][n_y] == "O":
                    queue.append((n_x, n_y))
                    count += 1
    return count
                    
                

for _ in range(testCase):
    result = []
    graph = []
    for i in range(3):
        graph.append(list(input().rstrip()))
    check = list(map(int, input().split()))
    check.pop(0)
    queue = deque()
    isVisited = [[False] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if graph[i][j] == "O" and isVisited[i][j] == False:
                result.append(BFS(i, j))
    result.sort()
    if result == check:
        print(1)
    else:
        print(0)