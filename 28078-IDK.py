import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque([])

dirS = 0
dirB = 0

for i in range(n):
    commend = input()
    if commend == "rotate l":
        dirS, dirB += 1, 1