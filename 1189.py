N, M, K = map(int, input().split())

lst = [list(input()) for _ in range(N)]
isVisited = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0

def dfs(x, y, dist):
    global answer
    isVisited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not isVisited[nx][ny] and lst[nx][ny] != 'T':
            isVisited[nx][ny] = True
            if nx == 0 and ny == M-1:
                if dist + 1 == K:
                    answer += 1
            else:
                dfs(nx, ny, dist + 1)
            isVisited[nx][ny] = False
                    
dfs(N-1, 0, 1)
print(answer)