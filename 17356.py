import sys
input = sys.stdin.readline

A, B = map(int, input().split())

m = (B-A)/400
print(1/(1+10**m))