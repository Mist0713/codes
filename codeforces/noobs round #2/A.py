import sys
input = sys.stdin.readline

#! 90 degrees === right, -90degress === left

direction = ["E", "S", "W", "N"]

T = int(input())
for _ in range(T):
    num = int(input())
    pos = 0
    comm = list(map(int, input().rstrip()))
    for i in range(num):
        if comm[i] == 0:
            pos += 1
        else:
            pos -= 1
    print(direction[pos%4])
