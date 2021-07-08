from itertools import combinations

n = int(input())
popul = list(map(int, input().split()))
whole = sum(popul)
nei_no = []
nei = []
res = 1001
for _ in range(n):
    temp = list(map(int, input().split()))
    nei_no.append(temp[0])
    if temp[0]:
        nei.append(temp[1:])
    else:
        nei.append([])

def is_neigh(lst):
    if len(lst) == 1:
        return 1
    q = [lst[0]]
    visited = [0]*n
    visited[lst[0]-1] = 1
    while len(q):
        v = q.pop(0)
        if nei_no[v-1] > 0:
            for v2 in nei[v-1]:
                if v2 in lst and not visited[v2-1]:
                    visited[v2-1] = 1
                    q.append(v2)
    return sum(visited)

def is_possible(part):
    uni = set(range(1,n+1))
    part1 = set(part)
    part2 = tuple(uni - part1)
    if is_neigh(part) + is_neigh(part2) == n:
        return True
    return False

def get_diff(lst):
    summ = 0
    for i in lst:
        summ += popul[i-1]
    other = whole - summ
    return abs(summ-other)

for i in range(1,n//2+1):
    lst = [st for st in combinations(range(1,n+1),i)]
    for st in lst:
        if is_possible(st):
            tmp = get_diff(st)
            if tmp < res:
                res = tmp

if res == 1001:
    res = -1
print(res)