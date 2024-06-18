import sys
input = sys.stdin.readline

def isArithsequence(n : int) -> bool: #!세자릿수 이상일때만 사용 --> 2자리수는 모두 등차수열(한수)
    n = str(n)
    for i in range(len(n)-2): #? 11111 을 생각할때, 3번만 비교
        if int(n[0+i]) + int(n[2+i]) != 2*int(n[1+i]):
            return False
    return True

countTrueValue = 0

N = int(input())

if N//100>=1:
    countTrueValue = 99
    for i in range(100, N+1):
        if isArithsequence(i):
            countTrueValue += 1
else:
    countTrueValue = N

print(countTrueValue)



