
# 투포인터 사용해서 시간 줄임 --> TLE 회피

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    team = 0
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)

    i, j = 0, N - 1

    while i <= j:
        if lst[i] >= K:
            team += 1
            i += 1
        elif i < j and lst[i] + lst[j] >= K:
            team += 1
            i += 1
            j -= 1
        else:
            j -= 1
    
    print(team)
