import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

temp = sum(lst)

if temp == 0:
    print("Stay")
elif temp >0:
    print("Right")
else:
    print("Left")