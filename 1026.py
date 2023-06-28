import sys
input = sys.stdin.readline

minx, maxx = map(int ,input().split())
isanswer = [False] * (max-min+1)
result = max-min+1

for i in range(2, int(max**0.5+1)):
    square = i**2
    for j in range((((min-1)//square)+1)*square, max+1, square):
        if not isanswer[j-min] :
            isanswer[j-min] = True
            result -= 1
print(result)