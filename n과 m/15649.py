import sys
input = sys.stdin.readline

n, m = map(int, input().split())

lst = []

def solve():
    if len(lst) == m:
        print(*lst, sep=' ')
        return
    for i in range(1, n+1):
        if not (i in lst):
            lst.append(i)
            solve()
            lst.pop()

solve()
