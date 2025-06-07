import sys
input = sys.stdin.readline

string = input().rstrip()
check = list(map(str, input().split()))

for i in range(len(check)):
    small = check[i].lower()
    string = string.replace(check[i], small)

print(string)