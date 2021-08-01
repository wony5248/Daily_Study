for i in range(10):
    dump = int(input())
    lst = list(map(int, input().split()))
    while dump:
        lst.sort()
        lst[99] -=1
        lst[0] +=1
        lst.sort()
        dump -= 1
        if lst[99] - lst[0] == 0 or lst[99] - lst[0] ==1:
            break
    print("#%d %d" %(i+1, lst[99] - lst[0]))

