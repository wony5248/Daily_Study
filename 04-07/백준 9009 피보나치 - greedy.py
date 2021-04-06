import sys
input = sys.stdin.readline
T = int(input())
fibo = [0 for _ in range(46)]
fibo[0] = 0
fibo[1] = 1
for i in range(2, 46):                # fibo[45] 는 10억보다 크다.
    fibo[i] = fibo[i - 1] + fibo[i - 2]
for i in range(T):                   
    sumV = int(input())               # 구하고자하는  합
    result = []
    while True:
        if sumV == 0:                 
            break
        for j in range(len(fibo)):     # 피보나치 배열 돌면서
            if fibo[j] > sumV:         # 피보나치 배열 값이 구하고자 하는 합의 값보다 크면
                result.append(fibo[j-1]) # 그 전값 result에 저장
                sumV -= fibo[j-1]        # 합에서 그 전값 빼줌
                break

    result.sort()
    for j in result:
        print(j, end=" ")
    print()