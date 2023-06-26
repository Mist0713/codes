import sys
input = sys.stdin.readline

result = 0
n = int(input())

lst = []
for i in range(n):
    start, end = map(int, input().split())
    lst.append((start, end))

lst.sort(key=lambda x : (x[1], x[0]))
end = 0
for i in lst:
    if i[0]>=end:
        # if i[0] == i[1]:
        #     result +=1
        #     continue
        end = i[1]
        result += 1

print(result)