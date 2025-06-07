import sys
input = sys.stdin.readline

def roundTraditional(val, digits):
    return round(val+10**(-len(str(val))-1), digits)

def solve(dots):
    ans = 0
    for i in range(len(dots) - 1):
        ans += (dots[i][0] * dots[i + 1][1]) - (dots[i + 1][0] * dots[i][1])
    return roundTraditional(abs(ans) / 2,2)

lst = []

for _ in range(int(input())):
    lst.append(list(map(int, input().split())))
lst.append(lst[0])

print(solve(lst))

