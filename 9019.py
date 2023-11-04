import sys
input = sys.stdin.readline
from collections import deque
testCase = int(input())

for _ in range(testCase):
    A, B = map(int, input().split())

    isVisited = [False for i in range(10001)]
    deq = deque()
    deq.append([A,''])
    isVisited[A] = True

    while deq:
        num, character = deq.popleft()

        if num == B:
            print(character)
            break

        d = num * 2 % 10000
        if not isVisited[d]:
            isVisited[d] = True
            deq.append([d, character + 'D'])

        s = (num - 1) % 10000
        if not isVisited[s]:
            isVisited[s] = True
            deq.append([s, character + 'S'])

        l = num // 1000 + (num % 1000)*10
        if not isVisited[l]:
            isVisited[l] = True
            deq.append([l, character + 'L'])

        r = num // 10 + (num % 10) * 1000
        if not isVisited[r]:
            isVisited[r] = True
            deq.append([r, character + 'R'])

'''
import sys
from collections import deque
input = sys.stdin.readline

testCase = int(input())

def D(num):
    num *= 2
    if num>9999:
        num %= 10000
    return num

def S(num):
    num -= 1
    if num==0:
        num = 9999
    return num

def L(num):
    return num*10 - num*10//10000*10000 + (num*10//10000)

def R(num):
    return num//10 + num%10*1000

def BFS(currentNum, target):
    isVisted = [False] * 10001
    queue = deque()
    queue.append((currentNum, ""))
    isVisted[currentNum] = True
    while queue:
        num, answer = queue.popleft()
        if num == target:
            print(answer)
            return
        if isVisted[S(num)] == False:
            isVisted[S(num)] = True
            queue.append((S(num), answer + "S"))
        if isVisted[D(num)] == False:
            isVisted[D(num)] = True
            queue.append((D(num), answer + "D"))
        if isVisted[L(num)] == False:
            isVisted[L(num)] = True
            queue.append((L(num), answer + "L"))
        if isVisted[R(num)] == False:
            isVisted[R(num)] = True
            queue.append((R(num), answer + "R"))   
    
for _ in range(testCase):
    a, b = map(int, input().split())
    BFS(a, b)
'''