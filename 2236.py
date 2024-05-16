import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))

lstForCompare = lst[:]
lstForCompare.sort()

print(lstForCompare)

answerPower = []
isPowerConnected = []

for i in range(K):
    
    answerPower.append(lst.index(lstForCompare[i]))
    