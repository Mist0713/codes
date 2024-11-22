import sys
from collections import deque

input = sys.stdin.readline

movingX = [2, 2, 1, 1, -1, -1, -2, -2]
movingY = [1, -1, 2, -2, 2, -2, 1, -1]

for _ in range(int(input())):  #! test case 수
    chessPlateWidth = int(input())
    knightLoc = list(map(int, input().split())) + [0]
    arrivalLoc = list(map(int, input().split()))
    graph = deque()
    graph.append(knightLoc)
    isVisited = set()
    isVisited.add((knightLoc[0], knightLoc[1]))

    while graph:
        lst = graph.popleft()
        if lst[0] == arrivalLoc[0] and lst[1] == arrivalLoc[1]:
            print(lst[2])
            break
        for i in range(8):
            nx = lst[0] + movingX[i]
            ny = lst[1] + movingY[i]
            if 0 <= nx < chessPlateWidth and 0 <= ny < chessPlateWidth and (nx, ny) not in isVisited:
                isVisited.add((nx, ny))  
                graph.append([nx, ny, lst[2] + 1]) 
