import sys
input = sys.stdin.readline

# n = int(input())
# compair = "IOI"
# for i in range(n-1):
#     compair += "OI"
# m = int(input())
# string = input().rstrip()

# result = 0

# for i in range(m-2-(n-1)*2):
#     if compair == string[i:i+len(compair)]:
#         result += 1

# print(result)

#---------------------------------------------
n = int(input())
m = int(input())
compair = input()
result = 0
streak = 0
i = 0

while i < (m - 1):
    if compair[i:i+3] == 'IOI':
        i += 2
        streak += 1
        if streak == n:
            result += 1
            streak -= 1
    else:
        i += 1
        streak = 0

print(result)