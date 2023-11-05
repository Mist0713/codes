import sys
input = sys.stdin.readline
n, a = map(int, input().split())

answer = [0, 0]

for i in range(n):
    lst = list(input().rstrip())
    cnt = 0
    check = False
    for j in lst:
        if j == '1' and check == False:
            cnt += 1
            check = True
        elif j == '0':
            check = False
    if answer[0] < cnt:
        answer[0] = cnt
        answer[1] = 1
    elif answer[0] == cnt:
        answer[1] += 1
        
print(*answer, sep=' ')