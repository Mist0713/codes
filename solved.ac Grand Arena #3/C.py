import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
answer = 0
flag = False
for i in range(N-1):
    length = 1 
    num = [lst[i]]
    if flag:
        break
    for j in range(i+1, N):
        if lst[j] not in num:
            num.append(lst[j])
        if len(num) !=3:
            length += 1
        else:
            break
        if j == N-1:
            flag = True
    answer = max(answer, length)
print(answer)
