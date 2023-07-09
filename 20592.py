import sys
input = sys.stdin.readline

testCase = int(input())
a = []
for _ in range(testCase):
    num = int(input())
    lst = list(input().rstrip().split())
    print(lst)
    if num>32:
        print(0) #비둘기 집의 원리에 따라 MBTI가 같은 사람이 적어도 3명 이상
    else:
        answer = sys.maxsize
        for i in range(num):
            for j in range(num):
                for k in range(num):
                    if i == j or j == k or k == i:
                        continue #같은 사람끼리 비교 예외처리
                    else:
                        n = 0
                        for l in range(4):
                            if lst[i][l] != lst[j][l]:
                                n += 1
                            if lst[j][l] != lst[k][l]:
                                n += 1
                            if lst[i][l] != lst[k][l]:
                                n += 1
                        answer = min(answer, n)
        print(answer)
