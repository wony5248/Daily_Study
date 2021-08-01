import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    p = list(input().rstrip())
    n = int(input())
    arr = input()[1:-2].split(",")
    lst = []
    iserror = 0
    isreverse = 0

    for j in range(len(p)):
        if p[j] == "R":
            isreverse = 1 - isreverse          # 뒤집힌 상태인지 원상태인지 파악하는 변수 0: 원상태 1: 뒤집힘
        elif p[j] == "D" and arr:
            if isreverse == 1:                 # R때마다 뒤집어주면 시간 오래걸려서 뒤집혔을때는 맨 뒤꺼 빼줌
                arr.pop()
            else:
                arr.pop(0)
        elif p[j] == "D" and not arr:          # iserror 가 1이면 답은 error
            iserror = 1
            break
        if n == 0 and p[j] == "D":
            iserror = 1
            break

    if iserror == 0:
        if isreverse == 1:
            arr.reverse()
        print("[", end="")
        for j in range(len(arr)):
            if j == len(arr) - 1:
                print("%s" % arr[j], end="")
            else:
                print("%s," % arr[j], end="")
        print("]")
    elif iserror == 1:
        print("error")
