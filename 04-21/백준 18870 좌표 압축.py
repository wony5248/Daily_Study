import sys
input =sys.stdin.readline
N = int(input())
coor = list(map(int, input().split()))
zipcoor= {}                         # 입력 받은 좌표의 크기 순서를 저장하는 dict()
scoor = list(sorted(set(coor)))     # 중복 제거하기 위해 set 해주고 다시 list
for i in range(len(scoor)):         # scoor[i]의 크기 순서는 i
    zipcoor[scoor[i]] = i

for i in coor:
    print(zipcoor[i], end=" ")