sub = list(input())
subnum = 0
score = 0

def calculateScore(character):
    if character == "A":
        return 4.0
    elif character == "B":
        return 3.0
    elif character == "C":
        return 2.0
    elif character == "D":
        return 1.0
    else:
        return 0.0

flag = False

try:
    for i in range(len(sub)):
        a = sub.pop()
        if a == "+":
            flag = True
            a = sub.pop()
            score += 0.5 + calculateScore(a)
            subnum += 1
        else:
            score += calculateScore(a)
            subnum += 1
except:
    print(score/subnum)

if not flag:
    print(score/subnum)