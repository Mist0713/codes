import sys
input = sys.stdin.readline

stringA = input().rstrip()
stringB = input().rstrip()

result = 0

lst = [[0] * (len(stringB)+1) for _ in range(len(stringA)+1)]

for i in range(1, len(stringA)+1):
    for j in range(1, len(stringB)+1):
        if stringA[i-1] == stringB[j-1]:
            lst[i][j] = lst[i-1][j-1] + 1
            result = max(result, lst[i][j])
        else:
            lst[i][j] = max(lst[i][j-1], lst[i-1][j])
            result = max(result, lst[i][j])

print(result)

answer = []
i = len(stringA)
j = len(stringB)
while True:
    if lst[i][j] <= 0:
        break
    if lst[i-1][j] == lst[i][j]:
        i -= 1
    elif lst[i][j-1] == lst[i][j]:
        j -= 1
    else:
        answer.append(stringA[i-1])
        i -= 1
        j -= 1

# print(*lst, sep="\n")

answer = answer[::-1]
print(*answer, sep="")