import sys
input = sys.stdin.readline

a, r = list(map(int, input().rstrip())), 0
while len(a)>1:
    a = list(map(int, str(sum(a))))
    r +=1
print(r)
if a[0]%3 ==0:
    print("YES")
else:
    print("NO")

# import sys
# x = sys.stdin.buffer.read()
# if len(x) == 2:
#     print(0)
#     print(['NO','YES'][x[0] in b'0369'])
#     exit(0)
# x = sum(x)-len(x)*48+38
# v = 1
# while x > 9:
#     v += 1
#     y = 0
#     while x:
#         x, r = divmod(x, 10)
#         y += r
#     x = y
# print(v)
# print(['NO','YES'][x in (0,3,6,9)])