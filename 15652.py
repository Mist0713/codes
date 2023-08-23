import sys
input = sys.stdin.readline

n, m = map(int, input().split())

result = []

def solve(begin):
    if len(result) == m:
        print(*result, sep=" ")
        return
    for i in range(begin, n+1):
        result.append(i)
        solve(i)
        result.pop()

solve(1)