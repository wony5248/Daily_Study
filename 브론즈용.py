while True:
    x = list(map(int, input()))
    if x[0] == 0:
        break
    elif len(x) % 2 == 1:
        if x[:len(x) // 2 + 1] == x[len(x)//2:][::-1]:
            print("yes")
        else:
            print("no")
    elif len(x) % 2 == 0:
        if x[:len(x) // 2] == x[len(x)//2:][::-1]:
            print("yes")
        else:
            print("no")