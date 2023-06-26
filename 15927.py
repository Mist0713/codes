def isPalindrome(string, start, end):
    while True:
        if start >= end:
            return True
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1

string = input()
if not isPalindrome(string, 0, len(string) - 1):
    print(len(string))
elif not isPalindrome(string, 0, len(string) - 2):
    print(len(string) - 1)
else:
    print(-1)
