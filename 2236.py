import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))

lstForCompare = lst[:]
lstForCompare.sort()
lstForCompare.reverse()

# print(lstForCompare)

answerPower = []
isPowerConnected = [0] * N

if N==K:
    for i in range(K):
        answerPower = [i for i in range(1, N+1)]
        isPowerConnected = [i for i in range(1, N+1)]
elif N>K:
    for i in range(K):
        answerPower.append(lst.index(lstForCompare[i])+1)
        isPowerConnected[lst.index(lstForCompare[i])] = lst.index(lstForCompare[i])+1
elif N<K:
    for i in range(N):
        answerPower.append(lst.index(lstForCompare[i])+1)
        isPowerConnected[lst.index(lstForCompare[i])] = lst.index(lstForCompare[i])+1
    for i in range(K-N):
        answerPower.append(0)


for i in answerPower:
    print(i)

for i in isPowerConnected:
    print(i)
