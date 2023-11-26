def s():
    for i in list(map(int, input().split())):
        if i*i!=i:
            return print("F")
    return print("S")
s()