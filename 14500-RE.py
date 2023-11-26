import sys
input = sys.stdin.readline

n, m = map(int, input().split())

lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))
isVisited = [[False] * m for _ in range(n)]

answer = 0

dx = [0, 0 ,1 ,-1]
dy = [1, -1, 0, 0]

def dfs(x, y, sum, depth): # without T-mino
    global answer
    if depth == 4:
        answer = max(sum, answer)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and not isVisited[nx][ny]:
            if depth == 2:
                isVisited[nx][nx] = True
                dfs(x, y, sum + lst[nx][ny], depth + 1)
                isVisited[nx][ny] = False
            isVisited[nx][nx] = True
            dfs(nx, ny, sum + lst[nx][ny], depth + 1)
            isVisited[nx][ny] = False

# def Tmino(x, y, sum, depth):
#     global answer
#     isVisited[x][y] = True
#     if depth == 4:
#         answer = max(sum, answer)
#         isVisited[x][y] = False
#         return
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0<=nx<n and 0<=ny<m and not isVisited[nx][ny]:
#             if depth == 2:
#                 isVisited[nx][nx] = True
#                 Tmino(x, y, sum + lst[nx][ny], depth + 1)
#                 isVisited[nx][ny] = False
#             isVisited[nx][nx] = True
#             Tmino(nx, ny, sum + lst[nx][ny], depth + 1)
#             isVisited[nx][ny] = False

for i in range(n):
    for j in range(m):
        isVisited[i][j] = True
        dfs(i, j, lst[i][j], 1)
        # Tmino(i, j, lst[i][j], 1)
        isVisited[i][j] = False

print(answer)
        



# search O-mino --> complete
# x = [0, 0, 1, 1]
# y = [0, 1, 0, 1]
# for i in range(n-1):
#     for j in range(m-1):
#         sum = 0
#         for k in range(4):
#             sum += lst[i+x[k]][j+y[k]]
#         answer = max(answer, sum)

# search I-mino(width) --> complete
# for i in range(n):
#     for j in range(m-3):
#         sum = 0
#         for k in range(4):
#             sum += lst[i][j+k]
#         answer = max(answer, sum)

# search I-mino(length) --> complete
# for i in range(m):
#     for j in range(n-3):
#         sum = 0
#         for k in range(4):
#             sum += lst[j+k][i]
#         answer = max(answer, sum)

# search T-mino
# x = [0, 0, 0, 1, -1]
# y = [0, 1, -1, 0, 0]
