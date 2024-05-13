import sys
import heapq
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    isvisited = [False] * k
    max_heap, min_heap = [],[]
    for i in range(k):
        command, num = input().split()
        num = int(num)
        if command == 'I':
            heapq.heappush(max_heap,(-num,i))
            heapq.heappush(min_heap,(num,i))
            isvisited[i] = True
        else:
            if num == 1:
                while max_heap and not isvisited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                    #print("isvisited:", isvisited)
                    #print("minheap:", min_heap)
                    #print("maxheap:", max_heap)
                if max_heap:
                    isvisited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
                    #print("isvisited:", isvisited)
                    #print("minheap:", min_heap)
                    #print("maxheap:", max_heap)
            else:
                while min_heap and not isvisited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                    #print("isvisited:", isvisited)
                    #print("minheap:", min_heap)
                    #print("maxheap:", max_heap)
                if min_heap:
                    isvisited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
                    #print("isvisited:", isvisited)
                    #print("minheap:", min_heap)
                    #print("maxheap:", max_heap)
    while min_heap and not isvisited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not isvisited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    if max_heap and min_heap:
        print(-max_heap[0][0],min_heap[0][0])
    else:
        print("EMPTY")