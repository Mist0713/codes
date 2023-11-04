import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
num = []

for i in range(len(lst)):
    num.append([0, lst[i]])
    nl = list(map(int, str(lst[i])))
    length = len(nl)
    for j in range(10 - length):
        lst[i] = lst[i] * 10 + nl[j%length]
    num[i][0] = lst[i]

num.sort()
answer = []
for i in range(len(num)-1, -1, -1):
    answer.append(num[i][1])

if sum(answer) == 0:
    print(0)
else:
    print(*answer, sep="")