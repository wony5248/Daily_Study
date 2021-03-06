import sys
N = int(sys.stdin.readline().rstrip())
lst = []
for i in range(N):
    name, korean, english, math = sys.stdin.readline().rstrip().split()
    lst.append([name, int(korean), int(english), int(math)])    #이름,국어점수,영어점수,수학점수 를 하나의 배열로 해서 추가
lst.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))     # 국어점수 낮은순으로 -> 영어 높은순 -> 수학 낮은순으로 ->
for j in range(len(lst)):
    print(lst[j][0])

