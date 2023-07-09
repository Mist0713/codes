import sys
input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

testCase = int(input())
for _ in range(testCase):
    M, N, x, y = map(int, input().split())
    while x <= lcm(M, N):
        if x%N == y%N:
            print(x)
            break
        x += M
    else:
        print(-1)