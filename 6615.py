# import sys
# input = sys.stdin.readline

# def collatzOper(a):
#     if a%2==0:
#         return a//2
#     else:
#         return a*3 + 1

# while True:
#     a, b = map(int, input().split())
#     if a==0 and b==0:
#         break

#     lstA = []
#     lstB = []

SIZE = 1000000
MAX_COUNT = 1000

values_a = [0] * MAX_COUNT
values_b = [0] * MAX_COUNT

def prepare(ptr, value):
    while True:
        ptr[0] = value
        if value == 1:
            return ptr
        ptr += 1
        value = (3 * value + 1) if (value % 2) else (value // 2)

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    ptr_a = prepare(values_a, a)
    ptr_b = prepare(values_b, b)
    while ptr_a >= values_a and ptr_b >= values_b and ptr_a[0] == ptr_b[0]:
        ptr_a -= 1
        ptr_b -= 1
    ptr_a += 1
    ptr_b += 1
    print(f"{a} needs {ptr_a - values_a} steps, {b} needs {ptr_b - values_b} steps, they meet at {ptr_a[0]}")