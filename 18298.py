import sys
input = sys.stdin.readline

def roundTraditional(val, digits):
    return round(val+10**(-len(str(val))-1), digits)

def solve(N):
    lst = []
    ans = 0
    for _ in range(N):
        lst.append(list(map(int, input().split())))
    lst.append(lst[0])

    for i in range(len(lst) - 1):
        ans += (lst[i][0] * lst[i + 1][1]) - (lst[i + 1][0] * lst[i][1])
    return abs(ans) / 2

T = int(input())
answer = 0

for _ in range(T):
    answer += solve(int(input()))

print(int(answer))
