import sys
input = sys.stdin.readline

N, m, M, T, R = map(int, input().split())
presentBeat = m
exersiseNum = 0
result = 0

if M-m < T:
    print(-1)
else:
    while True:
        if exersiseNum>=N:
            print(result)
            break
        if presentBeat+T<=M:
            exersiseNum += 1
            presentBeat += T
        else:
            presentBeat -= R
        if presentBeat < m:
            presentBeat = m
        result += 1