import sys
def roundTraditional(val, digits):
    return round(val+10**(-len(str(val))-1), digits)

# input = sys.stdin.readline

plus = False

string = input()
for i in range(len(string)):
    if string[i]=="+":
        plus = True
    if string[i]=="=":
        Index = i
d = int(string[Index+1:])
equ = string[:Index]


if plus:
    a, b = equ.split("+")
    c = a[:-1]
    c = int(c)
    b = int(b)
    result = (-1*b+d)/c
    result = roundTraditional(result, 2)
    print(f"%.2f" % result)
else:
    a, b = equ.split("-")
    c = a[:-1]
    c = int(c)
    b = int(b)
    result = (b+d)/c
    result = roundTraditional(result, 2)
    print(f"%.2f" % result)