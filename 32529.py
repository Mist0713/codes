import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.reverse()

combined_lst = []
for i in range(len(lst)):
    if i == 0:
        combined_lst.append(lst[0])
    else:
        combined_lst.append(lst[i] + combined_lst[-1])

if combined_lst[-1]<M:
    print(-1)
else:
    for i in range(len(combined_lst)):
        if combined_lst[i]>=M:
            print(len(combined_lst)-i)
            break
