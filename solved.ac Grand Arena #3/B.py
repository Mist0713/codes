import sys
input = sys.stdin.readline

N = int(input())
water = list(map(int, input().split()))
Q = int(input())
waterTot = sum(water)
print(waterTot)

for _ in range(Q):
    commend = list(map(int, input().split()))
    if commend[0] == 1:
        if water[commend[1]-1] >0:
            waterTot += commend[2] - water[commend[1]-1]
        if water[commend[1]-1] > 0:
            water[commend[1]-1] = commend[2]
        else:
            water[commend[1]-1] = commend[2] * -1
    else:
        waterTot -= water[commend[1]-1]
        water[commend[1]-1] = water[commend[1]-1] * -1
    print(waterTot)