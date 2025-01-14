lv, result = input().split()
lv = int(lv)

if result == "miss":
    print(0)
elif result == "bad":
    print(lv*200)
elif result == "cool":
    print(lv*400)
elif result == "great":
    print(lv*600)
else:
    print(lv*1000)