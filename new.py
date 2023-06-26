from queue import Queue
class Tomato:
    def __init__(self):
        self.index = 0
        self.state = 0
        self.days = 0
ripped = 0
empty = 0
total = 1
days = 0
s = [0] * 11
dist = [1] * 11
for i in range(11):
    s[i] = int(input())
    total *= s[i]
for i in range(1, 11):
    dist[i] = s[i - 1] * dist[i - 1]
tomatoes = [Tomato() for i in range(total)]
q = Queue()
for i in range(total):
    tomatoes[i].state = int(input())
    tomatoes[i].index = i
    if tomatoes[i].state > 0:
        q.put(tomatoes[i])
    elif tomatoes[i].state < 0:
        empty += 1
while not q.empty():
    f = q.get()
    ripped += 1
    days = f.days
    for i in range(22):
        k = i // 2
        sign = 1 - 2 * (i % 2)
        nextIndex = f.index + sign * dist[k]
        dimSize = dist[k] * s[k]
        lmod = f.index % dimSize
        nmod = nextIndex % dimSize
        if nextIndex >= 0 and nextIndex < total and sign * (nmod - lmod) > 0 and not tomatoes[nextIndex].state:
            tomatoes[nextIndex] = Tomato()
            tomatoes[nextIndex].index = nextIndex
            tomatoes[nextIndex].state = 1
            tomatoes[nextIndex].days = f.days + 1
            q.put(tomatoes[nextIndex])
if ripped + empty - total or ripped <= 0:
    days = -1
print(days)