import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
graph = [[] for _ in range(n)]
delectNode = int(input())
result = 0

for i in range(len(lst)):
    if lst[i] == -1:
        continue
    else:
        graph[lst[i]].append(i) # 부모 노드에 자식 노드 저장

queue = deque()
queue.append(delectNode)
while queue:
    v = queue.popleft()
    if len(graph[v]) == 0:
        graph[v].append("*")
    else:
        while graph[v]:
            queue.append(graph[v].pop())
        graph[v].append("*")

for i in range(len(graph)-1):
    for j in graph[i]:
        if j == delectNode:
            graph[i].remove(j)

for i in graph:
    if i == []:
        result += 1

print(result)
# print(graph)
