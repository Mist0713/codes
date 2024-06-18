import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def solve(sequence = []):
    if len(sequence) == M:
        print(*sequence, sep=' ')
        return
    for i in range(1, 1+N):
        solve(sequence + [i])

solve()