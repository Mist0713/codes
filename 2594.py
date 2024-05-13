import sys
input = sys.stdin.readline

def timeToMinute(time):
    hour, minute = divmod(time, 100)
    return hour * 60 + minute

times = []
endTime = 0
for _ in range(int(input())):
   a, b = map(int, input().split())
   times.append((timeToMinute(a)-10, timeToMinute(b)+10))
   endTime = max(endTime, timeToMinute(b)+10)
                
    
times.sort(key = lambda x : x[0])
# print(times)
answer = 0
answer = max(answer, times[0][0]-600, 1320-endTime)
maxtime = 0
for i in range(len(times)-1): #if n = 3 range(2) = [0,1]
    maxtime = max(maxtime, times[i][1])
    answer = max(answer, times[i+1][0]-maxtime)

print(answer)



