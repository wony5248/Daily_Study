import time
start = time.time()

code = {'0':'0000', '1':'0001', '2':'0010', '3':'0011',
         '4':'0100', '5':'0101', '6':'0110', '7':'0111',
         '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
         'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}

secret = {'211':0, '221':1, '122':2, '411':3, '132':4, '231':5, '114':6, '312':7, '213':8, '112':9}

def reduce(c, b, a):
    min_num = min(c,b,a)
    c //= min_num
    b //= min_num
    a //= min_num
    return str(c)+str(b)+str(a)

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        graph[i] = input()

    blst = [''] * N
    for i in range(N):
        for j in range(M):
            blst[i] += code[graph[i][j]]

    result = []
    visited = []
    ans = 0
    for y in range(N):
        a = b = c = 0
        for x in range(M*4-1, -1, -1):
            if b == 0 and c == 0 and blst[y][x] == '1':
                a += 1
            elif a > 0 and c == 0 and blst[y][x] == '0':
                b += 1
            elif a > 0 and b > 0 and blst[y][x] == '1':
                c += 1

            if a > 0 and b > 0 and c > 0 and blst[y][x] == '0':
                result.append(secret[reduce(c, b, a)])
                a = b = c = 0

            if len(result) == 8:
                result = result[::-1]
                value = (result[0] + result[2] + result[4] + result[6]) * 3 + \
                        (result[1] + result[3] + result[5]) + result[7]

                if value % 10 == 0 and result not in visited:
                    ans += sum(result)

                visited.append(result)
                result = []

    print('#%d %d'%(tc, ans))
print("time : ", time.time()-start)