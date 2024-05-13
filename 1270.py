import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    lst = list(map(int, input().split()))
    num = lst.pop(0)
    dictionary = {}; key = []
    for i in lst:
        if i in key:
            dictionary[i] += 1 
        else:
            key.append(i)
            dictionary[i] = 1
    maximum = 0
    for i in key:
        maximum = max(maximum, dictionary[i])
        if maximum = dictionary[i]
    

        


