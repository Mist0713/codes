import sys
from collections import deque
input = sys.stdin.readline

start = 1
ladder, snake = map(int, input().split())

answer = [0] * 101
lst = []

isVisited = [False] * 101

for _ in range(ladder+snake):
    lst.append(list(map(int, input().split())))

# print(lst)

def solve(start):
    queue = deque([start])
    isVisited[start] = True
    while queue:
        # print(queue)
        cnt = queue.popleft()
        # print(cnt)
        if cnt == 100:
            print(answer[100])
            return
        for i in range(1, 7):
            posi = cnt + i
            if posi<=100 and isVisited[posi] == False:
                for j in range(ladder + snake):
                    if lst[j][0] == posi:
                        posi = lst[j][1]
                if not isVisited[posi]:
                        isVisited[posi] = True
                        answer[posi] = answer[cnt] + 1
                        queue.append(posi)

solve(1)

# print(isVisited)
# print(answer)