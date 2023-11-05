import sys
input = sys.stdin.readline

testCase = int(input())

for _ in range(testCase):
    s = input().rstrip()
    if len(s)%3==0:
        sPrime = s[:len(s)//3]
    else:
        sPrime = s[:len(s)//3+1]
    sPrimeRev = sPrime[::-1]
    sPrimeTail = sPrime[1:]
    sPrimeTailRev = sPrimeRev[1:]
    if s == sPrime + sPrimeRev + sPrime:
        print(1)
    elif s == sPrime + sPrimeTailRev + sPrime:
        print(1)
    elif s == sPrime + sPrimeRev + sPrimeTail:
        print(1)
    elif s == sPrime + sPrimeTailRev + sPrimeTail:
        print(1)
    else:
        print(0)