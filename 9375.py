import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    wear = int(input())
    result = 1
    keys = []
    dict = {}
    for i in range(wear):
        clothes, Type = input().split()
        if Type in dict:
            dict[Type] += 1
        else:
            dict[Type] = 1
            keys.append(Type)
    for i in range(len(keys)):
        result *= dict[keys[i]]+1
    if wear == 1:
        print(1)
    else:
        print(result -1)