import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b, c = map(int, input().split())
    if a<b and b<c:
        print("STAIR")
    elif a<b and b>c:
        print("PEAK")
    else:
        print("NONE")
