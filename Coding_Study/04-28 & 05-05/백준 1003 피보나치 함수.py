T = int(input())


for i in range(T):
    N = int(input())
    fibo0 = [0 for k in range(41)] # fibo(n) 구할때 나오는 fibo(0)의 갯수
    fibo1 = [0 for k in range(41)] # fibo(n) 구할때 나오는 fibo(1)의 갯수
    fibo0[0] = 1
    fibo0[1] = 0
    fibo1[0] = 0
    fibo1[1] = 1
    for j in range(2, N+1):
        fibo0[j] = fibo0[j - 1] + fibo0[j - 2]
        fibo1[j] = fibo1[j - 1] + fibo1[j - 2]
    print(fibo0[N], fibo1[N])


