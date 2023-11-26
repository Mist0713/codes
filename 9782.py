import sys
input = sys.stdin.readline

# def roundTraditional(val, digits):
#     return round(val+10**(-len(str(val))-1), digits)
# n = 1
# while True:
#     lst = list(map(int, input().split()))
#     length = len(lst)
#     if length == 1 and sum(lst) == 0:
#         break
#     lst.sort()
#     if length%2 == 0:
#         print("Case ",n, ": ", roundTraditional((lst[length//2-1]+lst[length//2])/2, 0), sep='')
#     else:
#         print("Case ",n, ": ", roundTraditional(lst[length//2], 0), sep='')
#     n += 1
T = 0
while True :
    data = [*map(int, input().split())]
    if data[0] == 0 : break
    T += 1
    N, D = data[0], data[1:]
    print("Case %d: %.1f" %( T, D[(N + 1) // 2 - 1] if N % 2 else (D[N // 2 - 1] + D[(N // 2)]) / 2) )