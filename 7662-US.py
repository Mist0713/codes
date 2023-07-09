import sys
import heapq
input = sys.stdin.readline

testCase = int(input())

for _ in range(testCase):
    minHeap, maxHeap = [], []
    operatorNum = int(input())
    Delcted = [False] * operatorNum
    for i in range(operatorNum):
        oper, num = input().split()
        num = int(num)
        if oper == "I":
            heapq.heappush(minHeap, (num, num))
            heapq.heappush(maxHeap, (-num, num))
        elif oper == "D":
            

