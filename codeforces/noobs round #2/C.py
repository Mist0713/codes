import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    team = 0
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    lst = sorted(lst)
    lst = lst[::-1]
    for i in range(N):
        if lst[0]>= K:
            team += 1
            lst.pop(0)
    # print(lst)
    if len(lst)==0:
        print(team)
    else:
        # index = -1
        # for i in range(len(lst)-1, 1, -1):
        #     if lst[0] + lst[i] >= K:
        #         index = i
        #         break
        # if index == -1:
        #     print(team)
        # else:
        #     # print(lst[0:i])
        #     print(team + len(lst[0:i+1])//2)
        while len(lst)>=2:
            if lst[0] + lst.pop() >=K:
                team += 1
                lst.pop(0)
        print(team)