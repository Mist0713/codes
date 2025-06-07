import sys
input = sys.stdin.readline

lst = []

for _ in range(10):
    lst.append(list(map(str, input().split())))

def solve():
    for j in range(10):
        flag = 0
        target = lst[j][j]
        for i in range(10):
            if lst[j][i] != target:
                flag +=1
                break
        for i in range(10):
            if lst[i][j] != target:
                flag += 1
                break
        if flag<2:
            print(1)
            return True
    print(0)
        
solve()

        