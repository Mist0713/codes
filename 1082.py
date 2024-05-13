import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
m = int(input())

a = min(lst[1:n-1])
b = min(lst)
answer = []

if m//a == 0:
    print(0)
else:
    answer.append(lst.index(a)+1); m -= a
    for _ in range(m//b):
        answer.append(lst.index(b))
    m -= b*(m//b)
    for i in range(len(answer)-1, -1, -1):
        for j in range(len(lst)-1, -1, -1): #i, j ==> index
            if m+answer[i]-lst[j] > 0
print(answer)