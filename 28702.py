import sys
input = sys.stdin.readline

string = ["Fizz", "Buzz", "FizzBuzz"]

num = 0 

for i in range(3):
    a = str(input().rstrip())
    if a not in string:
        num = int(a)+3-i

mod5 = num%5
mod3 = num%3

if mod3*mod5 != 0 :
    print(num)
elif mod3+mod5 == 0:
    print(string[2])
elif mod5 == 0:
    print(string[1])
else:
    print(string[0])