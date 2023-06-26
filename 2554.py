import sys
import math
input = sys.stdin.readline

n = int(input())

a = n//10
b = n%10

if a%4==0:
    r = 6
elif a%4 == 1:
    r = 8
elif a%4 == 2:
    r = 4
else:
    r = 2

num = list(str(r*math.factorial(b)))
num.reverse()
if n!=1:
    for i in range(len(num)):
        if num[i] == "0":
            continue
        else:
            print(num[i])
            break
else:
    print(1)