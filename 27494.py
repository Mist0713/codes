import sys
input = sys.stdin.readline

N = int(input())

result = 0

if N<2023:
    print(0)
else:
    for i in range(2023, N+1):
        Num = list(map(int, str(i)))
        indexs = [0 ,0, 0, 0, False]
        for j in range(len(Num)):
            if Num[j] == 2:
                if not indexs[4]:
                    indexs[0] = j
                    indexs[4] = True
                else:
                    indexs[2] = j
            elif Num[j] == 0:
                indexs[1] = j
            elif Num[j] == 3:
                indexs[3] = j
        if indexs[4] and indexs[0] < indexs[1] < indexs[2] < indexs[3]:
            # print(indexs)
            result += 1

print(result)

