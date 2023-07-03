import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
LENGTH = 21

n = int(input())
parentNode = [[0] * LENGTH for _ in range(n+1)]
visited = [False] * (n+1)
d = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(x, depth):
    visited[x] = True
    d[x] = depth

    for node in graph[x]:
        if visited[node]:
            continue
        parentNode[node][0] = x
        dfs(node, depth + 1)

def setParendNode():
    dfs(1, 0)
    for i in range(1, LENGTH):
        for j in range(1, n+1):
            parentNode[j][i] = parentNode[parentNode[j][i-1]][i-1]


def LCA(a, b):
    if d[a] > d[b]:
        a, b = b, a
    for i in range(LENGTH-1, -1, -1):
        if d[b] - d[a] >= 2**i:
            b = parentNode[b][i]
    if a == b:
        return a
    for i in range(LENGTH-1, -1, -1):
        if parentNode[a][i] != parentNode[b][i]:
            a = parentNode[a][i]
            b = parentNode[b][i]
    return parentNode[a][0]

setParendNode()

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    print(LCA(a, b))