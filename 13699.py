import sys
input = sys.stdin.readline

N = int(input())
valueList = [1]

def dp(n):
    value = 0
    for i in range(n):
        value += valueList[i]*valueList[n-i]
    return value

for i in range(N):
    dp(i)
    
        
