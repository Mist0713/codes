import sys
input = sys.stdin.readline

def check(array):
    flag = False
    for i in range(len(array)-1):
        if not array[i]<array[i+1]:
            flag = True
    if not flag:
        print(*array, sep=' ')

n, m = map(int, input().split())

lst = [] #stack

def solve():
    if len(lst) == m:
        check(lst)
        return
    for i in range(1, n+1):
        if not (i in lst):
            lst.append(i)
            solve()
            lst.pop()

solve()