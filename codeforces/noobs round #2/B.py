import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    count = 0
    num = int(input())
    lst = list(map(int, input().split()))
    for i in range(len(lst)):
        if lst[i]%2==0:
            count += 1
    if count == num:
        print(-1)
    else:
        print(count)