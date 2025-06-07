import sys
input = sys.stdin.readline

integers = [str(x) for x in range(10)]

N = int(input())
a = list(input().rstrip())
answer = 0

cnt = ""
for i in range(N):
    if a[i] in integers:
        cnt += a[i]
    else:
        if cnt !="":
            answer += int(cnt)
        cnt = ""
answer += int(cnt) if cnt!= "" else 0

print(answer)