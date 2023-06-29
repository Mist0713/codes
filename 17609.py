import sys
input = sys.stdin.readline

testCase = int(input())

def isPalindrome(s):
    if s[:]!=s[::-1]:
            return 2
    return 1

for _ in range(testCase):
    flag = 0
    string = input().rstrip()
    start = 0
    end = len(string) - 1
    while start<end:
        if string[start] != string[end]:
            flag = 1
            result = []
            result.append(isPalindrome(string[start:end]))
            result.append(isPalindrome(string[start+1:end+1]))
            print(min(result))
            break
        start += 1
        end -= 1
    if flag == 0:
        print(0)
