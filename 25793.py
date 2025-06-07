import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    a = int(list(str(a))[-1])
    print(10 if(a==0) else pow(a, b, 10))
