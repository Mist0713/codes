import sys
input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))

freq_arr = [0] * 11 #? 숫자의 index와 freq가 일치

for i in range(len(lst)):
    freq_arr[lst[i]] += 1

start, end = 0, len(lst)-1

while start<=end:
    