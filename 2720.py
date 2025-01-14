import sys
input = sys.stdin.readline

change = [25, 10, 5, 1]

for _ in range(int(input())):
    lst = []
    money = int(input())
    for i in range(4):
        lst.append(money//change[i])
        money -= lst[-1]*change[i]
    print(*lst)