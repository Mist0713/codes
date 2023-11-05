import sys
input = sys.stdin.readline

p, n = map(int, input().split())

answer = '1'
for i in range(n-2):
    answer += '1'

print(answer + str(p))