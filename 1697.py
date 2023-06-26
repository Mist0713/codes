import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
isVisited = [0 for _ in range(100001)]

def BFS(n):
    queue = deque([n])
    while queue:
        a = queue.popleft()
        if a==k:
            return(isVisited[a])
        else:
            for i in [a-1, a+1, a*2]:
                if 0<=i<=100000 and isVisited[i]==0:
                    isVisited[i] = isVisited[a] + 1
                    queue.append(i)

print(BFS(n))