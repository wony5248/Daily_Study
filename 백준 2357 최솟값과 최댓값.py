# 2357번 최솟값과 최댓값
from math import *
import sys

# 세그먼트 트리 초기화
def initMin(node, start, end):
    if start == end:
        tree_min[node] = arr[start]
        return tree_min[node]

    mid = (start + end) // 2
    tree_min[node] = min(initMin(node*2, start, mid), initMin(node*2+1, mid+1, end))
    return tree_min[node]

def initMax(node, start, end):
    if start == end:
        tree_max[node] = arr[start]
        return tree_max[node]

    mid = (start + end) // 2
    tree_max[node] = max(initMax(node*2, start, mid), initMax(node*2+1, mid+1, end))
    return tree_max[node]

# 최솟값 쿼리
def queryMin(node, start, end, left, right):
    if start > right or end < left:
        return 1000000001

    if left <= start and end <= right:
        return tree_min[node]

    mid = (start + end) // 2
    return min(queryMin(node*2, start, mid, left, right), queryMin(node*2+1, mid+1, end, left, right))

# 최댓값 쿼리
def queryMax(node, start, end, left, right):
    if start > right or end < left:
        return 0

    if left <= start and end <= right:
        return tree_max[node]

    mid = (start + end) // 2
    return max(queryMax(node*2, start, mid, left, right), queryMax(node*2+1, mid+1, end, left, right))

# main
n, m = [int(x) for x in sys.stdin.readline().split()]

# 세그먼트 트리 사이즈 계산
h = int(ceil(log2(n)))       # 트리의 높이
t_size = 1 << (h+1)     # 대략의 트리 총 노드 개수

arr = []
tree_min = [0] * t_size     # 최솟값 저장
tree_max = [0] * t_size     # 최댓값 저장

for _ in range(n):
    arr.append(int(sys.stdin.readline()))

initMin(1,0,n-1)
initMax(1,0,n-1)

for _ in range(m):
    a, b = [int(x) for x in sys.stdin.readline().split()]

    print(queryMin(1, 0, n-1, a-1, b-1), end = ' ')
    print(queryMax(1, 0, n-1, a-1, b-1))