import sys
input = sys.stdin.readline
n = int(input().rstrip())                         # AB ,CD list 일시 시간초과
A = []                                            # AB, CD set 일시 중복없어져서 오답
B = []
C = []
D = []
AB = dict()
count = 0
for i in range(n):
    a, b, c, d = map(int, input().rstrip().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)


for i in range(len(A)):             # 하나씩 탐색하면 N^4라 시간 초과
    for j in range(len(B)):         # 두개의 합을 하나로 보고 탐색
        if not A[i] + B[j] in AB:   # A + B의 합이 AB 딕셔너리에 없으면 1로 초기화
            AB[A[i] + B[j]] = 1
        else:                       # 있다면 해당 key 의 value +1
            AB[A[i] + B[j]] += 1

for i in range(len(C)):             # 나머지 두개의 수 탐색 하면서
    for j in range(len(D)):         # 그 수에 -1 곱한값이 AB 딕셔너리에 있다면
        if -(C[i] + D[j]) in AB:    # 해당값의 value 만큼 더해줌
            count += AB[-(C[i] + D[j])]


print(count)