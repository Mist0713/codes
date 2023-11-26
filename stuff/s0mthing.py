className = ["생명실험실", "물리실험실", "화학실험실", "지구과학실험실", "AI실", "멀티미디어실", "무한상상실", "입력종료"]
time = [[], [], [], [], [], [], []]

def tryInput():
    global lst
    print("장소와 시간을 입력하세요 : ", end='')
    a, b = input().split()
    if a in className and 1<=int(b)<=3:
        lst = [a, b]
    else:
        print("잘못된 입력입니다.")
        tryInput()

while True:
    tryInput()
    if lst[0] == "입력종료":
        break
    if lst[1] in time[className.index(lst[0])]:
        print("이미 해당된 장소에 예정된 스케쥴이 있습니다. 다른 시간 또는 장소를 선택하세요.")
    else:
        time[className.index(lst[0])].append(lst[1])

print("전체 사용자의 스케쥴 목록 : ")

for i in range(7):
    if len(time[i]) == 0:
        print("장소 :",className[i], "시간 : 예약 없음", sep=' ')
    else:
        print("장소 :",className[i], "시간 :", sep=' ', end=' ')
        for j in range(len(time[i])):
            print(time[i][j], "면학", sep=' ', end=' ')
        print() 