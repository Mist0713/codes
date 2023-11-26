import sys
import math
input = sys.stdin.readline

p, v, k = map(int, input().split())

GCD = (p+1)*(v+1)//math.gcd(p+1, v+1)

A = k - k//(p+1) - k//(v+1) + k//GCD #포함 배제 원리
B = k//GCD
C = k//(v+1) - B
D = k//(p+1) - B

print(A, B, C, D)