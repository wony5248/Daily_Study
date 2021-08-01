N, K = map(int, input().split())
child = list(map(int, input().split()))
dif = []
for i in range(1, len(child)):            # 혼자 조일경우 0 -> 차이 저장한 배열에서 K개 만큼 안뽑을 수 있음
    dif.append(child[i] - child[i-1])
dif.sort()
print(sum(dif[0:N-K]))
