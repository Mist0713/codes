from collections import defaultdict
from bisect import bisect_left
import sys
MAXN = 1 << 17
MAXVAL = 1000000000
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
objx = defaultdict(list)
objy = defaultdict(list)
def getnext(x, y, dir):
    vmove = dir % 2 == 0
    a = x if vmove else y
    b = y if vmove else x
    db = dy[dir] if vmove else dx[dir]
    objs = objx[a] if vmove else objy[a]
    id = bisect_left(objs, (b, 0))
    id += db
    ch = '?'
    if id < 0:
        b = -(MAXVAL + 1)
    elif id == len(objs):
        b = MAXVAL + 1
    else:
        b = objs[id][0]
        ch = objs[id][1]
    return ((a, b), ch) if vmove else ((b, a), ch)
def getpath(x, y, dir):
    pos = (x, y)
    path = [pos]
    while True:
        res = getnext(pos[0], pos[1], dir)
        pos = res[0]
        path.append(pos)
        if res[1] == '/':
            dir = (dir + (3 if dir % 2 != 0 else 1)) % 4
        elif res[1] == '\\':
            dir = (dir + (3 if dir % 2 == 0 else 1)) % 4
        else:
            break
    return path
def getverts(path):
    ret = []
    for i in range(len(path) - 1):
        if path[i][0] == path[i + 1][0]:
            ret.append((path[i][0], (path[i][1], path[i + 1][1])))
            if ret[-1][1][1] < ret[-1][1][0]:
                ret[-1] = (ret[-1][0], (ret[-1][1][1], ret[-1][1][0]))
    return ret
def gethorz(path):
    ret = []
    for i in range(len(path) - 1):
        if path[i][1] == path[i + 1][1]:
            ret.append((path[i][1], (path[i][0], path[i + 1][0])))
            if ret[-1][1][1] < ret[-1][1][0]:
                ret[-1] = (ret[-1][0], (ret[-1][1][1], ret[-1][1][0]))
    return ret
BT = [0] * MAXN
def bit_add(x, v):
    i = x | MAXN
    while i < (MAXN << 1):
        BT[i ^ MAXN] += v
        i += i & -i
def bit_get(x):
    ret = 0
    i = x - 1
    while x != 0:
        ret += BT[i]
        if not i:
            break
        i &= i - 1
    return ret
def countints(vs, hs):
    ys = []
    for v in vs:
        ys.append(v[1][0])
        ys.append(v[1][1])
    for h in hs:
        ys.append(h[0])
    ys.sort()
    ys = list(set(ys))
    for i in range(len(vs)):
        vs[i] = (vs[i][0], (ys.index(vs[i][1][0]), ys.index(vs[i][1][1])))
    for i in range(len(hs)):
        hs[i] = (ys.index(hs[i][0]), hs[i][1])
    vs.sort()
    events = []
    for h in hs:
        events.append(((h[1][0], h[0]), 1))
        events.append(((h[1][1], h[0]), -1))
    events.sort()
    result = 0
    global BT
    BT = [0] * len(BT)
    i, j = 0, 0
    while i < len(events):
        x = events[i][0][0]
        while j < len(vs) and vs[j][0] < x:
            result += bit_get(vs[j][1][1]) - bit_get(vs[j][1][0] + 1)
            j += 1
        bit_add(events[i][0][1], events[i][1])
        i += 1
    return result
def main():
    sys.stdin = open("optics.in", "r")
    sys.stdout = open("optics.out", "w")
    N, bx, by = map(int, input().split())
    objx[0].append((0, 'S'))
    objy[0].append((0, 'S'))
    objx[bx].append((by, 'B'))
    objy[by].append((bx, 'B'))
    for _ in range(N):
        x, y, mr = input().split()
        x, y = int(x), int(y)
        objx[x].append((y, mr[0]))
        objy[y].append((x, mr[0]))
    for it in objx:
        objx[it] = sorted(objx[it])
    for it in objy:
        objy[it] = sorted(objy[it])
    result = 0
    plaser = getpath(0, 0, 0)
    for i in range(4):
        pbarn = getpath(bx, by, i)
        res = countints(getverts(plaser), gethorz(pbarn)) + \
              countints(getverts(pbarn), gethorz(plaser))
        if pbarn[0] == pbarn[-1]:
            result += res
        else:
            result += 2 * res
    print(result // 2)
if __name__ == "__main__":
    main()