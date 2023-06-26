import math
 
n = int(input())
dp = [0,1]
 
for i in range(2, n+1):
    mini = 1e9
    for j in range(1, int(math.sqrt(i)) + 1):
        mini = min(mini, dp[i - j**2])
    dp.append(mini + 1)
 
print(dp[n])
def roundTraditional(val, digits):
    return round(val+10**(-len(str(val))-1), digits)