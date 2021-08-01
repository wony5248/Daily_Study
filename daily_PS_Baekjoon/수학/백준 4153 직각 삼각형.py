while True:
    length = list(map(int, input().split()))
    if length.count(0) == 3:
        break
    else:
        length.sort()
        x = length[0]
        y = length[1]
        z = length[2]
        if x ** 2 + y ** 2 == z ** 2:
            print("right")
        else:
            print("wrong")