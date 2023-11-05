import sys
input = sys.stdin.readline
n, a = map(int, input().split())

answer = [0, 0]

for i in range(n):
    lst = list(int(input()))
    cnt = 0
    check = False
    for j in range(a):
        if not check and lst[j] == 1:
            cnt+=1
            check = True
        elif lst[j] == 0:
            check == 0
    if cnt>answer[0]:
        answer[0] = cnt
        answer[1] = 1
    elif cnt == answer[0]:
        answer[1] += 1

print(*answer, sep=' ')
            