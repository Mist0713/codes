import sys
input = sys.stdin.readline

N, a, b = map(int, input().split())

lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

point = lst[a-1][b-1]
flag = False

for i in range(N):
    if lst[a-1][i] > point:
        print("ANGRY")
        flag = True
        break
    if lst[i][b-1] > point:
        print("ANGRY")
        flag = True
        break

if not flag:
    print("HAPPY")