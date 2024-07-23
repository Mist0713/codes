S = ''

while True:
    try:
        S += str(input())
    except EOFError:
        break

num = list(map(int, S.split(',')))

print(sum(num))