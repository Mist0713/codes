import sys
input = sys.stdin.readline

n = int(input())

dp = [1, 1, 2, 3]

if n<=4:
    print(dp[n-1])
else:
    for i in range(4, n):
        dp.append(dp[i-1] + dp[i-3])
    print(dp[-1]%1000000009)
    
print(dp)