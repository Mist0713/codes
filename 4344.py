import sys; input = sys.stdin.readline

def roundTraditional(val, digits):
    return round(val+10**(-len(str(val))-1), digits)
    
n = int(input())

for i in range(n):
    score = list(map(int, input().split()))
    num = score.pop(0)
    average = sum(score)/num
    stu = 0
    for j in range(num):
        if score[j]>average:
            stu += 1
    print(format(roundTraditional(stu/num*100, 3), '.3f'), "%",sep='')