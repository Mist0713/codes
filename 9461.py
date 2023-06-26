import sys
input = sys.stdin.readline

testCase = int(input())

for _ in range(testCase):
    dp = [1,1,1,2,2,3]
    n = int(input())
    if n<=6:
        if n==0:
            print(0)
        else:
            print(dp[n-1])
    else:
        for i in range(5, n-1):
            dp.append(dp[i]+dp[i-4])
        print(dp[-1])