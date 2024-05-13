import sys
input = sys.stdin.readline

N, M = map(int, input().split())

isVisited = [False] * (N+1)
lst = []

selected = 0

def solve(selected):
    if selected == M:
        print(*lst, sep=' ')
        return
    for i in range(1, N+1):
        if isVisited[i] == False:
            isVisited[i] = True
            lst.append(i)
            solve(selected+1)
            isVisited[i] = False
            lst.pop()

solve(0)


# !hello!
# * Hello!
# ? Hello?
# todo:Hello!
# >= *** -> ++ 
#========================> <====================