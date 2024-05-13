import sys
input = sys.stdin.readline

n , m = map(int, input().split())
isvisited = [False] * (n+1)

def solve(n, m, lst):
    if sum(isvisited) == m:
        print(*lst, sep=' ')
        return
    lst = []
    solve(n, m, lst)

print(solve(n, m, isvisited))

