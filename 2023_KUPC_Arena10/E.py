def count_alpha(string):
    count = {}

    for char in string:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    for value in count.values():
        if value % 2 != 0:
            return False
    
    return True

n = int(input())
string = input()
n = n//2
a = string[:n]
b = string[-n:]
a += b

if count_alpha(a):
    print("Yes")
else:
    print("No")