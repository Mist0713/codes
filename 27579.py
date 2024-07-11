import sys
input = sys.stdin.readline

h, k, v, s = map(int, input().split())
answer = 0
while h>0:
    v = v + s - max(1, v//10)
    if v>=k:
        h+=1
    elif 0 < v < k:
        h -=1
        if h == 0:
            v = 0
    elif v<=0:
        h , v = 0, 0
    answer += v
    if s>0:
        s -= 1

print(answer)

